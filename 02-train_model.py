
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

os.makedirs("outputs",exist_ok=True)
os.makedirs("models",exist_ok=True)

print("="*55)
print("safal mess demand forecaster")
print("="*55)

# loading data
print("\n loading data")
safal_df=pd.read_csv("data/safal_mess_data.csv")
print(f"loaded{len(safal_df)}rows and {safal_df.shape[1]}columns")

print("\n converting text columns to numbers")

safal_day_encoder=LabelEncoder()
safal_meal_encoder=LabelEncoder()
safal_item_encoder=LabelEncoder()
safal_category_encoder=LabelEncoder()

safal_df["day_encoded"]= safal_day_encoder.fit_transform(safal_df["day_of_week"])
safal_df["meal_encoded"]= safal_meal_encoder.fit_transform(safal_df["meal_type"])
safal_df["item_encoded"]= safal_item_encoder.fit_transform(safal_df["item_name"])
safal_df["category_encoded"]=safal_category_encoder.fit_transform(safal_df["item_category"])


safal_features = [
    "day_encoded",
    "meal_encoded",
    "item_encoded",
    "category_encoded", 
    "quantity_made",
    "month", 
    "is_exam_week", 
    "is_holiday_nearby", 
    "is_weekend",
]


safal_target="quantity_sold"

x = safal_df[safal_features]
y = safal_df[safal_target]

print(f"features used:{safal_features}")
print(f"target :{safal_target}")


print("\n splitting data:80% train, 20% test")
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=7
)
print(f"training samples:{len(x_train)}")
print(f"testing samples:{len(x_test)}")


print("\ntraining models")


print("training linear regression")
safal_lr_model = LinearRegression()
safal_lr_model.fit(x_train, y_train)


print("training random forest (stronger model)")
safal_rf_model=RandomForestRegressor(
    n_estimators=100, 
    max_depth=10, 
    random_state=7,
    n_jobs=-1 
)
safal_rf_model.fit(x_train, y_train)


print("evaluating models on test data")
print("-"*25)

safal_results={}

for model_name,model in [("linear regression",safal_lr_model),
                           ("random forest",safal_rf_model)]:
   
    predictions = model.predict(x_test)
    predictions = np.clip(predictions,0,None)

    # calculate accuracy metrics
    mae=mean_absolute_error(y_test, predictions)
    rmse=np.sqrt(mean_squared_error(y_test, predictions))
    r2=r2_score(y_test, predictions)

    safal_results[model_name]={
        "mae":mae,"rmse":rmse,"r2": r2,"preds":predictions
    }

    print(f"\n{model_name}:")
    print(f"r² score = {r2:.4f}(1.0 = perfect)")
    print(f"mae={mae:.1f}(avg error in units)")
    print(f"rmse={rmse:.1f}")

print("-" * 25)

#picking the best model based on r²
safal_best_name=max(safal_results, key=lambda m: safal_results[m]["r2"])
safal_best_model=safal_rf_model if safal_best_name == "random forest" else safal_lr_model
safal_best_r2 =safal_results[safal_best_name]["r2"]
print(f"\n best model: {safal_best_name}(r²={safal_best_r2:.4f})")

#saving the model
print("\nsaving best model")
safal_model_package={
    "model":safal_best_model,
    "features":safal_features,
    "encoders":{
        "day":safal_day_encoder,
        "meal": safal_meal_encoder,
        "item": safal_item_encoder,
        "category":safal_category_encoder,
    }
}
with open("models/safal_model.pkl", "wb") as f:
    pickle.dump(safal_model_package, f)



print("generating plots")

best_preds=safal_results[safal_best_name]["preds"]

#plot1
fig,axes = plt.subplots(1, 3, figsize=(14,5))
fig.suptitle("safal mess forecaster-model comparison",fontsize=13,fontweight="bold")

