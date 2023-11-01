import streamlit as st
import numpy as np
from keras.models import load_model

def load_knn_model(model_path):
        try:
            model = load_model(model_path)
            return model
        except Exception as e:
            st.write("Error loading the model:", str(e))
            return None

def predict(model, article_title):
        if model is None:
            return None

        try:
            
            prediction = model.predict(article_title)
        
            
            return prediction
        except Exception as e:
            st.write("Error predicting:", str(e))
            return None



st.markdown("# Fake Article Title Predction")
st.markdown("----")

model_path = "knn_deplaoyment\knn_model.pkl"
if 'model' not in st.session_state:
        st.session_state.model = load_knn_model(model_path)

st.subheader("Enter some Article Title")
article_title = st.text_input("")


if st.button("Predict"):
    prediction = predict(st.session_state.model, article_title)
    if prediction==0:
        st.write("Fake Article Title")
    else:
        st.write("Article Title is Accurate")
