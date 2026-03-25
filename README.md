# Safal Mess Demand Forecaster 

## Overview
The **Safal Mess Demand Forecaster**is an ml project made by me to solve the food wastage in mess in day to day life. .


## The Problem
College messes often prepare a fixed quantity of food. However, actual student demand fluctuates wildly based on factors like:
* **Menu Items:** (eg.biryani is consumed more while bhindi is consumed less but mess staff kepps making same amount of food everyday that leads to wastage of lot of food.)
* **Time of Year:** Demand drops during holidays or when students go home.
* **Exam time:** Demand dips slightly during exam weeks as students skip meals or eat lightly.
* **Weekends:** demand spikes as special meals are given on weekends like chole bature and birtani.

## Features
1.  **Data Generator (`generate_data.py`):** random dat has been generated here as i dont have the real data but it will work same for real data if provided.
2.  **Model Trainer (`train_model.py`):** trained on Linear Regressor and Random forest .
3.  **Interactive Predictor (`predict.py`):** here mess staff can enter the day and few other things like is exam going or not and other factors which will help them to predict how much quantity of food needs to be prepared.

## Tech Stack
* **Language:** Python
* **Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`

## Setup & Installation

*1. Clone the repository:*
   ```bash
   git clone [https://github.com/omkar-vitb/safal-mess-demand-forecaster.git]

*2. run the following command to install the required dependencies.*
pip install pandas numpy scikit-learn matplotlib

3. How to run
   first run  generate_data.py
   then run train_model.py
   then finally run predict.py

4. Here in predict.py one get to enter the date->Select meal:
  1) Breakfast  2) Lunch  3) High Tea  4) Dinner->Is it exam week? (y/n):->Is holiday nearby? (y/n): ->then a report like this will appear
=============================================
  Predicted Demand — Breakfast (Tuesday)
=============================================
  Item                    Predicted  Advice
  ------------------------------------------
  Poha                      902 units   OK
  Idli                       94 units   Make LESS
  Bread                     140 units   Make LESS
  Butter                    140 units   Make LESS
  Jam                       115 units   Make LESS
  Tea                       637 units   OK
  Coffee                    140 units   Make LESS
  Milk                      115 units   Make LESS
=============================================

   
