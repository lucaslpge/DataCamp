import streamlit as st

st.set_page_config(layout="wide")
st.markdown("#Route Planning")
st.sidebar.markdown("Route Planning")


# ------------------------------------------------ PAGES ------------------------------------------------ #


def home():
    st.markdown("#Home")
    st.sidebar.markdown("#Home")

def page2():
    st.markdown("#Trafic")
    st.sidebar.markdown("#Trafic")

def page3():
    st.markdown("#Route Planning")
    st.sidebar.markdown("#Route Planning")