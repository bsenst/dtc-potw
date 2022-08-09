'''
install streamlit "https://docs.streamlit.io/library/get-started/installation"
run file as ">streamlit run main_page.py"
'''

import streamlit as st
import pandas as pd
import numpy as np

# st.set_page_config(page_title=None, page_icon=None, layout="wide")

url = "https://www.destatis.de/static/de_/opendata/data/preise_ueberblick_originalwert.csv"
price = "preise_ueberblick_originalwert.csv"

#@st.cache
def load_data():
    return pd.read_csv(price, encoding="latin", skiprows=1, delimiter=";")

df = load_data()

st.dataframe(df.head())

chart_data = pd.DataFrame(
     [float(x.replace(",", ".")) for x in df["Verbraucherpreisindex, 2015=100"]],
     columns=['Verbraucherpreisindex'])

st.line_chart(chart_data)

st.write(url)
st.write("as available through the Statistisches Bundesamt (Destatis)")
st.write("dl-de/by-2-0 http://www.govdata.de/dl-de/by-2-0")