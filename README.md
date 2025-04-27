# Corolla Price Predictor 🚗💰

This project predicts the market value of **Toyota Corolla** cars using machine learning models. The goal is to assist **ACB Auctions** and car dealerships in estimating vehicle prices quickly during live auctions. It includes **data preprocessing**, **EDA**, **model training**, **hyperparameter tuning**, and **deployment via Streamlit**.

---

## 🌐 Live App

👉 [Check out the deployed Streamlit app here!](https://corolla-price-predictor-qdxuxvge9wve5bbpbyp4tf.streamlit.app/)

Enter vehicle features like **age**, **mileage**, and **fuel type** to get an **instant price prediction**.

---

## 📈 Business Use Case

At live car auctions, making quick, data-driven pricing decisions is crucial. This app helps dealerships and auctions like **ACB Auctions** assess used Toyota Corolla values in real time, improving **bidding strategies** and **profit margins**.

---

## 🚀 What We Did

1. **Exploratory Data Analysis (EDA):**
   - Analyzed the distribution of car prices.
   - Explored relationships between features like **car age, mileage, horsepower, fuel type, etc.** and price.
   - Used scatterplots, boxplots, and correlation heatmaps for insights.

2. **Data Preprocessing:**
   - **Removed irrelevant columns** (`Id`) and **constant columns** (`Cylinders`).
   - **Imputed missing values**:
     - Categorical (`Color`) → Mode.
     - Numerical (`CC`, `Mfr_Guarantee`, `Airco`) → Median.
   - **Dropped `Mistlamps`** due to excessive missing values (~72%).
   - **Encoded categorical variables** (`Fuel_Type`, `Color`) using One-Hot Encoding.
   - **Scaled numerical features** (e.g., `Age_08_22`, `KM`, `HP`, `CC`, `Doors`, `Gears`) for models sensitive to feature magnitude.

3. **Machine Learning Models Trained:**
   - **Linear Regression** (baseline).
   - **K-Nearest Neighbors (KNN) Regressor**.
   - **Random Forest Regressor**.

4. **Model Evaluation (Default Hyperparameters):**

| Model                   | Train R² | Test R² | Test MAE   | Test MSE       |
|-------------------------|----------|---------|------------|----------------|
| Linear Regression       | 0.8621   | 0.8600  | \$961.38   | 1,770,089.00   |
| KNN (Default)           | 0.9139   | 0.8738  | \$954.45   | 1,595,057.00   |
| Random Forest (Default) | 0.9864   | 0.9092  | \$784.47   | 1,147,725.00   |

5. **Hyperparameter Tuning:**
   - **KNN**: Tuned `n_neighbors` (optimal = 7).
   - **Random Forest**: Tuned `n_estimators` (optimal = 200).

| Model                 | Train R² | Test R² | Test MAE   | Test MSE       |
|-----------------------|----------|---------|------------|----------------|
| KNN (Tuned `n=7`)     | 0.9011   | 0.8734  | \$941.29   | 1,600,300.00   |
| Random Forest (Tuned) | 0.9866   | 0.9107  | \$781.74   | 1,129,643.00   |

6. **Best Model Recommendation:**
   - **Random Forest Regressor (Tuned)** achieved the best performance (**R²: 91.1%**) on the test set with the lowest MAE and MSE.
   - Recommended for **ACB Auctions** for further use.

7. **Deployment:**
   - The best model was deployed via **Streamlit**.
   - Users can input car features (age, mileage, fuel type, etc.) to get **instant price predictions**.

---


