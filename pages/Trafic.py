import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Data Camp", page_icon="taxi")


# ------------------------------------------------ PAGES ------------------------------------------------ #


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


# ------------------------------------------------ LOADING CSV ------------------------------------------------ #


st.header('Welcome to the trafic page !')
df = pd.read_csv('clean_taxi.csv')
df2 = pd.read_csv('Data_China_71k.csv')


# ------------------------------------------------ FUNCTIONS ------------------------------------------------ #


def map(df):
    st.header("Take a look at the trafic")
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Just say us what day and what time you want to check the trafic :")
        day_to_filter = st.slider('Day', 2, 8, 4)
        hour_to_filter = st.slider('Hour', 0, 23, 15)
        start_minute, end_minute = st.select_slider(
            'Minute',
            options=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 59],
            value=(15, 30))
    with right_col:
        st.write('You are looking at the trafic at the ', day_to_filter, '/02/2008 between', hour_to_filter, ':', start_minute, 'and', hour_to_filter, ':', end_minute)
        filtered_data = df.loc[(df.hour == hour_to_filter) & (df.day == day_to_filter) & (df.minute >= start_minute) & (df.minute <= end_minute)]
        st.map(filtered_data)

def street(df2):
    st.header("Take a look at the streets of highest congestion rate :")
    left_col_street, right_col_street = st.columns(2)
    with left_col_street :
        st.subheader("Here you can see the streets (left column) with the number of taxis present for each street (right column) and sort them in ascending or descending order by cliking on the arrow next to '0'.")
    with right_col_street :
        def count_rows(rows):
            return len(rows)
        st.write(df2['Street'].value_counts().head(10))


# ------------------------------------------------ MAIN FUNCTION ------------------------------------------------ #


def main(df, df2):
    map(df)
    street(df2)

main(df, df2)