import streamlit as st
import pandas as pd
import pickle
import os

# Get the absolute path to the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Load the Random Forest model
model_path = os.path.join(current_script_directory, 'random_forest_model.pkl')
with open(model_path, 'rb') as model_file:
    random_forest_model = pickle.load(model_file)

# Streamlit App
st.title("Anemia Prediction ")
# Input features from the user
st.sidebar.title("Input Features")  # Sidebar title

# Add textboxes for features
gender = st.sidebar.selectbox("Select Gender", ["Male", "Female"])  # Use selectbox for categorical choice
hemoglobin = st.sidebar.text_input("Enter Hemoglobin", 10.0)  # Textbox for Hemoglobin
mch = st.sidebar.text_input("Enter MCH", 30.0)  # Textbox for MCH
mchc = st.sidebar.text_input("Enter MCHC", 35.0)  # Textbox for MCHC
mcv = st.sidebar.text_input("Enter MCV", 80.0)  # Textbox for MCV

# Convert input values to appropriate data types
gender = 1 if gender == "Male" else 0
hemoglobin = float(hemoglobin)
mch = float(mch)
mchc = float(mchc)
mcv = float(mcv)

# Create a DataFrame with user input
user_input = pd.DataFrame({
    'Gender': [gender],
    'Hemoglobin': [hemoglobin],
    'MCH': [mch],
    'MCHC': [mchc],
    'MCV': [mcv]
})

# Make predictions
prediction = random_forest_model.predict(user_input)

st.subheader("Prediction:")

# Apply different colors and font sizes based on prediction
if prediction[0] == 1:
    st.markdown("<p style='color: red; font-size: 20px;'>High Risk of Anemia</p>", unsafe_allow_html=True)
    # Display a resized image from the internet for high risk
    st.image("https://th.bing.com/th/id/OIP.35t8iXfgpUn2WigZL7tkYAHaEy?rs=1&pid=ImgDetMain", width=600)

else:
    st.markdown("<p style='color: green; font-size: 20px;'>Low Risk of Anemia</p>", unsafe_allow_html=True)
    # Display a resized image from the internet for low risk
    st.image("https://www.tfp.mu/image/catalog/2020/Blog/July/What%20is%20good%20health/2.png", width=600)