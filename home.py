# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:53:01 2023

@author: ACER
"""
import streamlit as st
from streamlit_option_menu import option_menu
from utils import md_runner

text = """
<h1><span class='logo'>Hi There</span> <img src="https://raw.githubusercontent.com/Ddhruv-IOT/Ddhruv-IOT/main/assetes/wave-hello.gif" height=80px width=80px/></h1>

<h3>I am Ddhruv Arora</h3> <p class="intro-p">
 A Flutter developer, Machine Learning Enthusiast, and open source contributor based in India.

very passionate about learning and understanding new technologies. I always try to build projects involving multiple technologies as I am passionate about <span class="elarge pg">integrating</span> technologies. I have worked in teams for various startups as an Intern and helped them in launching their prototypes, as an open-source contributor at GitHub, and got valuable learning experience.

Currently, I'm in the fourth year of my <span class="elarge pg">dual degree course</span> at <span class="elarge pg">Amity University Rajasthan</span>, President of RaIoT Labs, Chief Igniter at D2C Igniters Club, and Class Representative.
</p>

<b><p>Connect with me on <a target='_blank' href='https://linkedin.com/in/ddhruv-arora'>Linkedin</a> </p></b>

<style> .elarge {
    transition: 1s;
}

.elarge:hover,
.left-col:hover>.heading-phone span,
.right-col:hover>h3 {
    transition: 1s;
    font-size: 3vw;
    text-shadow: 0 1px 0 #ccc, 0 2px 0 #ccc, 0 3px 0 #ccc, 0 4px 0 #ccc, 0 5px 0 #ccc, 0 6px 0 #ccc, 0 7px 0 #ccc, 0 8px 0 #ccc, 0 9px 0 #ccc, 0 10px 0 #ccc, 0 11px 0 #ccc, 0 12px 0 #ccc, 0 20px 30px rgba(0, 0, 0, 0.5), 0 0 7px #fff, 0 0 10px #fff, 0 0 21px #fff, 0 0 42px #0fa, 0 0 82px #0fa, 0 0 92px #0fa, 0 0 102px #0fa, 0 0 151px #0fa;
    color: #fff;
}

.pg:hover,
.left-col:hover>.heading-phone span,
.right-col:hover>h3 {
    font-size: 2.5vw;
}

 .logo {
    color: #fff;
    font-weight: bold;
    text-shadow: 3px 3px blue;
    -webkit-text-stroke: 0.1px darkblue;
    animation: colorchanger 1s infinite alternate-reverse;
  }

  @keyframes colorchanger {
    0%{
      text-shadow: 3px 3px blue;
    }
    100% {
      text-shadow: 0 1px 0 #ccc, 0 2px 0 #ccc, 0 3px 0 red,  0 1px 1px rgba(0, 0, 0, 0.5), 0 0 2px #fff, 0 0 3px red;
    }
  }
</style>"""


def home_page():
    selected = option_menu(None, ['About Dev', 'About Project'],
                           icons=['person-fill', 'info-lg'], menu_icon="cast", default_index=0,
                           orientation='horizontal')

    if selected == "About Dev":
        md_runner("""""")
        md_runner(text)

    else:
        md_runner("""
<h1> Campus Placement Predictor</h1>
<p>Our AI-powered Placement Predictor App, developed using Python and Machine Learning, is designed to help individuals unlock their career potential. The app analyzes various data points such as academic performance, work experience, and skills to predict the likelihood of success in a particular job or industry.</p>

<p>The app's user-friendly interface makes it easy to input your information and receive instant feedback. Whether you're a recent graduate or a seasoned professional looking to switch careers, our Placement Predictor App provides valuable insights to guide you towards success.</p>

<b><p> Want to contribute or provide any feedback ? Write us at <a href="mailto:ddhruvarora2@gmail.com">gmail</a></p></b>


                  """)
