import streamlit as st  # type: ignore
import pickle
import numpy as np
from PIL import Image

# Load the pre-trained model
pickle_in = open("C:\\Users\palay\\OneDrive\\Desktop\\corn\\cropRec\\crop_rec.pkl", "rb")
crop_Rec = pickle.load(pickle_in)

def welcome():
    return "Welcome"

def predict_note_authenticate(Nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall):
    pred = crop_Rec.predict([[Nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall]])
    print(pred)
    return pred

def main():
    st.title("Crop Recommendation")
    html_temp = """
    <div style="background-color:tomato; padding: 10px">
    <h2>Crop Recommendation</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Inputs
    Nitrogen = st.text_input("Nitrogen", "Type Here")
    phosphorous = st.text_input("Phosphorous", "Type Here")
    potassium = st.text_input("Potassium", "Type Here")
    temperature = st.text_input("Temperature", "Type Here")
    humidity = st.text_input("Humidity", "Type Here")
    ph = st.text_input("pH", "Type Here")
    rainfall = st.text_input("Rainfall", "Type Here")

    result = ""

    if st.button("Predict"):
        try:
            result = predict_note_authenticate(
                float(Nitrogen),
                float(phosphorous),
                float(potassium),
                float(temperature),
                float(humidity),
                float(ph),
                float(rainfall),
            )
            st.success(f'The recommended crop is {result}')
        except ValueError:
            st.error("Please enter valid numerical values!")

    if st.button("About"):
        st.text("Let's learn about crop recommendation!")

if __name__ == '__main__':
    main()
