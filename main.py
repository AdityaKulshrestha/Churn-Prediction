import streamlit as st
import requests
import pandas as pd
import numpy as np
from backend import ChurnPredictionOutput, churn_model

st.set_page_config(page_title="Churn Prediction App")

st.title("Welcome to Churn Predictor :computer:")

st.subheader("""
     :dart:  This Streamlit app is made to predict customer churn.
    """)

st.info("Input the data below")

st.write("")
st.write("")
st.write("")
st.write("")

with st.form(key='predict'):
    name = st.text_input(label="Name")

    st.divider()
    col1, col2 = st.columns([1, 1])
    with col1:
        with st.container():
            gender = st.radio(label='Gender', options=['Male', 'Female'])
            location = st.selectbox(label='Location',
                                    options=['Los Angeles', 'Miami', 'New York', 'Houston', 'Chicago'])
            age = st.slider(label='Age', min_value=18, max_value=70, )
    with col2:
        with st.container():
            subscription = st.number_input("Subscription Length", min_value=1, max_value=24)
            bill = st.number_input("Monthly Bill", min_value=0.0)
            data_usage = st.number_input("Data Usage", min_value=0)

    submit = st.form_submit_button(label='Submit')
    st.divider()

    if submit:
        payload = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Location": location,
            "Subscription_Length_Months": subscription,
            "Monthly_Bill": bill,
            "Total_Usage_GB": data_usage
        }

        with st.spinner("Loading"):
            # For deployment purpose on streamlit cloud. The model is loaded inside main file.
            # For production. Remove the comment below after starting the fastapi backend.
            input_data = {
                'Age': payload['Age'],
                'Subscription_Length_Months': payload['Subscription_Length_Months'],
                'Monthly_Bill': payload['Monthly_Bill'],
                'Total_Usage_GB': payload['Total_Usage_GB'],
                'Gender_Female': 0,
                'Gender_Male': 0,
                'Location_Chicago': 0,
                'Location_Houston': 0,
                'Location_Los_Angeles': 0,
                'Location_Miami': 0,
                'Location_New_York': 0
            }

            location = payload['Location'].split()
            location = "_".join(location)
            input_data[f'Location_{location}'] = 1

            if payload['Gender'] == "Male":
                input_data['Gender_Male'] = 1
            else:
                input_data['Gender_Female'] = 1

            input_df = pd.DataFrame(input_data, index=[0])

            churn_pred = churn_model.predict(np.array(input_df).reshape(1, -1))

            output = ChurnPredictionOutput(Name=payload['Name'], Churn_Prediction=churn_pred)
            # response = requests.post("http://localhost:8000/predict_churn/", json=payload)
            response = output
            print(response)

        if response.Churn_Prediction == 0:
            st.markdown(":persevere: Unfortunately, our assessment suggests that the "
                        "customer might be considering "
                        "discontinuing their engagement with our services.", )
        else:
            st.balloons()
            st.markdown(":tada: Based on our analysis, we anticipate that the customer "
                        "will continue their "
                        "engagement with our services", unsafe_allow_html=True)
    else:
        st.error('Enter the data first!', icon="🚨")


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# Emojis and UI enhancements
st.write("🔍 Analyze customer data to predict churn.")
st.write("📊 Explore insights to make informed decisions.")

# Footer
st.divider()
st.write("Made with ❤️ by Aditya Kulshrestha")
