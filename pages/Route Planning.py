import streamlit as st

st.set_page_config(layout="wide", page_title="Data Camp", page_icon="taxi")


# ------------------------------------------------ PAGES ------------------------------------------------ #


st.markdown("#Route Planning")
st.sidebar.markdown("Route Planning")

def home():
    st.markdown("#Home")
    st.sidebar.markdown("#Home")

def page2():
    st.markdown("#Trafic")
    st.sidebar.markdown("#Trafic")

def page3():
    st.markdown("#Route Planning")
    st.sidebar.markdown("#Route Planning")