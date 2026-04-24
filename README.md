<div align="center">
💻 Laptop Price Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
Predict laptop prices in Euros and INR instantly based on hardware specifications — powered by a Random Forest ML model.
</div>
---
📌 Overview
Laptop Price Predictor is an end-to-end machine learning project that estimates the market price of a laptop based on its technical specifications. It includes data preprocessing, feature engineering, model training, and a fully interactive web application built with Streamlit.
> 🎯 **Goal:** Help users and buyers estimate fair laptop prices before purchasing, based on real-world data.
---
✨ Key Features
🔍 Predicts price based on RAM, SSD, HDD, Display PPI, Weight, and Brand
💱 Real-time Euro → INR conversion using a user-defined exchange rate
🌐 Interactive and responsive Streamlit web UI
🤖 Trained on 1300+ real laptop listings using Random Forest Regression
📦 Fully serialized model ready for deployment
---
🗂️ Project Structure
```
Laptop-Price-Predictor/
│
├── 📓 Laptop_price.ipynb          # EDA, feature engineering & model training
├── 🚀 app3.py                     # Streamlit web application
├── 🧠 laptop_price_model.pkl      # Trained Random Forest model
├── 📋 columns.pkl                 # Saved feature column names
├── 📊 laptop_price.xls            # Raw dataset
├── 📊 laptop_price.xlsx           # Raw dataset (Excel format)
└── 📄 requirements.txt            # Python dependencies
```
---
📊 Dataset
The model is trained on a dataset of 1,300+ laptop listings with the following features:
Feature	Description
`Company`	Laptop brand (Dell, HP, Apple, Lenovo, etc.)
`TypeName`	Category — Ultrabook, Gaming, Notebook, etc.
`Inches`	Screen size in inches
`ScreenResolution`	Display resolution
`Cpu`	Processor name and specs
`Ram`	RAM capacity in GB
`Memory`	Storage configuration (SSD / HDD)
`Gpu`	Graphics card details
`OpSys`	Operating system
`Weight`	Device weight in kg
`Price_euros`	⭐ Target variable — laptop price in Euros
---
⚙️ Feature Engineering
Raw data was cleaned and transformed through the following steps:
Step	Transformation
RAM & Weight	Stripped string units (`GB`, `kg`), cast to numeric
Memory	Extracted SSD and HDD sizes in GB via regex parsing
CPU / GPU	Isolated brand and type from full specification strings
Screen Resolution	Parsed X and Y pixel values from resolution string
PPI	Computed as `√(X² + Y²) / screen_inches`
Encoding	One-hot encoding applied to all categorical variables
Column Cleanup	Dropped `laptop_ID`, `Product`, `Cpu`, `Gpu`, `ScreenResolution`, `Inches`
---
🤖 Model Development
Three models were trained iteratively with increasing complexity:
#	Model	Config	Notes
1	Decision Tree Regressor	`max_depth=10`	Baseline
2	Random Forest Regressor	`n_estimators=100`, `max_depth=15`	Improved accuracy
3	Random Forest Regressor	`n_estimators=200`, `max_depth=20`	✅ Final Model
Final Model Configuration:
```python
RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    random_state=42
)
```
Evaluation Metric: R² Score on 20% test split
---
🖥️ Web Application
The Streamlit app provides a clean interface for real-time price prediction:
Input Parameter	Type	Range / Options
🏢 Company	Dropdown	Dell, HP, Lenovo, Asus, Acer, Apple
💾 RAM	Slider	2 GB – 32 GB
⚡ SSD Size	Slider	0 GB – 1024 GB
🗄️ HDD Size	Slider	0 GB – 2048 GB
🖥️ PPI	Slider	90 – 400
⚖️ Weight	Slider	1.0 kg – 3.5 kg
💱 Exchange Rate	Input	Euro → INR (user-defined)
Output: Predicted price displayed in both € Euros and ₹ INR
---
🚀 Getting Started
Prerequisites
Ensure you have Python 3.8+ installed, then install the required packages:
```bash
pip install -r requirements.txt
```
Or install manually:
```bash
pip install streamlit scikit-learn numpy pandas openpyxl
```
Run the Application
```bash
streamlit run app3.py
```
> ⚠️ **Important:** `laptop_price_model.pkl` and `columns.pkl` must be in the **same directory** as `app3.py`.
---
🛠️ Tech Stack
Technology	Purpose
Python 3	Core programming language
Pandas	Data loading and manipulation
NumPy	Numerical computations
scikit-learn	ML model training & evaluation
Streamlit	Interactive web application
Pickle	Model serialization
Jupyter Notebook	Exploratory analysis & prototyping
---
👩‍💻 Author
Bhumika Madhwani
GitHub: @madhwanibhumika24
---
<div align="center">
⭐ If you found this project useful, consider giving it a star! ⭐
</div>
