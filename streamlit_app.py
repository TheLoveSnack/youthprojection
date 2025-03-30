import numpy as np
import pandas as pd
import streamlit as st

combined = pd.read_csv("combined.csv")

cola1, cola2, cola3 = st.columns([1,1,1])
colb1, colb2, colb3 = st.columns([1,1,1])

leagues = combined['league'].unique()
league = cola1.selectbox('League',
leagues.tolist())

years = combined['season'].unique()
year = colb3.selectbox('Year',
years.tolist())

filters = combined[(combined['league']==league) & (combined['season']==year)]
st.write(filters)
