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
And it is not the problem only for institutuion but most of the places it could be for restaurant,gurudwaras(where they feed people on daily basis in langar.
There also consumption would vary on different factors so a similar kind of model could be trained for such places to reduce the wastage of food and help these places financially. 

## 3. Methodology & Approach

To solve this, I built a three-stage machine learning pipeline:

- **Phase 1: Data Synthesis:** Because real historical logs were unavailable, I programmed a data generator (`01-generate_data.py`) on the basis of my personal observations that which item is consumed more and which is consumed less. I created a base schedule for 500 days(based on my academic calender for holidays and exams schedule), mapping the actual menu of Safal Mess. I applied demand modifiers based on the days of the week,exam periods, holidays, and weekends. Natural daily noise was also added for realism.
![mess_menu](https://github.com/user-attachments/assets/8c4cfc4e-7589-4fe5-8957-040ed2518156)

- **Phase 2: Model Training:** I used `pandas` to manage the dataset and `scikit-learn` for preprocessing, applying `LabelEncoder` to convert categorical text (days, meals, categories) into numerical features. I trained two models—Linear Regression and a Random Forest Regressor. Random Forest was chosen as the primary model to capture the non-linear relationships between holidays, item types, and demand.
- **Phase 3: Deployment & Interaction:** I  trained model and encoders using `pickle`. I then built an Command Line Interface (`03-predict.py`) that allows mess staff to input a date and meal type, outputting exact unit predictions and give advice (e.g., "Make LESS", "OK").And to make it more interactive, with the help of html,css and flask i made an interactive ui so it can be used by anyone including non-technical persons.
<img width="694" height="879" alt="Screenshot 2026-03-27 180520" src="https://github.com/user-attachments/assets/0e1555dc-0ef0-46b2-b527-a282927a7eb0" />


## 4. Key Decisions and Challenges Faced

- **Challenge: Lack of Real Data:** The biggest hurdle was the absence of historical mess data.
- **Decision:** I decided to programmarically generate synthetic data based on my personal observation. 
- **Challenge: Handling Categorical Data:** Machine learning models require numbers, but my data consisted of text strings like "Breakfast" or "South Indian".
- **Decision:** I implemented Label Encoding to transform these strings into integers.

## 5. What I Learned

This project pushed me beyond my regular learning and make something that could solve a real world challenge. I learnt these libraries like scikit-learn a long ago but never implemented in real life world but with this peoject i learnt to use my knowledge and implement to solve some real-life world problems.

