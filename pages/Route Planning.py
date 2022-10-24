import streamlit as st
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


'''input1 = 0.0  # source's lattitude
input2 = 0.0  # source's longitude
input3 = 0.0  # destination's lattitude
input4 = 0.0  # destination's longitude'''

input1 = 39.88493  # source's lattitude
input2 = 116.3924  # source's longitude
input3 = 39.8787  # destination's lattitude
input4 = 116.39228  # destination's longitude


colors = ['blue', 'orange', 'green', 'yellow', 'purple']

algo_value='dijkstra'
network_value='drive'


st.write("""
Enter the coordinate of the Source
""")

# Activated two columns for input of lattitude and longitude of source
col1, col2 = st.columns(2)
'''with col1:
    input1 = st.number_input('Source Lattitude Coordinates')
with col2:
    input2 = st.number_input('Source Longitude Coordinates')'''

# Display the stored values of input by the user to double-check the given inputs
st.write("Lattitude:", input1, "Longitude:", input2)

# Display text
st.write("""
Enter the coordinate of the Destination
""")

# Activated two columns for input of lattitude and longitude of destination
col1, col2 = st.columns(2)
'''with col1:
    input3 = st.number_input('Destination Lattitude Coordinates')
with col2:
    input4 = st.number_input('Destination Longitude Coordinates')'''

# Display the stored values of input by the user to double-check the given inputs
st.write("Lattitude:", input3, "Longitude:", input4)

# A Radio button with three options to select the map_type by the user
map_type = 'OpenStreetMap'


# Slider to take the value of k from the user to plot k shortest routes
k = 1
k_paths = 1

# Slider to select the distance range between source and destination by the user ( in Kms )
range = 10

# Converting the selection of the user in integer from string, and changing it into metres
range_value = int(range)
range_value *= 1000

if st.button('Show me the Way'):

    # try and except blocks to handle the errors during the process of generation of maps with shortest routes

    # Configure OSMnx by setting the default global settings’ values
    ox.config(use_cache=True, log_console=True)

    # Creating a graph from OSMNX within some distance of source point
    G = ox.graph_from_point((input1, input2), dist=range_value, network_type=network_value, simplify=False)

    # adding edge speeds for all the nodes present in the graph G
    G = ox.speed.add_edge_speeds(G)

    # adding edge travel times for all the nodes present in the graph G
    G = ox.speed.add_edge_travel_times(G)

    # getting the nearest node from the source coordinates in the graph G generated above
    orig = ox.get_nearest_node(G, (input1, input2))

    # getting the nearest node from the destination coordinates in the graph G generated above
    dest = ox.get_nearest_node(G, (input3, input4))

    # shortest_path() function generates the shortest path between the orgin and source
    # and store the path in a 'route' named variable according to the algorithm
    # selected by the user and all computations are based on travel time
    route = nx.shortest_path(G, orig, dest, 'travel_time', method=algo_value)

    # Plotting the shortest route on the folium map named 'route_map' and coloring it red
    route_map = ox.plot_route_folium(G, route, route_color='red', tiles=map_type, weight=5)

    # Now, generating k number of shortest_path
    k_paths = k_paths - 1
    routes = ox.k_shortest_paths(G, orig, dest, k=k_paths, weight='length')

    # Plotting the other shortest_routes other than the main shortest route
    ind = 0
    for x in routes:
        if (x != route):
            route_map = ox.plot_route_folium(G, x, route_color=colors[ind], route_map=route_map, tiles=map_type,
                                             weight=2)
            ind = ind + 1

    # Putting a blue folium Marker on the source coordinates with proper tooltip
    tooltip1 = "Source"
    folium.Marker(
        [input1, input2], popup="Source", tooltip=tooltip1, icon=folium.Icon(color='blue')).add_to(route_map)

    # Putting a red folium Marker on the destination coordinates with proper tooltip
    tooltip2 = "Destination"
    folium.Marker(
        [input3, input4], popup="Destination", tooltip=tooltip2, icon=folium.Icon(color='red')).add_to(
        route_map)

    # Displaying the final map with shortest_path plotted and markers placed on the correct locations
    folium_static(route_map)