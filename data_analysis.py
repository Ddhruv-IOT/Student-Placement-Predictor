# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:26:12 2023

@author: ACER
"""
import streamlit as st
import pandas as pd
from utils import md_runner

df = pd.read_csv("./assets/Placement_Data_Full_Class.csv")

def data_exploration():

    md_runner("<h2> Data Head </h2>")
    st.table(df.head()) #df.head()
    # st.des
    st.info("Test", icon="i")

def data_page():

    main_opt = ("Data Overview", "Data Visualization")

    selection = st.sidebar.radio(
        "Select to explore ", main_opt)

    if selection == main_opt[0]:
        st.write('Here you go')
        data_exploration()

    else:
        st.write("You didn\'t select comedy.")
