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

df_filter = df_filter[df_filter['room_type'].isin(options_type)]
df_filter = df_filter[df_filter['price'] >= values_price[0]]
df_filter = df_filter[df_filter['price'] <= values_price[1]]


with st.container():

    px.set_mapbox_access_token(mb_token)

    fig = px.scatter_mapbox(df_filter, lat="latitude", lon="longitude",  hover_data=["price", "availability_365", "id"],   color="room_type",  size_max=15, zoom=10, width=800, height=500) #color_continuous_scale=px.colors.cyclical.IceFire,

    st.plotly_chart(fig, use_container_width=True)





col3, col4 = st.columns(2)

with col3:
    st.header("Top 10 des propriétaires")
    # You can call any Streamlit command, including custom components:
    nb_proprietes_pp = df_filter[['host_id']].value_counts().head(10)
    nb_proprietes_pp = nb_proprietes_pp.to_frame().reset_index().rename(columns= {0: 'Nombre de propriétés'})
    nb_proprietes_pp.index.name = 'index'
    nb_proprietes_pp['host_id']= nb_proprietes_pp['host_id'].map(str)

    fig2 = px.bar(nb_proprietes_pp[:10], \
             x='Nombre de propriétés', \
             y=nb_proprietes_pp.index, \
             text='Nombre de propriétés', \
             title='TOP 10 : Propriétaires qui ont le plus de biens à louer', \
             orientation='h',
             hover_data=['host_id'])
    fig2.update_yaxes(autorange='reversed')
    st.plotly_chart(fig2, use_container_width=True)

with col4:
    st.header("Taux de disponibilité par bien")
    proportion_dispo = df_filter[['availability_365']]/3.65
    fig3 = px.histogram(proportion_dispo, x='availability_365', nbins=13)
    fig3.update_layout(bargap=0.1)
    st.plotly_chart(fig3, use_container_width=True)



# pourcentage de proprios ayant 1 , 2 , 3 propriétés / top 5 des proprios 
# taux de disponibilité < > moitié de l'année

# revenus max #revenus par mois
# quartiers les plus demandés / chers / proposés


# chambre privée ou logement entier ?
# liens vers annonces