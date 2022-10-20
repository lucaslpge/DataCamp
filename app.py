import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title='Data Camp', page_icon='taxi')


# ------------------------------------------------ PAGES ------------------------------------------------ #


st.markdown("#Home")
st.sidebar.markdown("Home")

def home():
    st.markdown("#Home")
    st.sidebar.markdown("#Home")

def page2():
    st.markdown("#Trafic")
    st.sidebar.markdown("#Trafic")

def page3():
    st.markdown("#Route Planning")
    st.sidebar.markdown("#Route Planning")


st.title("Welcome on our website !")
l_col, r_col = st.columns(2)
with l_col:
    st.subheader("Traffic can be very heavy in a city like Beijing with a population of nearly 22 millions and nearly 70,000 taxis operating 24/7. ")
with r_col:
    image_taxi_pekin = Image.open('pictures/taxi_pekin.jpg')
    st.image(image_taxi_pekin, width=500)


l_col1, r_col1 = st.columns(2)
with l_col1:
    image1 = Image.open('pictures/efrei.png')
    st.image(image1, width=400, caption='EFREI Paris')
with r_col1:
    st.subheader('As part of our engineering studies at Efrei Paris and our Data Camp, we had to imagine, study and design an application in the cloud to meet the following 3 criteria:')
    st.subheader('- display the most congested streets')
    st.subheader('- the average time to go from point A to point B')
    st.subheader('- a global view of Beijing traffic')


st.subheader('Meet the team !')
l_col1, r_col1 = st.columns(2)
with l_col1:
    image1 = Image.open('pictures/anto.jpg')
    st.image(image1, width=350, caption='Antonin Guillocheau')
with r_col1:
    image2 = Image.open('pictures/lucas.jpg')
    st.image(image2, width=350, caption='Lucas Le Page')

