# Project Report: Safal Mess Demand Forecaster

## **Course:** [Fundamentals of AI and ML]

## 1. Problem Statement

Large-scale institutional cafeterias, such as a college mess, struggle with severe food wastage and financial inefficiency due to unpredictable daily demand. Safal Mess caters to approximately 2,000 students, but the daily consumption of food items fluctuates heavily.These can vary fluctuate based on which meal is provided, which day it is, are any exam nearby , or is it holiday and many more.But mess staff keeps preparing same amount of food everyday that results to wastage of food.To solve this problem i made a machine learning model which will evaluate all these criteria and could suggest mess staff whether how much foof should be prepared on a particular day .

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
