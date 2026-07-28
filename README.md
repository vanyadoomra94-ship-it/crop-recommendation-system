# 🌱 Crop Recommendation System

A Machine Learning-based Crop Recommendation System that recommends the most suitable crop based on soil and environmental conditions.

## 📌 Project Overview

This project uses machine learning classification algorithms to recommend a crop based on seven input features:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

The project compares multiple machine learning algorithms and uses **GridSearchCV** to tune the best-performing model.

## 🎯 Objective

The objective of this project is to develop a machine learning model that can recommend a suitable crop based on given soil and environmental conditions.

## 📊 Dataset

* **Rows:** 2200
* **Features:** 7
* **Target:** Crop label
* **Number of crop classes:** 22
* **Problem Type:** Multiclass Classification

### Features

| Feature     | Description        |
| ----------- | ------------------ |
| N           | Nitrogen content   |
| P           | Phosphorus content |
| K           | Potassium content  |
| Temperature | Temperature in °C  |
| Humidity    | Relative humidity  |
| pH          | Soil pH            |
| Rainfall    | Rainfall in mm     |

## 🔍 Exploratory Data Analysis

The dataset was analyzed to understand:

* Data distribution
* Missing values
* Duplicate records
* Feature relationships
* Correlations between variables
* Class distribution

The dataset contains **22 crop classes** and the classes are balanced.

## 🤖 Machine Learning Models

The following classification algorithms were evaluated:

| Model                   | Test Accuracy |
| ----------------------- | ------------: |
| Logistic Regression     |           96% |
| Decision Tree           |           98% |
| Random Forest           |           99% |
| K-Nearest Neighbors     |           95% |
| Support Vector Machine  |           96% |
| **Tuned Random Forest** |     **99.3%** |

## 🏆 Best Model

The final model is a **Random Forest Classifier** optimized using **GridSearchCV**.

### Best Parameters

```text
n_estimators = 100
max_depth = None
min_samples_split = 2
```

### Performance

* Cross-validation accuracy: **99.49%**
* Test accuracy: **99.3%**

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 📁 Project Structure

```text
crop-recommendation-system/
│
├── Crop_Recommendation.ipynb
├── Crop_recommendation.csv
├── crop_recommendation_model.pkl
├── app.py
└── README.md
```

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd crop-recommendation-system
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🌐 Streamlit Application

The application provides an interactive interface where users can enter:

* Nitrogen
* Phosphorus
* Potassium
* Temperature
* Humidity
* pH
* Rainfall

The trained Random Forest model then predicts the recommended crop.

## 🔮 Future Improvements

* Add more soil and environmental parameters
* Improve the user interface
* Add crop information and cultivation tips
* Deploy the application publicly
* Add model explainability
* Test the model on real-world agricultural data

## 👩‍💻 Author

**Vanya Doomra**

This project was developed as part of my Machine Learning learning journey.
