# 🍽 Restaurant Rating Prediction

## 📌 Project Overview

This project was developed as part of the **Machine Learning Internship at Cognifyz Technologies**.

The objective of this project is to build a Machine Learning model that predicts the **Aggregate Rating** of a restaurant based on different restaurant features such as cuisine, city, average cost, price range, online delivery, table booking, and customer votes.

---

## 🎯 Objective

- Predict restaurant ratings using Machine Learning.
- Compare different regression algorithms.
- Analyze the factors that influence restaurant ratings.
- Evaluate model performance using standard regression metrics.

---

## 📂 Dataset

The dataset contains information about **9,551 restaurants** with **21 features**, including:

- Restaurant Name
- City
- Cuisine
- Average Cost for Two
- Currency
- Table Booking
- Online Delivery
- Price Range
- Votes
- Aggregate Rating

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Project Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Encoding
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Feature Importance Analysis
10. Model Saving

---

## 🤖 Machine Learning Models

The following regression models were implemented:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 📈 Model Performance

| Model | R² Score | RMSE |
|--------|---------:|-----:|
| Linear Regression | 0.303 | 1.259 |
| Decision Tree | 0.923 | 0.420 |
| **Random Forest** | **0.962** | **0.296** |

### Best Model

**Random Forest Regressor**

The Random Forest model achieved the highest accuracy and was selected as the final prediction model.

---

## 🔍 Feature Importance

The most influential features affecting restaurant ratings are:

1. Votes
2. Longitude
3. Latitude
4. Cuisines
5. Average Cost for Two

---

## 📁 Project Structure

```text
Task1_Restaurant_Rating_Prediction/
│
├── data/
├── models/
├── notebooks/
├── reports/
├── src/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run

### Clone the repository

```bash
git clone <repository_link>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Hyperparameter tuning
- One-Hot Encoding for categorical features
- Cross-validation
- Advanced ensemble models
- Interactive dashboard enhancements

---

## 👩‍💻 Author

**Dixa**

B.Tech CSE (AI & ML)

