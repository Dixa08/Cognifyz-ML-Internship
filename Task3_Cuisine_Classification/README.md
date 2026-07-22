# 🍽 Restaurant Cuisine Classification using Machine Learning

![Banner](assets/images/banner.png)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
## 📌 Project Overview

This project was developed as part of the **Machine Learning Internship at Cognifyz Technologies**.

The objective of this project is to build a machine learning classification model that predicts the **primary cuisine** of a restaurant using its characteristics, such as location, pricing, customer engagement, and service-related features.

The project follows a complete machine learning workflow, including data preprocessing, feature engineering, model training, performance evaluation, and feature importance analysis. A **Random Forest Classifier** was used to classify restaurants into different cuisine categories based on the available dataset.

---

# 🎯 Objective

The primary objectives of this project are:

- Develop a machine learning model for restaurant cuisine classification.
- Clean and preprocess the restaurant dataset.
- Handle missing values and prepare the target variable.
- Convert categorical variables into numerical form.
- Train a classification model using Random Forest.
- Evaluate the model using Accuracy, Precision, Recall, and F1-Score.
- Analyze the most important features influencing cuisine prediction.

---

# 📂 Dataset

The dataset contains information about restaurants from multiple cities and countries.

### Dataset Summary

| Attribute | Value |
|-----------|--------|
| Total Records | 9551 |
| Total Features | 21 |
| Target Variable | Primary Cuisine |

### Important Features Used

- Country Code
- City
- Average Cost for Two
- Currency
- Has Table Booking
- Has Online Delivery
- Is Delivering Now
- Price Range
- Votes

![Dataset](assets/images/dataset.png)

---

# 🧹 Data Cleaning & Preprocessing

The following preprocessing steps were performed before training the model:

- Missing values in the **Cuisines** column were replaced with **"Unknown"**.
- Duplicate records were checked and removed where necessary.
- Since many restaurants belonged to multiple cuisines, only the **first cuisine** was selected as the **Primary Cuisine** for classification.
- Categorical variables were encoded using **LabelEncoder**.
- Rare cuisine categories with very few samples were removed to improve model stability.
- The dataset was split into **80% training** and **20% testing** data.

![Missing Values](assets/images/missing_values.png)

---

# 🔄 Primary Cuisine Selection

Many restaurants in the dataset were associated with multiple cuisines (e.g., *North Indian, Chinese*). Since the project focuses on **single-label classification**, the first listed cuisine was selected as the target variable.

**Example**

| Original Cuisine | Primary Cuisine |
|------------------|-----------------|
| North Indian, Chinese | North Indian |
| Italian, Pizza | Italian |
| Cafe, Desserts | Cafe |

This preprocessing step simplified the classification problem while preserving the dominant cuisine category for each restaurant.

![Primary Cuisine](assets/images/primary_cuisine.png)

---

# ⚙️ Project Workflow

The project follows the complete machine learning pipeline shown below.

![Workflow](assets/images/workflow.png)

### Workflow Steps

1. Dataset Loading
2. Data Cleaning
3. Missing Value Handling
4. Primary Cuisine Selection
5. Feature Selection
6. Label Encoding
7. Train-Test Split
8. Random Forest Classifier Training
9. Model Evaluation
10. Feature Importance Analysis

---

# 🤖 Machine Learning Model

A **Random Forest Classifier** was selected for this project because it performs well on datasets containing both numerical and categorical features.

### Why Random Forest?

- Handles complex and non-linear relationships.
- Reduces overfitting through ensemble learning.
- Provides feature importance analysis.
- Produces reliable classification performance.

---

# 📊 Model Performance

The trained model was evaluated using multiple classification metrics.

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score

The Random Forest Classifier demonstrated strong performance in predicting the primary cuisine category.

![Performance](assets/images/performance.png)

---

# 📈 Feature Importance

Feature importance analysis was performed to determine which restaurant attributes contributed the most to cuisine prediction.

The model identified features such as customer votes, price range, average cost, and city as key factors influencing the classification process.

![Feature Importance](assets/images/feature_importance.png)

---

# 📉 Confusion Matrix

The Confusion Matrix provides a visual representation of the model's classification performance across different cuisine categories.

It highlights correctly classified cuisines as well as areas where the model experienced confusion between similar cuisine types.

![Confusion Matrix](assets/images/confusion_matrix.png)

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# 📁 Project Structure

```text
Task3_Cuisine_Classification/
│
├── assets/
│   └── images/
├── data/
├── models/
├── notebooks/
├── reports/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 Future Scope

The project can be further enhanced by:

- Applying Hyperparameter Tuning.
- Using Cross Validation for improved evaluation.
- Experimenting with XGBoost, LightGBM, and CatBoost classifiers.
- Building a Multi-Label Cuisine Classification model.
- Deploying the model as an interactive web application.
- Integrating the classifier with a restaurant recommendation system.

---

# 📚 References

- Scikit-learn Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Seaborn Documentation

---

# 👩‍💻 Author

**Dixa**

**B.Tech Computer Science Engineering (Artificial Intelligence & Machine Learning)**

**Graphic Era Hill University**

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
