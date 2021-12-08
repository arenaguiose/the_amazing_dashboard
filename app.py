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

col1, col2 = st.columns(2)

with col1:
    options_type = st.multiselect(
         'Type de logement',
         ['Entire home/apt', 'Private room', 'Shared room'])
#st.write('You selected:', options_type)


with col2:
    values_price = st.slider(
     'Prix à la nuitée',
     float(df.price.min()), float(df.price.max()), (float(df.price.min()), float(df.price.max())))
#st.write('Values:', values_price)

df_filter = df
for i in options_type:
    df_filter = df_filter[df_filter['room_type'] == i]

df_filter = df_filter[df_filter['price'] >= values_price[0]]
df_filter = df_filter[df_filter['price'] <= values_price[1]]


with st.container():

    px.set_mapbox_access_token(mb_token)

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",  hover_data=["price", "availability_365"],   color="room_type",  size_max=15, zoom=10, width=800, height=500) #color_continuous_scale=px.colors.cyclical.IceFire,

    st.plotly_chart(fig, use_container_width=True)


col3, col4 = st.columns(2)

with col3:
    st.header("A cat")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

with col4:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")




# quartiers les plus demandés / chers / proposés
# top 5 des proprios / pourcentage de proprios ayant 1 , 2 , 3 propriétés
# revenus max
#chambre privée ou logement entier ?
#revenus par mois