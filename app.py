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
px.set_mapbox_access_token(mb_token)

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",  hover_data=["price", "availability_365"],   color="room_type", 
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
fig.show()