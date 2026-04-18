import streamlit as st
import pickle
import numpy as np

# -------------------- LOAD MODEL --------------------
model = pickle.load(open("laptop_price_model.pkl", "rb"))
cols = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻")

st.title("💻 Laptop Price Predictor")

# -------------------- INPUTS --------------------

company = st.selectbox("Company", ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple"])

cpu = st.selectbox(" CPU", [
    "Intel Core i3",
    "Intel Core i5",
    "Intel Core i7"
])

gpu = st.selectbox("GPU", [
    "Intel",
    "Nvidia",
    "AMD"
])

ram = st.slider(" RAM (GB)", 2, 32, 8)
ssd = st.slider("SSD (GB)", 0, 1024, 256)
hdd = st.slider(" HDD (GB)", 0, 2048, 0)
ppi = st.slider(" PPI", 90, 400, 150)
weight = st.slider(" Weight", 1.0, 3.5, 2.0)

rate = st.number_input(" Euro → INR Rate", value=90)

# -------------------- PREDICTION --------------------

if st.button("Predict Price"):

    input_data = np.zeros(len(cols))

    for i, col in enumerate(cols):

        # Numeric features
        if col == "Ram":
            input_data[i] = ram
        elif col == "SSD_size":
            input_data[i] = ssd
        elif col == "HDD_size":
            input_data[i] = hdd
        elif col == "PPI":
            input_data[i] = ppi
        elif col == "Weight":
            input_data[i] = weight

        # Company
        elif col == f"Company_{company}":
            input_data[i] = 1

        # CPU
        elif col == f"Cpu Type_{cpu}":
            input_data[i] = 1

        # GPU
        elif col == f"Gpu Brand_{gpu}":
            input_data[i] = 1

    prediction = model.predict([input_data])[0]

    price_inr = prediction * rate

    st.success(f"💰 Price: ₹ {round(price_inr, 2):,}")

    st.balloons()