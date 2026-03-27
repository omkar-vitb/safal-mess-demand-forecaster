"""
this is not real data this has been created by me but it could be implemented with real data and can be used by safal mess .

based on my personal observation:-
- 2000 students total, mostly north indian
- south indian items: consumed by ~15-20% students only as most students are north indian so south indian items are consumed by only ~15-20% students only
- bread/butter/jam: ~25% (as this is because this is not the main item for breakfast this is just served for those who dont want to eat that main items for breakfast )
- tea > coffee > milk consumption ratio (as per observation)
- pickle/condiments: small side, ~35% take it
- buttermilk: popular with everyone, ~55%
- desserts (kheer, gulab jamun, custard): limited quantity made,
  but almost fully consumed (~94%) since everyone wants them
- veg and non-veg dinner are mutually exclusive choices:
  non-veg = ~40% students, veg = ~60%
- biryani on sunday: demand spike
- exam weeks and holidays
"""

#importing libraries
import pandas as pd
import numpy as np
from datetime import date, timedelta
import random

#seeding
np.random.seed(7)  
random.seed(7)

# semester 1:sep 1 2025 – nov 25 2025 
# winter break: dec 2025 – jan 17 2026 (due to protest from 25 nov to 17 january was declared holidays for us freshers)
# semester 2: feb 2 2026 – may 2026
# these holidays data is for the period sep 2025 → apr 2026 )
safal_mess_total_students=2000
start_date=date(2025,9,1)
num_days=500
all_dates=[(start_date+timedelta(days=i)) for i in range(num_days)]

#sem1 mid-term:oct 8–17,2025
#sem2 mid-term:mar 9–20,2026
#sem1 end-term :jan 19–31,2026
safal_exam_periods=[
    ((date(2025, 10, 8),date(2025, 10, 17))),# sem1 mid-term
    ((date(2026, 1, 19),date(2026, 1, 31))),# sem1 end-term
    ((date(2026, 3, 9),date(2026, 3, 20))),# sem2 mid-term
]

#holidays
safal_holiday_windows=[
    ((date(2025, 9, 5),date(2025, 9, 6))),# onam / anant chaturdashi
    ((date(2025, 10, 2),date(2025, 10, 2))),# gandhi jayanti / dussehra
    ((date(2025, 10, 20),date(2025, 10, 24))),# diwali break
    ((date(2025, 12, 1),date(2026, 1, 17))),# winter break(protest)
    ((date(2026, 1, 12),date(2026, 1, 16))),# pongal break
    ((date(2026, 1, 26),date(2026, 1, 26))),# republic day
    ((date(2026, 2, 15),date(2026, 2, 15))),# maha shivratri
    ((date(2026, 2, 26),date(2026, 2, 28))),# advitya fest
    ((date(2026, 3, 3),date(2026, 3, 4))),# holi
    ((date(2026, 3, 26),date(2026, 3, 26))),# rama navami
]

def is_exam_week(d):
    return int((any(s<=d<=e for s,e in safal_exam_periods)))

def is_holiday_nearby(d):
    return int((any(s<=d<=e for s,e in safal_holiday_windows)))



