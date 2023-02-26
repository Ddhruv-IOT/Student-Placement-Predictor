# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:26:33 2023

@author: ACER
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import streamlit as st

df = pd.read_csv("./assets/clean_data.csv")

def model():
    X = df.iloc[:, :-1].values # features
    Y = df.iloc[:, -1].values  # target

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    clf = LogisticRegression(random_state=0, solver='lbfgs',
                             max_iter=1000).fit(X_train, Y_train)

    print(clf.score(X_test, Y_test))
    return clf

def stip():
    with st.form("my_form"):
       st.write("Inside the form")
       slider_val = st.slider("Form slider")
       checkbox_val = st.checkbox("Form checkbox")
       submitted = st.form_submit_button("Submit")
       if submitted:
           st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")
    Y_pred = x.predict([[87, 0, 95, 0, 2, 78, 2, 0, 0, 1, 0, 0]])
    print(Y_pred)


x = model()
