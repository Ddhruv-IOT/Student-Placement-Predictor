# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:26:12 2023

@author: ACER
"""
import streamlit as st
import pandas as pd

df = pd.read_csv("./assets/Placement_Data_Full_Class.csv")

def data_exploration():
    df.head()

def data_page():

    main_opt = ("Data Overview", "Data Visualization")

    selection = st.sidebar.radio(
        "Select to explore ", main_opt)

    if selection == main_opt[0]:
        st.write('Here you go, ')

    else:
        st.write("You didn\'t select comedy.")
