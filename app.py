import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import geopandas as gpd



df = pd.read_csv('data/listings.csv')
nb = gpd.read_file('data/neighbourhoods.geojson')

df = df[df['availability_365'] > 0]
df = df[df['room_type'] != "Hotel room"]


mb_token = "pk.eyJ1IjoiYXJlbmFnc2UiLCJhIjoiY2t3d3hrMjl6MDg4dDMxcjBrbHBycHFqYSJ9.Izk3V1cMsjb96YruvGeMzg"



st.set_page_config(layout="wide")
st.title("Airbnbs à Bordeaux")

with st.container():
    st.write("This is inside the container")

    

    px.set_mapbox_access_token(mb_token)

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",  hover_data=["price", "availability_365"],   color="room_type",  size_max=15, zoom=10, width=800, height=500) #color_continuous_scale=px.colors.cyclical.IceFire,

    st.plotly_chart(fig)


col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

