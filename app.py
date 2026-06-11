import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')
hist_checkbox = st.checkbox('Criar Histograma')

if hist_checkbox:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carro')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)


hist_button = st.checkbox('Criar Gráfico')

if hist_button:
    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
