import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open(r'C:\Users\asus\Desktop\New folder\RandomForest.sav', 'rb'))

# Function for Prediction
def crop_prediction(input_data):
    # Use the loaded model to make a prediction
    prediction = loaded_model.predict(input_data)
    
    # Debugging print
    print(f"Prediction raw output: {prediction}")
    
    # Return the predicted crop name directly
    return prediction[0]

def main():
    # Title
    st.title('Crop Recommendation Web App')

    # Input data from user
    N = st.text_input('Level of Nitrogen')
    P = st.text_input('Level of Phosphorus')
    K = st.text_input('Level of Potassium')
    temperature = st.text_input('Temperature')
    humidity = st.text_input('Humidity')
    ph = st.text_input('pH value')
    rainfall = st.text_input('Rainfall')

    # Code for Prediction
    recommendation = ''
    
    # Prediction button
    if st.button('Recommend Crop'):
        # Convert input data to a numpy array
        try:
            input_data = np.array([[float(N), float(P), float(K), float(temperature), float(humidity), float(ph), float(rainfall)]])
            
            # Debugging print
            print(f"Input data: {input_data}")

            # Use the prediction function
            recommendation = crop_prediction(input_data)
            
            st.success(f'Recommended Crop: {recommendation}')
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")


main()