import streamlit as st
import requests


st.title("HR Analytics: employee promotion prediction")
education = st.selectbox("Education", [0, 1, 2])
age = st.number_input("Age")
previous_year_rating = st.number_input("Previous Year Rating")
length_of_service = st.number_input("Length of Service")
no_of_trainings = st.number_input('How many times do you do the training?')
avg_training_score = st.number_input('Average Training Score')
awards_won = st.selectbox("Have you won an awards while working here?", ['No', 'Yes'])
# inference
data = {'Education':education,
        'Age':age,
        'Previous Year Rating': previous_year_rating,
        'Length of Service':length_of_service,
        'how many times do you do the training?':no_of_trainings,
        'Average Training Score': avg_training_score, 
        'Have you won an awards while working here?':awards_won}



URL = "https://h8-model-deployment-backend.herokuapp.com/titanic"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['result']['classes'])