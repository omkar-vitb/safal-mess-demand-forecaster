# Safal Mess Demand Forecaster 

## Overview
The **Safal Mess Demand Forecaster** is an machine learning project made by me to solve the food wastage problem in mess in day to day life. .


## The Problem
College messes often prepare a fixed quantity of food. However, actual  demand fluctuates wildly based on factors like:
* **Menu Items:** (eg.biryani is consumed much more while bhindi is consumed less but mess staff kepps making same amount of food everyday that leads to wastage of food.)
* **Time of Year:** Demand drops during holidays or when many students go home due to any special occasions like wedding seasons or if many student exams got over early because of **FFCS** system here at VIT BHOPAL.
* **Exam time:** Demand dips slightly during exam weeks as students skip meals or eat lightly.
* **Weekends:** demand spikes as special meals are given on weekends like chole bature and biryani. 
**So there are many factors which influences the consumption of food and it leads to a lot of food wastages on a daily basis so i trained a model by keeping all these criteria into mind and trained a model to predict the consumption of food on a particular day.The aim of the project is to reduce the wastage of food by a high margin.**

## ORIGINAL MESS MENU ON WHICH DATA HAS BEEN GENERATED AND TRAINED 
![mess_menu](https://github.com/user-attachments/assets/80ba26db-9dd5-40d8-bbf9-64f533e452e7)

## HOLIDAYS DATA HAS BEEN TAKEN FROM ACADEMIC CALENDER OF VIT BHOPAL
<img width="1842" height="845" alt="Screenshot 2026-03-25 144925" src="https://github.com/user-attachments/assets/083d3606-0272-4fed-a99b-0057d020d3eb" />
<img width="1836" height="811" alt="Screenshot 2026-03-25 144939" src="https://github.com/user-attachments/assets/1382cd12-4093-4d74-affe-7d0042675ff5" />
<img width="1848" height="846" alt="Screenshot 2026-03-25 144955" src="https://github.com/user-attachments/assets/a066671b-cb44-423a-a768-d7cfea1d947c" />
<img width="1849" height="865" alt="Screenshot 2026-03-25 145010" src="https://github.com/user-attachments/assets/d7f5d4bb-84f8-4205-a372-56e05a7a78cb" />
<img width="1855" height="844" alt="Screenshot 2026-03-25 145020" src="https://github.com/user-attachments/assets/31ebfc0b-d36e-4a17-8a45-3879b41ae500" />
<img width="1855" height="833" alt="Screenshot 2026-03-25 145034" src="https://github.com/user-attachments/assets/99f55a2d-f056-478a-bce9-ec3ccef4aa52" />
<img width="1837" height="829" alt="Screenshot 2026-03-25 145121" src="https://github.com/user-attachments/assets/d46ae871-4eb4-48a2-a74e-17bd227b41c2" />



## Features that has been added in the project.
1.  **Data Generator (`01-generate_data.py`)** **Due to lack of original data ,i have generated data by myself(in the file 01-generate_data.py) keeping the original menu of the mess in mind.**  
2.  **Model Trainer (`02-train_model.py`):** trained on Linear Regressor and Random forest .
3.  **Interactive Predictor (`03-predict.py and 04-app.py`):** here mess staff can enter the day and few other factors like Is it exam week? or Is holiday nearby? and other factors that can influence the food consumption which will help them to predict how much quantity of food needs to be prepared.

## Tech Stack
* **Language:** Python,html,css
* **Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`,flask.

## Setup & Installation

*1. Clone the repository:*
   git clone-> https://github.com/omkar-vitb/safal-mess-demand-forecaster.git.

*2. run the following command to install pandas,numpy,matplotlib and scikit-learn.*
pip install pandas numpy scikit-learn matplotlib.

*3. How to run:*
- 01- First run `generate_data.py`.
- 02- Run `train_model.py`.
- 03- Run `predict.py`.
- 04- run app.py
.

*4.* **Here in predict.py one needs to enter the following data:-**
  - **Step 1:** Enter date (DD-MM-YYYY): e.g., 20-05-2026.
  - **step 2:** Select meal:
  1) Breakfast  2) Lunch  3) High Tea  4) Dinner
Enter number: 2 (we want to predict for lunch)
- **Step 3.** Is it exam week? (y/n): n
- **Step 4.** Is holiday nearby? (y/n): n

**5.** The following table will be created which will help mess staff to know how much food need to be prepared.
============================================= 
  Predicted Demand — Lunch (Wednesday)        
============================================= 
  | Item | Predicted | Advice |
| :--- | :--- | :--- |
| Rajma | 1455 units | OK |
| Dal Tadka | 1447 units | OK |
| Roti | 1454 units | OK |
| Mutter Pulao | 1194 units | OK |
| Sweet Boondi | 413 units | OK |
| Mixed Veg Salad | 310 units | **Make LESS** |
| Pickle | 115 units | **Make LESS** |

**And finally to make it more interactive i used html,css and flask to make this interactive so anyone whether the person is technical or non-technical can use it easily** 

<img width="679" height="886" alt="Screenshot 2026-03-27 185703" src="https://github.com/user-attachments/assets/2616d9a5-8275-4651-abe4-af6fdd406c93" />


     


   
