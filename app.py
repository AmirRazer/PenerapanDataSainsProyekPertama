import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Set page title and configure layout
st.set_page_config(
    page_title="Prediksi Attrition Karyawan",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application title with some styling
st.title("Prediksi Attrition Karyawan")
st.markdown("---")

# Load model
try:
    model = joblib.load('knn_model.pkl')
    st.success("Model berhasil dimuat!")
except Exception as e:
    st.error(f"Error saat memuat model: {str(e)}")
    st.stop()

# Sidebar for model information
with st.sidebar:
    st.subheader("Tentang Model")
    st.write("Model ini memprediksi apakah seorang karyawan berpotensi mengundurkan diri berdasarkan beberapa faktor.")
    st.write("Dibuat dengan algoritma K-Nearest Neighbors.")
    
    # Show model details if available
    try:
        if hasattr(model, 'n_neighbors'):
            st.write(f"Jumlah neighbors (k): {model.n_neighbors}")
        if hasattr(model, 'feature_names_in_'):
            st.write(f"Jumlah fitur: {len(model.feature_names_in_)}")
    except:
        pass

# Categorical feature values - maintain the exact order as in training
business_travel = ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'] 
department = ['Sales', 'Research & Development', 'Human Resources']
education_field = ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources', 'Other']
gender = ['Female', 'Male']
job_role = ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 
            'Manufacturing Director', 'Healthcare Representative', 'Manager',
            'Sales Representative', 'Research Director', 'Human Resources']

# Range values for numerical features
age_min, age_max = 18, 60
distance_from_home_min, distance_from_home_max = 1, 29
monthly_income_min, monthly_income_max = 1009, 19999

# Create two columns for input layout
col1, col2 = st.columns(2)

# Input section
with col1:
    st.subheader("Data Karyawan")
    business_travel_input = st.selectbox("Business Travel", business_travel)
    department_input = st.selectbox("Department", department)
    education_field_input = st.selectbox("Education Field", education_field)
    gender_input = st.selectbox("Gender", gender)
    job_role_input = st.selectbox("Job Role", job_role)

with col2:
    st.subheader("Informasi Tambahan")
    age_input = st.slider("Umur", min_value=age_min, max_value=age_max, value=30)
    distance_from_home_input = st.slider("Jarak dari Rumah (KM)", 
                                        min_value=distance_from_home_min, 
                                        max_value=distance_from_home_max, 
                                        value=10)
    monthly_income_input = st.slider("Penghasilan Bulanan", 
                                    min_value=monthly_income_min, 
                                    max_value=monthly_income_max, 
                                    value=6502)

# Add a divider before prediction section
st.markdown("---")

# Prediction button
predict_button = st.button("Prediksi Attrition", use_container_width=True)

# Replace the analysis section with this cleaner version
if predict_button:
    # Create input dataframe - hidden from user
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
    
    # Apply Label Encoding like in training (hidden from user)
    for col in input_data.columns:
        if input_data[col].dtype == 'object':
            le = LabelEncoder()
            if col == 'BusinessTravel':
                le.fit(business_travel)
            elif col == 'Department':
                le.fit(department)
            elif col == 'EducationField':
                le.fit(education_field)
            elif col == 'Gender':
                le.fit(gender)
            elif col == 'JobRole':
                le.fit(job_role)
            input_data[col] = le.transform(input_data[col])
    
    # Ensure features are in the correct order for model (hidden from user)
    try:
        model_features = model.feature_names_in_
        input_data = input_data[model_features]
    except:
        pass  # Silently handle if model doesn't have feature_names_in_
    
    # Make prediction with diagnostics
    try:
        prediction = model.predict(input_data)
        
        # Display final result with nicely formatted card
        st.markdown("## Hasil Prediksi")
        if prediction[0] == 1:
            st.error("⚠️ Karyawan Diprediksi **Mengundurkan Diri (Attrition)**")
            
            # Additional insights for attrition case
            st.markdown("### Faktor yang Mungkin Berpengaruh:")
            factors = []
            if distance_from_home_input > 15:
                factors.append("- Jarak dari rumah yang jauh (> 15 km)")
            if monthly_income_input < 5000:
                factors.append("- Penghasilan bulanan yang relatif rendah")
            if business_travel_input == 'Travel_Frequently':
                factors.append("- Frekuensi perjalanan bisnis yang tinggi")
                
            if factors:
                for f in factors:
                    st.markdown(f)
            else:
                st.markdown("- Kombinasi berbagai faktor dalam data")
                
        else:
            st.success("✅ Karyawan Diprediksi **Tidak Mengundurkan Diri (No Attrition)**")
            
            # Show retention factors
            st.markdown("### Faktor Positif:")
            positives = []
            if monthly_income_input > 10000:
                positives.append("- Penghasilan bulanan yang kompetitif")
            if distance_from_home_input < 10:
                positives.append("- Jarak rumah yang relatif dekat")
            if business_travel_input == 'Non-Travel':
                positives.append("- Tidak ada kebutuhan perjalanan bisnis")
                
            if positives:
                for p in positives:
                    st.markdown(p)
            else:
                st.markdown("- Kombinasi berbagai faktor dalam data")
        
    
                
    except Exception as e:
        st.error(f"Error saat memprediksi: {str(e)}")
        st.info("Pastikan format data input sesuai dengan data training model.")

# Footer
st.markdown("---")
st.caption("Aplikasi Prediksi Attrition Karyawan © 2025")