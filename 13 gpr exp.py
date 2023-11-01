##Experiment 13a

import streamlit as st
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
import pickle as pk

def load_gpr_model(model_path):
    try:
        with open(model_path, "rb") as file:
            model = pk.load(file)
        return model
    except Exception as e:
        st.write("Error loading the model:", str(e))
        return None

st.markdown("# Student Performance")
st.markdown("----")

st.title("Student Performance Prediction")

model_path = r"C:\Users\vaibh\OneDrive\Desktop\PDS\gpr_model/model.pkl"
gpr_model = load_gpr_model(model_path)

if gpr_model is not None:
    hours = st.number_input("Enter study hours: ")
    previous_scores = st.number_input("Enter previous score: ")
    sleep_hours = st.number_input("Enter sleep hours: ")
    practice = st.number_input("Enter number of sample questions practiced: ")
    ext_act = st.number_input("Any external activities (0 for no, 1 for yes): ")

    if st.button("Predict"):
        # You should format the input data as a numpy array before making predictions
        input_data = np.array([[hours, previous_scores, sleep_hours, practice, ext_act]])
        prediction, _ = gpr_model.predict(input_data, return_std=True)

        st.write(f"Predicted Performance Index: {prediction[0]:.2f}")
else:
    st.write("Model failed to load. Please check the model file path.")