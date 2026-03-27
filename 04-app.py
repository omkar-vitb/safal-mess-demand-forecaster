from flask import Flask, render_template, request
import pickle
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)


MODEL_PATH = "models/safal_model.pkl"

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        safal_package = pickle.load(f)
    safal_model    = safal_package["model"]
    safal_features = safal_package["features"]
    safal_encoders = safal_package["encoders"]
else:
    print(f"ERROR: {MODEL_PATH} not found. Please ensure the model exists.")


MEAL_ITEMS = {
    "Breakfast": [
        ("Poha", "north indian", 1400),
        ("Idli",  "south indian",  484),
        ("Bread",  "bread items", 560),
        ("Butter",   "bread items",560),
        ("Tea",  "beverage",    1200),
        ("Coffee",  "beverage",   600),
        ("Milk", "beverage",  400),
    ],
    "Lunch": [
        ("Rajma",  "veg curry",   1800),
        ("Dal Tadka",   "dal",   1800),
        ("Roti",  "roti/rice",   1800),
        ("Mutter Pulao",   "roti/rice",   1600),
        ("Sweet Boondi",   "dessert",   500),
        ("Mixed Veg Salad", "salad",  800),
        ("Pickle",     "condiment", 400),
    ],
    "High Tea": [
        ("Cutlet", "snack",    550),
        ("Cho. Noodles",  "snack",    800),
        ("Tea",    "beverage",1000),
        ("Coffee",   "beverage",  500),
        ("Milk",   "beverage", 300)
    ],
    "Dinner": [
        ("Paneer Masala",   "veg curry",  1800),
        ("Dal Fry",  "dal",   1800),
        ("Butter Roti",  "roti/rice", 1600),
        ("Jeera Rice", "roti/rice", 1600),
        ("Gulab Jamun",   "dessert",  500),
        ("Chicken Biryani", "biryani", 1800),
        ("Veg Biryani", "biryani",  1200),
    ],
}

DAY_NAMES = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def safe_encode(encoder, value):
    try:
        return encoder.transform([value])[0]
    except (ValueError, KeyError):
        return 0

def predict_demand(day_of_week, meal_type, item_name,
                   item_category, quantity_made,
                   month, is_exam_week, is_holiday_nearby, is_weekend):
    input_row = {
        "day_encoded":  safe_encode(safal_encoders["day"],  day_of_week),
        "meal_encoded":   safe_encode(safal_encoders["meal"], meal_type),
        "item_encoded":  safe_encode(safal_encoders["item"], item_name),
        "category_encoded": safe_encode(safal_encoders["category"], item_category),
        "quantity_made":  quantity_made,
        "month":    month,
        "is_exam_week":    is_exam_week,
        "is_holiday_nearby": is_holiday_nearby,
        "is_weekend":        is_weekend,
    }
    input_df = pd.DataFrame([input_row])[safal_features]
    pred = safal_model.predict(input_df)[0]
    pred = max(0, int(round(pred)))
    pred = min(pred, quantity_made)
    return pred

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    form_data = {}

    if request.method=="POST":
        date_str = request.form.get("date", "")
        meal_type = request.form.get("meal", "Lunch")
        is_exam = 1 if request.form.get("exam_week") else 0
        is_holiday= 1 if request.form.get("holiday") else 0

        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
        except:
            dt = datetime.today()
        
        month  = dt.month
        day_of_week = DAY_NAMES[dt.weekday()]
        is_weekend  = 1 if dt.weekday() >= 5 else 0

        form_data = {
            "date": date_str,
            "meal": meal_type,
            "exam_week": is_exam,
            "holiday": is_holiday,
        }

        items = MEAL_ITEMS.get(meal_type, [])
        results = []
        for item_name, category, qty_made in items:
            pred = predict_demand(
                day_of_week, meal_type, item_name,
                category, qty_made, month,
                is_exam, is_holiday, is_weekend
            )
            fill_pct = round((pred / qty_made) * 100, 1)
            
            # Advice Logic
            if fill_pct >= 90:
                advice, badge = "Make More", "more"
            elif fill_pct >= 50:
                advice, badge = "Quantity OK", "ok"
            else:
                advice, badge = "Make Less", "less"

            results.append({
                "item":     item_name,
                "made":     qty_made,
                "pred":     pred,
                "fill":     fill_pct,
                "advice":   advice,
                "badge":    badge,
            })

        # Sort results by predicted demand (highest first)
        results.sort(key=lambda x: x["pred"], reverse=True)

    # CRITICAL: Ensure your file is named index.html inside the templates/ folder
    return render_template("index.html",
                           results=results,
                           form_data=form_data,
                           meals=list(MEAL_ITEMS.keys()))

if __name__ == "__main__":
    app.run(debug=True, port=5000)