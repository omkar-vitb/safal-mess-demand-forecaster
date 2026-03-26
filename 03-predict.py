
import pickle
import pandas as pd

print("Loading Safal Mess trained model...")
with open("models/safal_model.pkl", "rb") as f:
    safal_package = pickle.load(f)

safal_model    = safal_package["model"] 
safal_features = safal_package["features"]  
safal_encoders = safal_package["encoders"] 

print("Model loaded successfully!\n")


def safe_encode(encoder, value):
    """Convert a text label to its number using the saved encoder."""
    try:
        return encoder.transform([value])[0]
    except ValueError:
     
        return 0


def predict_safal_demand(day_of_week, meal_type, item_name,
                          item_category, quantity_made,
                          month, is_exam_week, is_holiday_nearby, is_weekend):

    input_row = {
        "day_encoded":safe_encode(safal_encoders["day"],day_of_week),
        "meal_encoded":safe_encode(safal_encoders["meal"],meal_type),
        "item_encoded": safe_encode(safal_encoders["item"],item_name),
        "category_encoded": safe_encode(safal_encoders["category"],item_category),
        "quantity_made":quantity_made,
        "month": month,
        "is_exam_week":is_exam_week,
        "is_holiday_nearby":is_holiday_nearby,
        "is_weekend":is_weekend,
    }


    input_df = pd.DataFrame([input_row])[safal_features]


    prediction = safal_model.predict(input_df)[0]


    prediction = max(0, int(round(prediction)))
    prediction = min(prediction, quantity_made)

    return prediction



test_scenarios = [
    ("Normal Thursday Lunch — Rajma",
     "Thursday", "Lunch", "Rajma", "Veg Curry", 1800, 9, 0, 0, 0),

    ("Sunday Lunch — Chicken Biryani (weekend spike)",
     "Sunday", "Lunch", "Chicken Biryani", "Biryani", 1800, 10, 0, 0, 1),

    ("Monday Breakfast — Idli (South Indian, low demand)",
     "Monday", "Breakfast", "Idli","South Indian", 484, 9, 0, 0, 0),

    ("Monday Breakfast — Bread (fallback item, very low)",
     "Monday","Breakfast","Bread","Bread Items", 560, 9, 0, 0, 0),

    ("Exam Week — Butter Roti (demand dips in exams)",
     "Tuesday","Dinner", "Butter Roti", "Roti/Rice", 1600, 10, 1, 0, 0),

    ("Diwali Break — Rajma (most students went home)",
     "Monday","Lunch", "Rajma", "Veg Curry", 1800, 10, 0, 1, 0),

    ("High Tea — Cutlet (1-piece limited snack)",
     "Wednesday","High Tea","Cutlet", "Snack", 550, 11, 0, 0, 0),

    ("High Tea — Noodles (bowl item, more popular)",
     "Thursday", "High Tea","Cho. Noodles", "Snack", 800, 11, 0, 0, 0),

    ("Sunday Dinner — Gulab Jamun (always finishes!)",
     "Sunday", "Dinner","Gulab Jamun", "Dessert", 500, 9, 0, 0, 1),

    ("Wednesday Dinner — Paneer Masala (most loved dish)",
     "Wednesday", "Dinner", "Paneer Masala","Veg Curry", 1800, 3, 0, 0, 0),
]

print("=" * 65)
print("  Safal Mess — Demand Predictions")
print("=" * 65)
print(f"\n  {'Scenario':<48} {'Made':>5} {'Pred':>6} {'Fill%':>6}")
print("  " + "-" * 68)

for desc,day, meal,item,cat,qty,month,exam,hol,wknd in test_scenarios:
    pred     = predict_safal_demand(day, meal, item, cat, qty, month, exam, hol, wknd)
    fill_pct=(pred / qty) * 100
    print(f"{desc:<48} {qty:>5} {pred:>6} {fill_pct:>5.1f}%")

