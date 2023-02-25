# -*- coding: utf-8 -*-

import streamlit as st
from utils import md_runner
from streamlit_option_menu import option_menu
from data_analysis import data_page
from home import home_page


main_options = ["Home", 'Data Analysis', 'Model Prediction']

with st.sidebar:
    selected = option_menu("Main Menu", main_options,
        icons=['house', 'gear', 'play'], menu_icon="cast", default_index=0)

if selected == main_options[0]:
    home_page()

if selected == main_options[1]:
    data_page()
