# 🏡 House Price Prediction Using XGBoost

## 📌 Overview
This project aims to predict house prices based on various features such as location, number of rooms, square footage, and other factors. The **XGBoost** algorithm is used due to its efficiency and accuracy in handling structured data.

---

## 📊 Project Workflow:

### 1️⃣ Data Collection
- The dataset is typically obtained from sources like:
  - Kaggle (`house-prices-advanced-regression-techniques` dataset)
  - Real estate APIs
  - CSV files with historical house prices

### 2️⃣ Data Preprocessing
- Handling missing values using:
  - Mean/median/mode imputation
  - Dropping irrelevant columns
- Encoding categorical variables using **Label Encoding** or **One-Hot Encoding**.
- Normalizing numerical values for better model performance.

### 3️⃣ Feature Engineering
- Important features affecting house prices:
  - `LotArea`: Size of the property in square feet
  - `OverallQual`: Overall material and finish quality
  - `YearBuilt`: Year the house was built
  - `GrLivArea`: Above-ground living area in square feet
  - `TotalBsmtSF`: Total basement area in square feet

### 4️⃣ Model Training (Using XGBoost)
- **XGBoost (Extreme Gradient Boosting)** is chosen for its speed and accuracy.
- Model training example:
  ```python
  from xgboost import XGBRegressor
  
  model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
  model.fit(X_train, y_train)
  ```
- Hyperparameter tuning using **GridSearchCV** or **RandomizedSearchCV**.

### 5️⃣ Model Evaluation
- Performance metrics used:
  - **Mean Absolute Error (MAE)**
  - **Root Mean Squared Error (RMSE)**
  - **R² Score**
- Example evaluation code:
  ```python
  from sklearn.metrics import mean_absolute_error, r2_score
  
  y_pred = model.predict(X_test)
  print("MAE:", mean_absolute_error(y_test, y_pred))
  print("R² Score:", r2_score(y_test, y_pred))
  ```

### 6️⃣ Model Deployment (Using Streamlit)
- A **Streamlit** app allows users to input house details and get a price prediction.
- Example Streamlit code:
  ```python
  import streamlit as st
  
  st.title("🏡 House Price Prediction")
  area = st.number_input("Enter House Area (sq ft)")
  quality = st.slider("Select House Quality", 1, 10)
  
  if st.button("Predict Price"):
      price = model.predict([[area, quality]])
      st.success(f"Estimated Price: ${price[0]:,.2f}")
  ```
- Deployment options: **Streamlit Cloud**, **Heroku**.

---

## 🚀 Final Output
✅ A trained XGBoost model that accurately predicts house prices  
✅ A user-friendly **Streamlit web app** for real-time predictions  

---

## 📌 Future Improvements
- Use **LSTM/Deep Learning** for time-series forecasting of house prices.
- Include **real-time market trends** from Zillow API.
- Optimize model hyperparameters for better accuracy.


## Output:
1.![Output Image 1](image\img1.png)
2.![Output Image 2](image\img2.png)
---

