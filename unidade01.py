import pandas as pd
import numpy as np
import streamlit as st 
import altair as alt 
import matplotlib.pyplot as mp
import seaborn as sb

@st.cache_data

def load_database():
    return pd.read_csv('brasil_estados.csv')

st.title('Dados - GCI')

estados = load_database()

dados, estatistica = st.tabs(['Dados', 'Estatistica descritivas'])

with dados:
    regiao = st.selectbox(
        'Select região',
        estados['regiao_nome'].unique()
    )
    st.dataframe(estados[estados['regiao_nome'] == regiao])

with estatistica:
    variavel = st.selectbox(
        'Selecione a variável',
        ['area', 'populacao', 'idh', 'matricula']

    )
    st.table(estados[variavel].describe())