# base_demand_fraction = the fraction of relevant students take this item (based on observation but could be implemented with real data)
#(item_name, item_category, base_demand_fraction)
safal_menu={
    "monday":{
        "breakfast":[
            ("idli","south indian",0.20),
            ("vada","south indian",0.18),
            ("sambhar","south indian",0.18),
            ("chutney","condiment",0.15),
            ("banana","fruit",0.55),
            ("bread","bread items",0.25),
            ("butter jam","bread items",0.22),
            ("tea","beverage",0.50),
            ("coffee","beverage",0.30),
            ("milk","beverage",0.20),
        ],
        "lunch":[
            ("tawa roti","roti/rice",0.75),
            ("jeera aloo","veg curry",0.65),
            ("dhal fry","dal", 0.70),
            ("butter milk","beverage",0.55),
            ("mix salad","salad",0.40),
            ("plain rice","roti/rice",0.72),
            ("more kuzhambu","south indian",0.17),
            ("raw banana portyal","south indian",0.15),
            ("pepper rasam", "south indian",0.16),
            ("pickle","condiment",0.35),
        ],
        "high tea": [
            ("kachori", "snack",0.70),
            ("tamarind chutney","condiment", 0.55),
            ("tea","beverage", 0.50),
            ("coffee","beverage",0.30),
            ("milk","beverage",0.20),
        ],
        "dinner": [
            ("kadhai mix veg","veg curry",0.60),
            ("egg gravy","non-veg",0.38),
            ("butter roti","roti/rice",0.75),
            ("multi grain kitchadi","roti/rice",0.45),
            ("veg portyal","south indian",0.16),
            ("plain rice","roti/rice",0.70),
            ("tomato rasam","south indian",0.17),
            ("rice kheer","dessert",0.93),
            ("tea","beverage",0.50),
            ("coffee","beverage",0.30),
            ("milk","beverage",0.20),
            ("pickle","condiment",0.35),
        ],
    },
    "tuesday": {
        "breakfast":[
            ("poha","snack",0.72),
            ("jalebi","dessert",0.78),
            ("pongal","south indian",0.18),
            ("chutney","condiment",0.15),
            ("jeera aloo","veg curry",0.55),
            ("mix cutfruit salad","fruit", 0.45),
            ("bread","bread items", 0.25),
            ("butter jam","bread items",0.22),
            ("tea","beverage", 0.50),
            ("coffee","beverage",0.30),
            ("milk","beverage",0.20),
        ],
        "lunch": [
            ("white channa","veg curry",0.72),
            ("poori","roti/rice",0.80),
            ("mix dal","dal", 0.68),
            ("mix salad","salad",0.40),
            ("south indian plain rice","south indian", 0.18),
            ("bottle gourd kuzhambu","south indian", 0.14),
            ("tomato rasam","south indian",0.16),
            ("butter milk","beverage", 0.55),
            ("pickle","condiment",0.35),
        ],
        "high tea": [
            ("samosa","snack",0.82),
            ("aloo lader matter","snack",0.75),
            ("red sauce chutney","condiment", 0.55),
            ("tea","beverage", 0.50),
            ("coffee","beverage", 0.30),
            ("milk","beverage",0.20),
        ],
        "dinner":[
            ("butter roti","roti/rice",0.75),
            ("fresh custard","dessert",0.94),
            ("bhindi masala","veg curry",0.62),
            ("dal tadka","dal",0.70),
            ("plain rice","roti/rice",0.70),
            ("pepper rasam","south indian",0.16),
            ("pickle","condiment",0.35),
            ("tea","beverage",0.50),
            ("coffee","beverage",0.30),
            ("milk","beverage",0.20),
        ],
    },
    "wednesday": {
        "breakfast": [
            ("pav bhaji","snack",0.78),
            ("upma","south indian",0.20),
            ("chutney","condiment",0.15),
            ("sprouts","healthy",  0.38),
            ("banana", "fruit",0.55),
            ("boiled egg","non-veg",0.45),
            ("bread","bread items",0.25),
            ("butter jam","bread items",0.22),
            ("tea","beverage", 0.50),
            ("coffee", "beverage", 0.30),
            ("milk", "beverage", 0.20),
        ],
        "lunch": [
            ("veg kofta","veg curry",0.70),
            ("dal tadka","dal",  0.70),
            ("mutter pulao","roti/rice", 0.73),
            ("roti", "roti/rice", 0.75),
            ("sweet boondi","dessert",0.92),
            ("mixed veg salad","salad", 0.40),
            ("south indian plain rice","south indian",0.18),
            ("vegetable sambhar","south indian",  0.17),
            ("pickle", "condiment",  0.35),
        ],
        "high tea": [
            ("cutlet","snack",0.75),
            ("red chilli sauce","condiment",0.55),
            ("tea","beverage", 0.50),
            ("coffee","beverage",0.30),
            ("milk","beverage", 0.20),
        ],
        "dinner": [
            ("paneer masala","veg curry",0.80),
            ("kadai chicken masala","non-veg",0.40),
            ("plain dal", "dal", 0.65),
            ("butter roti","roti/rice",  0.75),
            ("plain rice","roti/rice", 0.70),
            ("vegi rasam","south indian",0.16),
            ("pickle","condiment",0.35),
            ("tea","beverage", 0.50),
            ("coffee","beverage", 0.30),
            ("milk","beverage",0.20),
        ],
    },
    "thursday": {
        "breakfast": [
            ("aloo paratha","roti/rice", 0.80),
            ("dahi", "dairy", 0.65),
            ("banana", "fruit", 0.55),
            ("boiled egg", "non-veg", 0.45),
            ("bread","bread items", 0.25),
            ("butter jam","bread items",0.22),
            ("tea","beverage", 0.50),
            ("coffee",  "beverage", 0.30),
            ("milk", "beverage", 0.20),
        ],
        "lunch": [
            ("rajma","veg curry", 0.82),
            ("jeera rice","roti/rice", 0.78),
            ("roti", "roti/rice",  0.75),
            ("seasonal veg",  "veg curry",  0.58),
            ("onion", "condiment",  0.45),
            ("mixed veg salad","salad", 0.40),
            ("veg sambar",  "south indian", 0.17),
            ("parripu rasam", "south indian", 0.15),
            ("beetroot portyal","south indian", 0.14),
            ("pickle", "condiment",  0.35),
        ],
        "high tea": [
            ("cho. noodles", "snack", 0.85),
            ("fried idli", "south indian", 0.20),
            ("coconut chutney", "condiment", 0.18),
            ("tea",   "beverage", 0.50),
            ("coffee",  "beverage", 0.30),
            ("milk", "beverage",  0.20),
        ],
        "dinner": [
            ("egg gravy","non-veg", 0.38),
            ("green peas masala",  "veg curry",  0.62),
            ("dal fry","dal",  0.68),
            ("jeera rice", "roti/rice",     0.72),
            ("butter roti","roti/rice",.75),
            ("teej halwa", "dessert", 0.93),
            ("pepper rasam","south indian",0.16),
            ("pickle","condiment",0.35),
            ("tea","beverage",0.50),
            ("coffee","beverage", 0.30),
            ("milk", "beverage", 0.20),
        ],
    },
    "friday": {
        "breakfast": [
            ("onion uthappam","south indian",0.20),
            ("onion tomato chutney","condiment",0.17),
            ("sprouts", "healthy",  0.38),
            ("fruit salad",  "fruit", 0.50),
            ("boiled egg", "non-veg",0.45),
            ("bread","bread items",0.25),
            ("butter jam","bread items",0.22),
            ("tea", "beverage", 0.50),
            ("coffee", "beverage",  0.30),
            ("milk",  "beverage", 0.20),
        ],
        "lunch": [
            ("kadi pakoda",  "veg curry",0.72),
            ("dal fry", "dal",0.68),
            ("plain rice", "roti/rice",0.72),
            ("roti",  "roti/rice",0.75),
            ("mix salad", "salad", 0.40),
            ("south indian plain rice","south indian",0.18),
            ("brinjal kuzhambu", "south indian",  0.14),
            ("veg aviyal", "south indian",  0.15),
            ("pickle","condiment",0.35),
        ],
        "high tea": [
            ("vada pav",  "snack",0.83),
            ("green chutney","condiment",.60),
            ("tea", "beverage", .50),
            ("coffee","beverage",0.30),
            ("milk","beverage",  0.20)
        ],
        "dinner": [
            ("tandoori butter chicken gravy","non-veg",0.42),
            ("kadai paneer","veg curry",0.78),
            ("dal tadka",  "dal",0.68),
            ("plain roti", "roti/rice",  0.75),
            ("plain rice", "roti/rice",0.70),
            ("south indian plain rice","south indian",0.18),
            ("puli rasam",    "south indian",0.16),
            ("pickle",  "condiment",  0.35),
            ("tea",  "beverage", 0.50),
            ("coffee",  "beverage", 0.30),
            ("milk","beverage",0.20),
        ],
    },
    "saturday": {
        "breakfast": [
            ("chole", "veg curry",0.80),
            ("bhature", "roti/rice", 0.82),
            ("mix cutfruit salad",  "fruit",  0.45),
            ("sprouts","healthy", 0.38),
            ("bread", "bread items", 0.25),
            ("butter jam", "bread items",0.22),
            ("tea","beverage",0.50),
            ("coffee", "beverage",0.30),
            ("milk","beverage",  0.20),
        ],
        "lunch": [
            ("corn palak", "veg curry",0.68),
            ("ghee rice",  "roti/rice",  0.72),
            ("dal makhni","dal", 0.78),
            ("plain roti", "roti/rice",0.75),
            ("south indian plain rice","south indian",0.18),
            ("potato kara portyal", "south indian",  0.15),
            ("mix veg sambar", "south indian",  0.17),
            ("rasam", "south indian",  0.16),
            ("butter milk","beverage",   0.55),
            ("pickle", "condiment",  0.35),
        ],
        "high tea": [
            ("bread pakoda","snack",0.78),
            ("red tomato chutney",  "condiment", 0.55),
            ("tea","beverage", 0.50),
            ("coffee", "beverage",0.30),
            ("milk","beverage", 0.20),
        ],
        "dinner": [
            ("veg pulao", "roti/rice", 0.65),
            ("lahsun gravy",  "veg curry",  0.62),
            ("dal makhani",  "dal",0.75),
            ("plain roti", "roti/rice",0.75),
            ("thaur dal fry", "south indian",  0.16),
            ("south indian plain rice","south indian",0.18),
            ("parripu rasam",       "south indian", 0.15),
            ("pickle", "condiment",  0.35),
            ("tea","beverage",0.50),
            ("coffee","beverage",  0.30),
            ("milk", "beverage", 0.20),
        ],
    },
    "sunday": {
        "breakfast": [
            ("masala dosa","south indian",  0.22),
            ("mix veg dosa","south indian",  0.20),
            ("sambhar", "south indian",  0.18),
            ("chutney", "condiment", 0.17),
            ("sprouts",  "healthy", 0.38),
            ("banana",  "fruit", 0.55),
            ("boiled egg", "non-veg",  0.45),
            ("bread",   "bread items",  0.25),
            ("butter jam",  "bread items", 0.22),
            ("tea",   "beverage",  0.50),
            ("coffee",  "beverage",  0.30),
            ("milk",  "beverage",  0.20),
        ],
        "lunch": [
            ("veg biryani",   "biryani", 0.82),
            ("chicken biryani", "biryani",  0.87),
            ("butter paneer masala","veg curry", .80),
            ("dal kolhapuri", "dal",   0.68),
            ("onion raita",  "dairy",   0.60),
            ("plain roti",  "roti/rice", 0.70),
            ("pickle",  "condiment", 0.35),
        ],
        "high tea": [
            ("white sauce pasta",  "snack",   0.80),
            ("red sauce pasta",  "snack",    0.78),
            ("sauce chutney",  "condiment",0.55),
            ("tea",   "beverage",  0.50),
            ("coffee",     "beverage",   0.30),
            ("milk", "beverage",  0.20),
        ],
        "dinner": [
            ("aloo white peas masala","veg curry",   0.65),
            ("dal makhani",  "dal", 0.75),
            ("plain rice",  "roti/rice",  0.70),
            ("roti",  "roti/rice",  0.75),
            ("south indian plain rice","south indian",0.18),
            ("bhindi portyal", "south indian",  0.15),
            ("parripu rasam",   "south indian",  0.15),
            ("veg samba soup",   "south indian",  0.16),
            ("gulab jamun",  "dessert",  0.94),
            ("pickle",      "condiment",0.35),
            ("tea",    "beverage",  0.50),
            ("coffee", "beverage",  0.30),
            ("milk",   "beverage",  0.20),
        ],
    },
}

