# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:02:42 2023

@author: ACER
"""

import streamlit as st

def md_runner(data):
    st.markdown(data, unsafe_allow_html=True)
