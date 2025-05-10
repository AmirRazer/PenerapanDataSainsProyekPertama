import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Muat model SVM yang sudah disimpan
model = joblib.load('svm_model.pkl')  # Ganti dengan lokasi model yang sesuai

# Nilai unik dari kolom yang digunakan untuk input
business_travel = ['Travel_Frequently', 'Travel_Rarely', 'Non-Travel']
department = ['Human Resources', 'Research & Development', 'Sales']
education_field = ['Other', 'Medical', 'Life Sciences', 'Marketing', 'Technical Degree', 'Human Resources']
gender = ['Male', 'Female']
job_role = ['Human Resources', 'Healthcare Representative', 'Research Scientist', 'Sales Executive', 'Manager', 
            'Laboratory Technician', 'Research Director', 'Manufacturing Director', 'Sales Representative']

# Range nilai untuk Age dan DistanceFromHome
age_min = 18
age_max = 60
distance_from_home_min = 1
distance_from_home_max = 29

# Judul aplikasi Streamlit
st.title("Prediksi Attrition Karyawan")

# Input untuk setiap fitur
business_travel_input = st.selectbox("Pilih Business Travel", business_travel)
department_input = st.selectbox("Pilih Department", department)
education_field_input = st.selectbox("Pilih Education Field", education_field)
gender_input = st.selectbox("Pilih Gender", gender)
job_role_input = st.selectbox("Pilih Job Role", job_role)

age_input = st.slider("Pilih Umur", min_value=age_min, max_value=age_max, value=30)
distance_from_home_input = st.slider("Pilih Jarak dari Rumah", min_value=distance_from_home_min, max_value=distance_from_home_max, value=10)
monthly_income_input = st.slider("Pilih Monthly Income", min_value=1009, max_value=19999, value=6502)

# Saat tombol prediksi ditekan
if st.button("Prediksi"):
    # Membuat dataframe untuk input
    input_data = pd.DataFrame({
        'BusinessTravel': [business_travel_input],
        'Department': [department_input],
        'EducationField': [education_field_input],
        'Gender': [gender_input],
        'JobRole': [job_role_input],
        'Age': [age_input],
        'DistanceFromHome': [distance_from_home_input],
        'MonthlyIncome': [monthly_income_input]
    })

    # Lakukan one-hot encoding pada data input
    input_data_encoded = pd.get_dummies(input_data, columns=[
        'BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole'
    ])
    
    # Mendapatkan feature names dari model
    model_features = model.feature_names_in_
    
    # Membuat DataFrame dengan kolom yang sama seperti saat training
    final_input = pd.DataFrame(columns=model_features)
    
    # Mengisi nilai yang ada di input_data_encoded
    for col in input_data_encoded.columns:
        if col in model_features:
            final_input[col] = input_data_encoded[col]
    
    # Mengisi nilai 0 untuk kolom yang tidak ada di input_data_encoded
    final_input = final_input.fillna(0)

    # Melakukan prediksi
    prediction = model.predict(final_input)

    # Tampilkan hasil prediksi
    if prediction[0] == 1:
        st.write("Karyawan Diprediksi Mengundurkan Diri (Attrition)")
    else:
        st.write("Karyawan Diprediksi Tidak Mengundurkan Diri (No Attrition)")