print("\n Fill% Guide:")
print("90–100% Almost sold out Safal Mess should make MORE")
print("50–89% Normal range Quantity is about right")
print("Below 50% High wastage  Safal Mess should make LESS")
print("=" * 65)



MEAL_ITEMS = {
    "Breakfast": [
        ("Poha", "north indian", 1400),
        ("Idli", "south indian", 484),
        ("Bread", "bread items", 560),
        ("Butter", "bread items", 560),
        ("Jam", "bread items", 400),
        ("Tea", "beverage", 1200),
        ("Coffee", "beverage", 600),
        ("Milk", "beverage", 400),
    ],
    "Lunch": [
        ("Rajma", "veg curry", 1800),
        ("Dal Tadka", "dal", 1800),
        ("Roti", "roti/rice", 1800),
        ("Mutter Pulao", "roti/rice", 1600),
        ("Sweet Boondi", "dessert", 500),
        ("Mixed Veg Salad", "salad", 800),
        ("Pickle", "condiment", 400),
    ],
    "High Tea": [
        ("Cutlet", "snack", 550),
        ("Cho. Noodles", "snack", 800),
        ("Tea", "beverage", 1000),
        ("Coffee", "beverage", 500),
        ("Milk", "beverage", 300),
    ],
    "Dinner": [
        ("Paneer Masala", "veg curry", 1800),
        ("Dal Fry", "dal", 1800),
        ("Butter Roti", "roti/rice", 1600),
        ("Jeera Rice", "roti/rice", 1600),
        ("Gulab Jamun", "dessert", 500),
        ("Chicken Biryani", "biryani", 1800),
        ("Veg Biryani", "biryani", 1200),
    ],
}

DAY_NAMES = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def run_interactive():
    print("\n" + "="*45)
    print("   Safal Mess — Staff Demand Predictor")
    print("="*45)

    # get date
    date_str = input("\nEnter date (DD-MM-YYYY): ").strip()
    try:
        from datetime import datetime
        dt = datetime.strptime(date_str, "%d-%m-%Y")
        month = dt.month
        day_of_week = DAY_NAMES[dt.weekday()]
        is_weekend = 1 if dt.weekday() >= 5 else 0
    except:
        print("Invalid date, using today as fallback")
        from datetime import datetime
        dt = datetime.today()
        month = dt.month
        day_of_week = DAY_NAMES[dt.weekday()]
        is_weekend = 1 if dt.weekday() >= 5 else 0

    # get meal
    print("\nSelect meal:")
    print("  1) Breakfast  2) Lunch  3) High Tea  4) Dinner")
    meal_choice = input("Enter number: ").strip()
    meal_map = {"1":"Breakfast","2":"Lunch","3":"High Tea","4":"Dinner"}
    meal_type = meal_map.get(meal_choice, "Lunch")

    # exam/holiday
    exam = 1 if input("\nIs it exam week? (y/n): ").strip().lower() == "y" else 0
    holiday = 1 if input("Is holiday nearby? (y/n): ").strip().lower() == "y" else 0

    # predict all items for that meal
    items = MEAL_ITEMS.get(meal_type, [])
    print(f"\n{'='*45}")
    print(f"  Predicted Demand — {meal_type} ({day_of_week})")
    print(f"{'='*45}")
    print(f"  {'Item':<22} {'Predicted':>10}  {'Advice'}")
    print("  " + "-"*42)

    for item_name, category, qty_made in items:
        pred = predict_safal_demand(
            day_of_week, meal_type, item_name,
            category, qty_made, month,
            exam, holiday, is_weekend
        )
        fill = (pred / qty_made) * 100
        if fill >= 90:
            advice = "Make MORE"
        elif fill >= 50:
            advice = "OK"
        else:
            advice = "Make LESS"
        print(f"  {item_name:<22} {pred:>6} units   {advice}")

    print("="*45)

run_interactive()
