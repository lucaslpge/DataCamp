import streamlit as st
import pandas as pd

st.markdown("#Trafic")
st.sidebar.markdown("Trafic")

def home():
    st.markdown("#Home")
    st.sidebar.markdown("#Home")

def page2():
    st.markdown("#Trafic")
    st.sidebar.markdown("#Trafic")

def page3():
    st.markdown("#Route Planning")
    st.sidebar.markdown("#Route Planning")

df = pd.read_csv("clean_taxi.csv")

st.header("Take a look at the Trafic")
st.subheader("Just say us what day and what time you want to check the trafic :")
day_to_filter = st.slider('Day', 2, 8, 2)
hour_to_filter = st.slider('Hour', 0, 23, 15)
minute_to_filter = st.slider('Minute', 0, 59, 30)
filtered_data = df.loc[(df.hour == hour_to_filter) & (df.day == day_to_filter) & (df.minute == minute_to_filter)]
st.map(filtered_data)