for ax, metric, color in zip(axes,
                              ["mae","rmse","r2"],
                              ["#4c72b0","#c44e52", "#55a868"]):
    vals  = [safal_results[m][metric] for m in safal_results]
    names = list(safal_results.keys())
    bars  = ax.bar(names, vals, color=color, alpha=0.85, edgecolor="white", width=0.5)
    ax.set_title(metric, fontsize=11)
    ax.set_ylabel(metric)
    ax.tick_params(axis="x", rotation=10)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() * 1.02, f"{val:.2f}",
                ha="center", fontsize=9)

plt.tight_layout()
plt.savefig("outputs/plot1_model_comparison.png", dpi=150)
plt.close()
print("  saved: plot1_model_comparison.png")

# plot 2: actual vs predicted 
fig, ax = plt.subplots(figsize=(7, 6))
sample_idx = np.random.choice(len(y_test), size=min(400, len(y_test)), replace=False)
ax.scatter(y_test.values[sample_idx], best_preds[sample_idx],
           alpha=0.35, s=15, color="#4c72b0", label="predicted vs actual")
max_val = max(float(y_test.max()), float(best_preds.max()))
ax.plot([0, max_val], [0, max_val], "r--", lw=1.5, label="perfect prediction line")
ax.set_xlabel("actual quantity sold")
ax.set_ylabel("predicted quantity sold")
ax.set_title(f"actual vs predicted ({safal_best_name})\nr² = {safal_best_r2:.4f}")
ax.legend()
plt.tight_layout()
plt.savefig("outputs/plot2_actual_vs_predicted.png", dpi=150)
plt.close()
print("  saved: plot2_actual_vs_predicted.png")

#  plot 3: feature importance (only for random forest)
if hasattr(safal_best_model, "feature_importances_"):
    feat_imp = pd.Series(
        safal_best_model.feature_importances_, index=safal_features
    ).sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    feat_imp.plot(kind="barh", ax=ax, color="#55a868", edgecolor="white", alpha=0.85)
    ax.set_title(f"feature importance — {safal_best_name}\n"
                 "(which factors affect demand most?)")
    ax.set_xlabel("importance score")
    plt.tight_layout()
    plt.savefig("outputs/plot3_feature_importance.png", dpi=150)
    plt.close()
    print("  saved: plot3_feature_importance.png")

#plot4 average demand ratio by category
safal_df["demand_ratio"] = safal_df["quantity_sold"] / safal_df["quantity_made"]
cat_demand = (safal_df.groupby("item_category")["demand_ratio"]
                       .mean()
                       .sort_values(ascending=True))

fig, ax = plt.subplots(figsize=(10, 6))
cat_demand.plot(kind="barh", ax=ax, color="#c44e52",edgecolor="white", alpha=0.85)
ax.set_title("safal mess — avg demand ratio by food category\n"
             "(quantity sold ÷ quantity made — closer to 1.0 = always runs out)")
ax.set_xlabel("average demand ratio")
ax.axvline(x=0.70, color="navy", linestyle="--", lw=1.2,label="0.70 line")
ax.legend()
plt.tight_layout()
plt.savefig("outputs/plot4_demand_by_category.png",dpi=150)
plt.close()
print("  saved: plot4_demand_by_category.png")

# plot5 15 most demanded dishes at safal mess
top_items = (safal_df.groupby("item_name")["quantity_sold"]
                      .mean()
                      .sort_values(ascending=False)
                      .head(15))

fig, ax = plt.subplots(figsize=(10,6))
top_items.sort_values().plot(kind="barh",ax=ax,
                              color="#4c72b0", edgecolor="white", alpha=0.85)
ax.set_title("top 15 most consumed items at safal mess\n(average per serving day)")
ax.set_xlabel("avg quantity sold")
plt.tight_layout()
plt.savefig("outputs/plot5_top15_items.png", dpi=150)
plt.close()
print("saved: plot5_top15_items.png")

print("\n"+"="*55)
print("  pipeline complete!")
print(f"best model: {safal_best_name}|r²={safal_best_r2:.4f}")
print("model saved → models/safal_model.pkl")
print("plots saved → outputs/ folder")
print("next step  → run predict.py to make predictions")
print("="*55)
