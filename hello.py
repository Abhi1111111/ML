import pandas as pd
import streamlit as st
data = pd.read_csv("movies.csv")
st.write(data)
