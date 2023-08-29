import streamlit as st
import pandas as pd
from typing import Optional
from pathlib import Path

import plotly.express as px


st.set_page_config(layout="wide", page_title="Data Dashboard", page_icon=":bar_chart:")

# overall_view_menu, describe_menu, plot_menu = st.columns(3)
# with overall_view_menu.expander("Overall"):
#     st.write("Overall")
# with describe_menu.expander("Describe"):
#     st.write("Describe")
# with plot_menu.expander("Plots"):
#     st.write("Plots")

st.title("Data Dashboard")
st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)  # to reduce the padding on the top
st.markdown("_Prototype v0.0.1_")


@st.cache_data
def load_data(path: str | Path) -> pd.DataFrame:
    data = pd.read_excel(path, dtype_backend="pyarrow")
    # data = pd.read_csv(path, engine="pyarrow", dtype_backend="pyarrow", encoding="ISO-8859-1")
    # light clearnig here..


    return data


with st.sidebar:
    st.header("Configuration")
    with st.expander(":file_folder:  Uploads"):
        uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info("Upload a file throught config")
    st.stop()

df = load_data(uploaded_file)
with st.expander("Data Preview"):
    st.dataframe(
        df, 
        # column_config={"Year": st.column_config.NumberColumn(format="%d")}
    )

# use duckdb which is an in-memory database than can run sql on pandas dataframe

