# Project Report: Safal Mess Demand Forecaster
**Name:-omkar kumar**
**registration number:-25BAI10893**
**project title:-Safal-Mess-Demans-Forecaster**

## 1. Problem Statement
College messes often prepare a fixed quantity of food. However, actual student demand fluctuates wildly based on factors like:

Menu Items: (eg.biryani is consumed much more while bhindi is consumed less but mess staff kepps making same amount of food everyday that leads to wastage of lot of food.)
Time of Year: Demand drops during holidays or when many students go home due to any special occasions like wedding seasons or if many student exams got over early because of FFCS system here at VIT BHOPAL.
Exam time: Demand dips slightly during exam weeks as students skip meals or eat lightly.
Weekends: demand spikes as special meals are given on weekends like chole bature and birtani.But on the other part many student generally prefere to skip the meals in the breakfast they like to sleep late.
So there are many factors which influences the consumption of food and it leads to a lot of food wastages on a daily basis so i trained a model by keeping all these criteria into mind and trained a model to predict the consumption of food on a particular day.The aim of the project is to reduce the wastage of food by a high margin.



## 2. Significance of the Problem

Solving this problem is highly relevant as it will help to reduce wastage of food by a significant margin and this will also help financially to the institution.

## 3. Methodology & Approach

To solve this, I built a three-stage machine learning pipeline:

- **Phase 1: Data Synthesis:** Because real historical logs were unavailable, I programmed a data generator (`01-generate_data.py`) grounded in real-world observations. I created a base schedule for 500 days, mapping the actual menu of Safal Mess. I applied demand modifiers based on the days of the week,exam periods, holidays, and weekends. Natural daily noise was also added for realism.
- **Phase 2: Model Training:** I used `pandas` to manage the dataset and `scikit-learn` for preprocessing, applying `LabelEncoder` to convert categorical text (days, meals, categories) into numerical features. I trained two models—Linear Regression and a Random Forest Regressor. Random Forest was chosen as the primary model to capture the non-linear relationships between holidays, item types, and demand.
- **Phase 3: Deployment & Interaction:** I serialized the trained model and encoders using `pickle`. I then built an interactive Command Line Interface (`03-predict.py`) that allows mess staff to input a date and meal type, outputting exact unit predictions and give advice (e.g., "Make LESS", "OK").

## 4. Key Decisions and Challenges Faced

- **Challenge: Lack of Real Data:** The biggest hurdle was the absence of historical mess logs.
- **Decision:** I decided to programmatically generate synthetic data. Ensuring this data wasn't too "perfect" was a challenge. I solved this by injecting random mathematical noise and programming strict logical constraints (e.g., scaling demand down explicitly during dates overlapping with known holidays or campus events).
- **Challenge: Handling Categorical Data:** Machine learning models require numbers, but my data consisted of text strings like "Breakfast" or "South Indian".
- **Decision:** I implemented Label Encoding to transform these strings into integers. I had to carefully export these encoders alongside the model using a Python dictionary and `pickle` so that the prediction script could interpret new user inputs correctly.

## 5. What I Learned

This project pushed me beyond my regular learning and prompted me to make something useful which could be implemented in real world and can be useful and i also learn many things like:

1. Translating human observations into programmatic, rule-based data generation.
2. Understanding the importance of feature engineering and how drastically it affects model accuracy.
3. Structuring a Machine Learning project into modular scripts (Generate -> Train -> Predict) rather than a single, messy file.
4. Designing a user-friendly terminal interface to make Python code usable for a non-technical end-user.
