import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium as f,folium
import osmnx as ox
import networkx as nx


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


input1 = 0.0  # source's lattitude
input2 = 0.0  # source's longitude
input3 = 0.0  # destination's lattitude
input4 = 0.0  # destination's longitude

colors = ['blue', 'orange', 'green', 'yellow', 'purple']

algo_value='dijkstra'
network_value='drive'
map_type = 'OpenStreetMap'
k = 1

df = pd.read_csv('clean_taxi.csv')
df

st.write("""
Enter the coordinate of the Source
""")

col1, col2 = st.columns(2)
with col1:
    input1 = st.number_input('Source Lattitude Coordinates')
with col2:
    input2 = st.number_input('Source Longitude Coordinates')

st.write("Lattitude:", input1, "Longitude:", input2)

st.write("""
Enter the coordinate of the Destination
""")

col1, col2 = st.columns(2)
with col1:
    input3 = st.number_input('Destination Lattitude Coordinates')
with col2:
    input4 = st.number_input('Destination Longitude Coordinates')

st.write("Lattitude:", input3, "Longitude:", input4)


if st.button('Show me the Way'):

    ox.config(use_cache=True, log_console=True)

    G = ox.graph_from_point((input1, input2), dist=10000, network_type=network_value, simplify=False)

    G = ox.speed.add_edge_speeds(G)

    G = ox.speed.add_edge_travel_times(G)

    orig = ox.get_nearest_node(G, (input1, input2))

    dest = ox.get_nearest_node(G, (input3, input4))

    route = nx.shortest_path(G, orig, dest, 'travel_time', method=algo_value)

    route_map = ox.plot_route_folium(G, route, route_color='red', tiles=map_type, weight=5)

    tooltip1 = "Source"
    folium.Marker(
        [input1, input2], popup="Source", tooltip=tooltip1, icon=folium.Icon(color='blue')).add_to(route_map)

    tooltip2 = "Destination"
    folium.Marker(
        [input3, input4], popup="Destination", tooltip=tooltip2, icon=folium.Icon(color='red')).add_to(
        route_map)

    folium_static(route_map)