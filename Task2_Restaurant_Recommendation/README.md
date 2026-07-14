<p align="center">
<img src="assets/images/banner.png" width="100%">
</p>

# 🍽 Restaurant Recommendation System
## AI Powered Recommendation Engine

> A Content-Based Restaurant Recommendation System using Machine Learning
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Project Overview

Finding restaurants that match a user's preferences can be difficult when thousands of options are available. This project develops a **Content-Based Recommendation System** that suggests restaurants based on user preferences such as **Cuisine**, **City**, and **Price Range**.

Instead of predicting ratings, this system recommends restaurants with similar characteristics using **CountVectorizer** and **Cosine Similarity**.

---

## 🎯 Objective

The objective of this project is to build a restaurant recommendation system capable of suggesting restaurants according to user preferences.

The recommendation system uses restaurant attributes including:

- 🍜 Cuisine
- 📍 City
- 💰 Price Range

to recommend similar restaurants.

---

## 📂 Dataset Information

| Attribute | Value |
|-----------|--------|
| Total Restaurants | 9551 |
| Total Features | 21 |
| Missing Cuisine Values | 9 |
| Duplicate Records | 0 |

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- CountVectorizer
- Cosine Similarity
- Streamlit (Future Deployment)

---

## 🧠 Recommendation Technique

This project implements a **Content-Based Filtering** recommendation system.

### Workflow

```text
Restaurant Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Selection
        │
        ▼
Combined Features
        │
        ▼
CountVectorizer
        │
        ▼
Cosine Similarity
        │
        ▼
Top Restaurant Recommendations
```

---

## 📊 Project Workflow

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Feature Selection
5. Create Combined Features
6. Text Vectorization
7. Cosine Similarity
8. Restaurant Recommendation
9. Recommendation Evaluation

---

## 📷 Sample Recommendation

Example User Preferences

| Feature | Value |
|---------|-------|
| City | New Delhi |
| Cuisine | North Indian |
| Price Range | 3 |

Recommended Restaurants

| Restaurant | Rating |
|------------|--------|
| Kopper Kadai | ⭐ 4.8 |
| Zabardast Indian Kitchen | ⭐ 4.7 |
| Band Baaja Baaraat | ⭐ 4.6 |
| Pind Balluchi | ⭐ 4.6 |
| The GT Road | ⭐ 4.5 |

---

## 📈 Recommendation Evaluation

The recommendation system was tested using multiple combinations of:

- Cuisine
- City
- Price Range

The generated recommendations matched user preferences successfully, demonstrating the effectiveness of the Content-Based Filtering approach.

---

## 📂 Project Structure

```text
Task2_Restaurant_Recommendation
│
├── data/
├── notebooks/
├── reports/
├── src/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- TF-IDF Vectorizer
- Deep Learning Recommendation Models
- Streamlit Deployment
- Restaurant Image Recommendation

---

## 👩‍💻 Author

**Dixa**

B.Tech CSE (AI & ML)
Machine Learning Intern @ Cognifyz Technologies
