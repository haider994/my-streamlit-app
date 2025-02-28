import streamlit as st
import math

# واجهة التطبيق
st.title("Calculate Safe Distance for Hydro-Test")
st.image("logo.png", width=150)  # تأكد من وجود الشعار بنفس المجلد

# إدخال البيانات
P = st.number_input("Pressor Test (Bar):", min_value=0.1, value=10.0)
D = st.number_input("Outter diameter:", min_value=0.1, value=100.0)
unit = st.radio("Unit:", [" (mm)", " (inch)"])
t = st.number_input("Pipe thickness (mm):", min_value=0.1, value=5.0)
risk_factor = st.selectbox("Safe Factor:", [1.5, 2.0, 2.5])

# تحويل القطر إذا كان بالإنش
if unit == " (inch)":
    D *= 25.4

# حساب المسافة الآمنة
if st.button("Calculate the safe distance"):
    if P > 0 and D > 0 and t > 0:
        d_safe = risk_factor * math.sqrt((P * D) / t)
        st.success(f"Safe distance: {round(d_safe, 2)} M")
    else:
        st.error("يرجى إدخال أرقام صحيحة فقط please enter a right num only!")

# توقيع
st.markdown('<p style="text-align:center; color:gray; font-size:12px;">by Haider Hashim</p>', unsafe_allow_html=True)
