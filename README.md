# Laptop Price Predictor

A Machine Learning Web Application for Predicting Laptop Prices

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)

---

## 🔗 Live Demo

👉 https://laptop-price--predictor.streamlit.app/

---

## Overview

The **Laptop Price Predictor** is an end-to-end machine learning project designed to estimate the market price of laptops based on their technical specifications. The project covers the complete pipeline, including data preprocessing, feature engineering, model training, and deployment using a Streamlit-based web application.

**Objective:**
To help users estimate fair laptop prices based on real-world data before making informed purchasing decisions.

---

## Key Features

* Predicts laptop prices using specifications such as RAM, storage, display PPI, weight, and brand
* Real-time Euro to INR conversion based on a user-defined exchange rate
* Interactive and user-friendly web interface built with Streamlit
* Trained on 1300+ real-world laptop records
* Ready-to-use serialized machine learning model for deployment

---

## Project Structure

```
Laptop-Price-Predictor/
│
├── Laptop_price.ipynb       # Data analysis and model training
├── app3.py                  # Streamlit application
├── laptop_price_model.pkl   # Trained model
├── columns.pkl              # Feature columns
├── laptop_price.xlsx        # Dataset
└── requirements.txt         # Dependencies
```

---

## Dataset

The dataset contains over 1,300 laptop records with the following attributes:

* Company (Brand)
* TypeName (Category)
* Screen Size (Inches)
* Screen Resolution
* CPU Specifications
* RAM (GB)
* Storage (SSD/HDD)
* GPU Details
* Operating System
* Weight (kg)
* Price (Euros) – Target variable

---

## Feature Engineering

The dataset was preprocessed using the following steps:

* Converted RAM and weight into numerical values
* Extracted SSD and HDD sizes from storage data
* Parsed CPU and GPU information into meaningful categories
* Extracted resolution and calculated PPI (Pixels Per Inch)
* Applied one-hot encoding to categorical variables
* Removed irrelevant columns

---

## Model Development

Multiple models were evaluated, including Decision Tree and Random Forest.

### Final Model:

* **Random Forest Regressor**

  * `n_estimators = 200`
  * `max_depth = 20`
  * `random_state = 42`

**Evaluation Metric:**
R² Score using an 80-20 train-test split

---

## Web Application

The Streamlit application allows users to input laptop specifications and get instant price predictions.

### Inputs:

* Company
* RAM
* SSD Size
* HDD Size
* PPI
* Weight
* Exchange Rate

### Output:

* Predicted price in Euros (€)
* Converted price in Indian Rupees (₹)

---

## Getting Started

### Prerequisites

* Python 3.8 or above

### Installation

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app3.py
```

**Note:** Ensure that `laptop_price_model.pkl` and `columns.pkl` are present in the same directory as `app3.py`.


---

## Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Jupyter Notebook

---

## Author

**Bhumika Madhwani**
GitHub: https://github.com/madhwanibhumika24
<img width="712" height="792" alt="image" src="https://github.com/user-attachments/assets/5d3d38d6-8762-4108-b676-b76a1d80b63b" />
<img width="638" height="829" alt="image" src="https://github.com/user-attachments/assets/197be2a1-eccd-43af-8932-a1ea93a8c6a7" />

---


