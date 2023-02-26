# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:02:42 2023

@author: ACER
"""

import streamlit as st


def md_runner(data):
    st.markdown(data, unsafe_allow_html=True)


legend = {

    "Key": ["sl_no",
            "gender",
            "ssc_p",
            "ssc_b",
            "hsc_p",
            "hsc_b",
            "hsc_s",
            "degree_p",
            "degree_t",
            "workex",
            "etest_p",
            "specialisation",
            "mba_p",
            "status",
            "salary"],

    "Full Form": ["Serial Number",
                  "Gender (M/F)",
                  "Class 10th boards Percentage",
                  "Board opted in class 10th",
                  "Class 12th boards Percentage",
                  "Board opted in class 12th",
                  "Main subject in class 12th Arts/Comm/Sci",
                  "Percentage scored in Degree Exams",
                  "Under Graduation Degree Stream Sci/Comm/Others",
                  "Any previous work experience",
                  "Employability test percentage",
                  "Post Graduation(MBA)- Specialization",
                  "MBA percentage",
                  "Placed or not",
                  "Current Salary"]
    }