#quantities that safal mess prepare beforehand
def safal_quantity_made(item_name,item_category,base_demand,meal_type):
    
    if item_category=="dessert":
        return random.randint(420,530)                  

    if item_category=="snack" and meal_type=="high tea":
        if "noodles" in item_name or "pasta" in item_name:
            return random.randint(700,900)               
        return random.randint(450,620)               

    if item_category=="south indian":
        return int(safal_mess_total_students*0.22*1.1) 

    if item_category=="bread items":
        return int(safal_mess_total_students*0.28)       

    if item_category=="condiment":
        return random.randint(500,700)                

    if item_category=="beverage":
        return int(safal_mess_total_students*base_demand*1.05)

   
    return int(safal_mess_total_students*base_demand*random.uniform(1.05,1.15))



safal_rows=[]

for d in all_dates:
    day_name=d.strftime("%A").lower()
    month=d.month
    exam=is_exam_week(d)
    holiday=is_holiday_nearby(d)
    is_weekend=int(day_name in ("saturday","sunday"))

    day_menu=safal_menu.get(day_name,{})

    for meal_type, items in day_menu.items():
        for (item_name,item_category,base_demand) in items:

            qty_made=safal_quantity_made(item_name, item_category,
                                           base_demand, meal_type)
            demand=base_demand

            # during exam weeks: students prefers to skip meal or eat less so they dont feel dizzy
            # tea/coffee demand goes up during exams (late night energy)
            if exam:
                if item_category in ("veg curry","dal","roti/rice","biryani"):
                    demand*=random.uniform(0.80, 0.90)
                if item_category=="beverage":
                    demand*=random.uniform(1.05, 1.15)

            # holiday- on holidays student prefer not to go to mess
            if holiday:
                demand*=random.uniform(0.55,0.75)   # significant dip, students go home

            # on weekend due to special items like biryani demand spike
            if is_weekend:
                if item_category=="biryani":
                    demand*=random.uniform(1.10,1.20)
                if item_category in ("dessert","snack"):
                    demand*=random.uniform(1.05,1.10)

            # during advitya students prefered to eat outside so mess food demand goes below
            if date(2026, 2, 26)<=d<=date(2026, 2, 28):
                demand*=random.uniform(0.60, 0.75)

            # adding  natural daily noise (~±8%) 
            demand*=random.uniform(0.92,1.08)
            demand=min(max(demand, 0.0),1.0)

            qty_sold = min(int(qty_made*demand),qty_made)

            safal_rows.append({
                "date":d.isoformat(),
                "day_of_week":day_name,
                "month":month,
                "meal_type": meal_type,
                "item_name":item_name,
                "item_category": item_category,
                "quantity_made":qty_made,
                "quantity_sold":qty_sold,  
                "is_exam_week":  exam,
                "is_holiday_nearby":holiday,
                "is_weekend":is_weekend,
            })


