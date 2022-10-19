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


def map(df):
    st.header("Take a look at the Trafic")
    st.subheader("Just say us what day and what time you want to check the trafic :")
    day_to_filter = st.slider('Day', 2, 8, 2)
    hour_to_filter = st.slider('Hour', 0, 23, 15)
    start_minute, end_minute = st.select_slider(
        'Minute',
        options=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 59],
        value=(15, 30))

    st.write('You are looking at the trafic at the ', day_to_filter, '/02/2008 between', hour_to_filter, ':', start_minute, 'and', hour_to_filter, ':', end_minute)
    filtered_data = df.loc[(df.hour == hour_to_filter) & (df.day == day_to_filter) & (df.minute >= start_minute) & (df.minute <= end_minute)]
    st.map(filtered_data)

def main(df):
    map(df)

df = st.file_uploader("Choose a file")
if df is not None:
    df = pd.read_csv(df)
    st.write(df)
    main(df)