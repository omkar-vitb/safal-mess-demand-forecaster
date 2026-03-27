
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

best_preds=safal_results[safal_best_name]["preds"]


