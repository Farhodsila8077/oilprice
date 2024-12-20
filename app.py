import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model = joblib.load("oilmodel.pkl")

# Foydalanuvchi interfeysi
st.title("Neft narxini bashorat qilish ilovasi")
st.write("Neft parametrlarini kiriting:")

# Parametrlarni foydalanuvchidan olish
open_price = st.number_input("Ochilgan narx (Open)", value=70.0)
high_price = st.number_input("Eng yuqori narx (High)", value=75.0)
low_price = st.number_input("Eng past narx (Low)", value=65.0)
volume = st.number_input("Hajm (Volume)", value=50000)

# Bashorat qilish uchun tayyorlash
if st.button("Bashorat qiling"):
    input_data = pd.DataFrame({
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Volume': [volume]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Bashorat qilingan neft narxi : ${prediction:.2f}")
