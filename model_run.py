# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:26:33 2023

@author: ACER
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import streamlit as st
from utils import md_runner

df = pd.read_csv("./assets/clean_data.csv")
sc = [0]

def model():
    X = df.iloc[:, :-1].values # features
    Y = df.iloc[:, -1].values  # target

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    clf = LogisticRegression(random_state=0, solver='lbfgs',
                             max_iter=1000).fit(X_train, Y_train)

    sc[0] = clf.score(X_test, Y_test)
    return clf

def stip():
    sta = 0
    with st.form("my_form"):
       st.write("Kindly fill the form to know about your placements!!")

       gender = {'M': 1, 'F': 0}
       boards_ten = {'Central': 0, 'Others': 1}
       boards_twl = {'Central': 0, 'Others': 1}
       twl_spl = {'Others': 0, 'Comm': 1, 'Sci': 2}
       ug_spl = {'Others': 1, 'Comm': 0, 'Sci': 2}
       work_ex = {'Yes': 1, 'No': 0}
       pg_spl = {"Mkt/hr": 1, "Mkt/fin": 0}

       g = st.radio(
           "Select your gender ", ('M', 'F'), horizontal=True)

       p_ten = st.slider("Your 10th Boards Percentage")

       b_ten = st.radio(
            "Select your 10th board ", ('Central', 'Others'),  horizontal=True)

       p_twl = st.slider("Your 12th Boards Percentage")

       b_twl = st.radio(
           "Select your 12th board ", ('Central', 'Others'), horizontal=True)

       s_twl = st.radio(
            "Select your class 12th stream", ('Sci', 'Comm', 'Others'),  horizontal=True)

       p_ug = st.slider("Your UG Degree Percentage")

       s_ug = st.radio(
            "Select your UG Degree ", ('Sci', 'Comm', 'Others'),  horizontal=True)

       wk = st.radio(
            "Do you have previous work exp ?", ('Yes', 'No'),  horizontal=True)

       p_et = st.slider("Your Percentage in Employbility test")

       s_pg = st.radio(
            "Select your MBA specialization ", ("Mkt/hr", "Mkt/fin"),  horizontal=True)

       p_pg = st.slider("Your PG Degree Percentage")

       checkbox_val = st.checkbox("I Agree to terms and conditions")
       submitted = st.form_submit_button("Submit")

       if (checkbox_val and submitted):
           st.write("Response saved, processing... Kindly wait!")
           sta = 1

    if sta:
        st.write("Your Status: ")

        Y_pred = x.predict([[gender[g], p_ten, boards_ten[b_ten], p_twl,
                             boards_twl[b_twl], twl_spl[s_twl], p_ug, ug_spl[s_ug],
                             work_ex[wk], p_et,  pg_spl[s_pg], p_pg]])
        if(Y_pred[0]):
            st.balloons()
            md_runner("<h2> Congrats!! your are eligible to be placed!!</h2>")
            st.write(f"Stats for nerds: Predicted with acc. of {round(sc[0])*100}%")

        else:
            st.snow()
            md_runner("<h2> Congrats!! your are going to be startup owner soon!!</h2>")
            st.write(f"Stats for nerds: Predicted with acc. of {round((sc[0]) * 100)}%")



x = model()
