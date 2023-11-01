import streamlit as st
import pickle
from tensorflow.keras.models import load_model
import base64

# Load the trained model (replace 'model.pkl' with the actual model file)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    backdrop-filter: blur(1000px);
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def predict(water_inlet_1, water_inlet_2):
    # Placeholder for actual prediction logic
    # You may replace the comparison logic based on your requirements
    flag = 0 or 1
    return water_inlet_1 + water_inlet_2 

def main():
    set_background(r'C:\Users\Suyash Tambe\Desktop\PDS\linus-nylund-Q5QspluNZmM-unsplash.jpg')
    
    
    # Title and description
    st.markdown("<p style='text-align: center; color: black; font-size: 58px; font-family: \'Times New Roman\', Times, serif;'>Water Inlet Prediction</p>", unsafe_allow_html=True)
    st.markdown('<p style="font-family: \'Times New Roman\', Times, serif; color: black; font-weight: bold; font-size: 24px; text-align: center;">This app predicts water inlet values based on a trained model.</p>', unsafe_allow_html=True)

    # Main content
    st.subheader("Enter Water Inlet Values:")
    water_inlet_1 = st.number_input("Water Inlet 1", min_value=0.0, max_value=5000.0, step=1.0)
    water_inlet_2 = st.number_input("Water Inlet 2", min_value=0.0, max_value=5000.0, step=1.0)

    # Add a "Predict" button with style
    if st.button("Predict", key="predict_button"):
        prediction = predict(water_inlet_1, water_inlet_2)

        # Display the prediction with a nice card-style layout
        st.subheader("Prediction:")
        st.info(f"The predicted output based on Water Inlet 1 ({water_inlet_1}), Water Inlet 2 ({water_inlet_2}) is: {prediction}")

if __name__ == "__main__":
    main()