safal_df=pd.DataFrame(safal_rows)

#we are training 80 percent data and testing for rest 20 so its
unique_dates = sorted(safal_df["date"].unique())
split_index  = int(len(unique_dates) * 0.80)
split_date   = unique_dates[split_index]

safal_df["split"] = safal_df["date"].apply(
    lambda x: "train" if x < split_date else "test"
)

train_df = safal_df[safal_df["split"] == "train"].drop(columns="split")
test_df  = safal_df[safal_df["split"] == "test"].drop(columns="split")
full_df  = safal_df.drop(columns="split")

#saving
full_df.to_csv("data/safal_mess_data.csv",       index=False)
train_df.to_csv("data/safal_mess_train.csv",     index=False)
test_df.to_csv("data/safal_mess_test.csv",       index=False)

print("=" * 55)
print("  Safal Mess — Data Generation Complete")
print("=" * 55)
print(f"  Total rows   : {len(full_df)}")
print(f"  Training rows: {len(train_df)}  (dates before {split_date})")
print(f"  Testing rows : {len(test_df)}  (dates from  {split_date})")
print(f"\n  Saved to data/ folder:")
print(f"    safal_mess_data.csv   ← full dataset")
print(f"    safal_mess_train.csv  ← for training")
print(f"    safal_mess_test.csv   ← for testing")
print(f"\n  Sample (first 5 rows):")
print(full_df[["date","meal_type","item_name","quantity_made","quantity_sold"]].head())
