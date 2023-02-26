# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:26:12 2023

@author: ACER
"""
import streamlit as st
import pandas as pd
from utils import md_runner
from utils import legend
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image

image = Image.open('./assets/images.png')

df = pd.read_csv("./assets/Placement_Data_Full_Class.csv")


def data_exploration():

    md_runner("<h2> Data Legend </h2>")
    st.info("Represnts the actual meaning of column names in dataset", icon="ℹ️")
    st.table(pd.DataFrame.from_dict(legend))

    md_runner("<h2> Data Head </h2>")
    st.write("Gives a brief idea of dataset from top 5 entries")
    st.table(df.head())

    md_runner("<h2> Data Tail </h2>")
    st.write("Gives a brief idea of dataset from last 5 entries")
    st.table(df.tail())

    md_runner("<h2> Data Shape </h2>")
    shape = df.shape
    st.write("The number of Rows: ", shape[0])
    st.write("The number of Columns: ", shape[1])

    md_runner("<h2> Count of Null Values </h2>")
    st.table(df.isna().sum())


def data_cleaning():
    df = pd.read_csv("./assets/Placement_Data_Full_Class.csv")

    md_runner("<h1> Data Cleaning and Pre-Proceesing </h1>")

    md_runner("<h2> Removing Columns</h2>")
    st.info("As we are not going to utilize Serial Number and Salary based data, its        better to remove them.", icon="ℹ️")
    st.code("df.drop('col_name', axis=1, inplace=True)", language="python")

    df.drop('sl_no', axis=1, inplace=True)
    df.drop('salary', axis=1, inplace=True)

    st.write("The rows and columns remaining after removal or drop: ")
    shape = df.shape
    st.write("The number of Rows: ", shape[0])
    st.write("The number of Columns: ", shape[1])

    md_runner("<h2> Conversion of data</h2>")
    st.info("As we are having lots of text data and mostly 'Yes' or 'No', so its better to convert it into categorical type", icon="ℹ️")
    st.code("df[col] = df[col].astype('category')", language="python")

    data_type_conversio_cols = ["gender", "ssc_b", "hsc_b",
                                "degree_t", "workex", "specialisation", "status", "hsc_s"]

    for col in data_type_conversio_cols:
        df[col] = df[col].astype('category')

    st.write("The datatypes after conversion: ")
    st.table(df.dtypes)

    md_runner("<h2> The Cat Codes </h2>")
    st.info("As we have converted data to categorical types, now we have got CAT codes instead of text. They are 0, 1, 2 respectively.", icon="ℹ️")
    st.code("df[col] = df[col].cat.codes)", language="python")

    data_type_conversio_cols = ["gender", "ssc_b", "hsc_b",
                                "degree_t", "workex", "specialisation", "status", "hsc_s"]

    for col in data_type_conversio_cols:
        df[col] = df[col].cat.codes

    md_runner(
        "<h4>Once done, we need to save the updated dataset for Visualization part</h4>")


def data_visualization():

    df = pd.read_csv("./assets/clean_data.csv")

    md_runner("<h1> Gender Distribution </h1>")
    data = df.groupby('gender').size()
    labels = 'Female', 'Male'

    fig1, ax1 = plt.subplots(figsize=(2, 2))
    ax1.pie(data, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=['#b465b5', '#93b50d'])
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    st.pyplot(fig1)
    md_runner("<br/>")

    md_runner(
        "<b><u>Conclusion</u>:</b> In this survey, males have participated in majority.")

    md_runner("<h1> Placement Distribution </h1>")
    fig = plt.figure(figsize=(5, 2))
    status = df.groupby('status').size()

    plt.bar([0], height=status[1], color="blue", width=0.5)
    plt.bar([1], height=status[0], color="red", width=0.5)

    plt.xlabel("Status")
    plt.ylabel("Count")

    plt.xticks(np.arange(2), ('Placed', 'Not Placed'))
    plt.title("Placed vs Not Placed ")

    st.pyplot(fig)
    st.write(
        f"Percentage of Students Placed: {round((status[1]/status.sum())*100)}%")
    st.write(
        f"Percentage of Students Not Placed: {round((status[0]/status.sum())*100)}%")
    md_runner("<b><u>Conclusion</u>:</b> Majority of students are placed")
    md_runner("<br/>")

    md_runner("<h1> Average Percentage(s) </h1>")
    fig = plt.figure(figsize=(5, 2))

    values = [(df['ssc_p'].mean()), (df['hsc_p'].mean()), (df['mba_p'].mean()),
              (df['degree_p'].mean())]

    ax = fig.add_axes([1, 1, 1, 1])
    names = ['ssc_p', 'hsc_p', 'mba_p', 'degree_p']

    ax.set_ylabel('Average percentages')
    ax.set_title('Average Percentage')
    ax.bar(names, values, width=0.4, color=["blue", "red", "green", "orange"])
    st.pyplot(fig)

    st.write(f"Class 10th Boards percentage: {round(values[0])}%")
    st.write(f"Class 12th Boards percentage: {round(values[1])}%")
    st.write(f"MBA (Post grad.) Percentage: {round(values[2])}%")
    st.write(f"Under grad. Degree Percentage: {round(values[3])}%")

    st.write("Important realation between placements and percentages")
    df_grade = df.groupby(['status']).mean()[['hsc_p', 'degree_p',
                                              'mba_p']].reset_index()
    st.table(df_grade.head())

    md_runner("<b><u>Conclusion</u>:</b> Avg. percentages throughout all the stages are about 60% and having around 64% throught will increase placement chances, specially in 12th boards.")
    md_runner("<br/>")

    md_runner("<h1>Let's Explore co-relations </h1>")

    st.write('Class 10th Boards percentage to placement ',
             round(df['status'].corr(df['ssc_p'])*100, 1), '%')

    st.write('Class 12th Boards percentage to placement',
             round(df['status'].corr(df['hsc_p'])*100, 1), '%')

    st.write('MBA (Post grad.) Percentage to placement ',
             round(df['status'].corr(df['mba_p'])*100, 1), '%')

    st.write('Under grad. Degree Percentage to placement ',
             round(df['status'].corr(df['degree_p'])*100, 1), '%')

    st.write('Employbility test Percentage to placement ',
             round(df['status'].corr(df['etest_p'])*100, 1), '%')

    st.write('Gender and placement',
             round(df['status'].corr(df['gender'])*100, 1), '%')

    st.write('Previous Work Experience to placement ',
             round(df['status'].corr(df['workex'])*100, 1), '%')

    md_runner("<b><u>Conclusion</u>:</b> Candidates should have perfromed well in class 10th, 12th and UG Degree program and should have previous work exp. (mostly which comes from internships), for having better placements. ")

    md_runner("<br/>")

    md_runner("<h1> Male vs Female Placement Rate </h1>")

    fig = plt.figure(figsize=(5, 3))
    x = df.groupby(['gender', 'status']).size().unstack()

    g_pla = x[0][1]
    g_npla = x[0][0]
    b_pla = x[1][1]
    b_npla = x[1][0]

    print(g_pla, g_npla)

    plt.bar([0, 2], height=[g_npla, g_pla], color='b', align='center')
    plt.xticks(range(0, 4), ['not placed \n(F)',
                             'not placed \n(M)', 'placed (F)', 'placed (M)'])
    plt.bar([1, 3], height=[b_npla, b_pla], color='g', align='center')
    plt.legend(['female placement', 'male placement'])

    st.pyplot(fig)

    st.write(f"Percentage of females placed (relative to females): {round((g_pla)/(g_pla+g_npla)*100)}%")
    st.write(f"Percentage of males placed (relative to males): {round((b_pla)/(b_pla+b_npla)*100)}%")

    md_runner("<b><u>Conclusion</u>:</b> It's clear that male students are having slightly higher placement rates, but it dosen't mean at all, that males are performing better than females. If we normalize the ratio of male and female candidates, the rate is almost equal.")
    md_runner("<br/>")


    md_runner("<h1> Ready for advance analysis ?? </h1>")

    md_runner("<h1>Combined Box Plot </h1>")

    recruit_numeric = df[['ssc_p','hsc_p','degree_p','etest_p','mba_p','status']]
    recruit_numeric_melt = pd.melt(recruit_numeric,id_vars='status',
                                   value_vars=['ssc_p','hsc_p',
                                               'degree_p','etest_p','mba_p'])
    fig = plt.figure(figsize=(6, 4))
    sns.boxplot(x="variable", y="value",
            hue="status", data=recruit_numeric_melt)
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> The plot below shows that almost all variables have a higher value in the placed group than not placed group, while MBA percent seem to have the least influence on whether a student is placed or not.")
    md_runner("<br/>")


    md_runner("<h1> 10th Board Type vs Placements </h1>")
    fig, ax = plt.subplots(figsize=(18, 10))

    df.groupby(["ssc_b", "status"]).size().groupby(level=0).apply(
        lambda x: 100 * x / x.sum()).unstack().plot(kind='bar', stacked=True,
                                                    ax=ax)
    plt.legend(loc='upper right', title='Board of Education')
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> There is no major differnce if you had given your class 10th boards from central board or others.")
    md_runner("<br/>")


    md_runner("<h1>12th Board Type vs Placements </h1>")
    fig, ax = plt.subplots(figsize=(18, 10))

    df.groupby(["hsc_b","status"]).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()).unstack().plot(kind='bar',stacked=True,
                                                ax=ax)
    plt.legend(loc='upper right', title='Board of Education')
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> There is no major differnce if you had given your class 12th boards from central board or others.")
    md_runner("<br/>")


    md_runner("<h1>Specialization in Higher Education </h1>")
    fig, ax = plt.subplots(figsize=(18, 10))

    df.groupby(["hsc_s","status"]).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()).unstack().plot(kind='bar', stacked=True,
                                                ax=ax)

    plt.legend(loc='upper right', title='Higher Education Specialization')
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> There is possibility that commerce and science are more likely to get placed.")
    md_runner("<br/>")


    md_runner("<h1>UG Degree vs Placements </h1>")
    fig, ax = plt.subplots(figsize=(18, 10))

    df.groupby(["degree_t","status"]).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()).unstack().plot(kind='bar', stacked=True,
                                                ax=ax)

    plt.legend(loc='upper right', title='Degree type')
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> There is possibility that comm/management and sci/tech are more likely to get placed.")
    md_runner("<br/>")


    md_runner("<h1>Work Exp. vs Placements </h1>")
    fig, ax = plt.subplots(figsize=(18, 10))

    df.groupby(["workex","status"]).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()).unstack().plot(kind='bar', stacked=True,
                                                ax=ax)

    plt.legend(loc='upper right', title='Work experience')
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> Having work experience is more likely to get placed.")
    md_runner("<br/>")


    md_runner("<h1>MBA Specialization </h1>")
    fig, ax = plt.subplots(figsize=(18, 10))

    df.groupby(["specialisation","status"]).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()).unstack().plot(kind='bar', stacked=True,
                                                ax=ax)

    plt.legend(loc='upper right', title='specialisation')
    st.pyplot(fig)

    md_runner("<b><u>Conclusion</u>:</b> Here, mrkt/finance are more likely to get placed than mrkt/hr.")
    md_runner("<br/>")

def data_page():

    main_opt = ("Data Overview", "Data Pre-processing", "Data Visualization")

    selection = st.sidebar.radio(
        "Select to explore ", main_opt)

    if selection == main_opt[0]:
        st.image(image, caption='Campus Placements', width=700)
        data_exploration()

    elif selection == main_opt[1]:
        data_cleaning()

    else:
        data_visualization()
