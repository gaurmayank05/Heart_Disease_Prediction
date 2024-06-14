import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

# sidebar for navigation


with st.sidebar:
    selected = option_menu('',

                           [
                            'Heart Disease Prediction',
                            ],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    # Validation code for input fields
    def validate_input_fields(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
        errors = []

        # Validate Age
        if not age.isdigit() or int(age) <= 0 or int(age) > 150:
            errors.append("Age must be a positive integer between 1 and 150")

        # Validate Sex
        if sex not in ['0', '1']:
            errors.append("Sex must be '0' for female or '1' for male")

        # Validate Chest Pain types (cp)
        if cp not in ['0', '1','2','3']:
            errors.append("Chest Pain must be in between 0 & 3")

        # Validate Exercise Induced Angina (exang)
        if exang not in ['0', '1']:
            errors.append("Exercise induced angina  must be in between 0 & 1")
        

        # Validate Major vessels colored by flourosopy (ca)
        if ca not in ['0', '1','2','3']:
            errors.append("Number of major vessels colored by fluoroscopy must be in between 0 & 3")


        # Validate Thal
        if thal not in ['0', '1', '2']:
            errors.append("Thal must be '0' for normal, '1' for fixed defect, or '2' for reversible defect")

        return errors

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        # Validate user inputs
        validation_errors = validate_input_fields(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

        if validation_errors:
            st.error("\n\n".join(validation_errors))
        else:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                st.error("The person is having heart disease ")
                st.error("Please consult a cardiologist for further evaluation.")
            else:
                st.success("The person does not have any heart disease")