import streamlit as st
import pandas as pd
import time

col1, col2 = st.columns(2)

with col1:
    st.image("images/HAR_photo.jpg")

with col2:
    st.title("Huzaifa Abdul Rab")
    content ="""Hi! Hope you're having a great day! Huzaifa Abdul Rab here. I'm a 2025 Mechatronics Engineering Graduate from NUST. Gradually shifting from Mechatronics to the Fields of Data In Sha Allah.  
    """
    # """...""" for multiline (dynamically and automatically sizing) string.
    st.info(content)

content2 = """<i><h3>Here are some of my Python projects. Feel free to view them below!</h3></i>"""
st.write(content2,
         unsafe_allow_html=True)

df = pd.read_csv("data.csv", sep=";")


col3, col4 = st.columns(2)

with col3:
    for index, row in df[0:10].iterrows():
        st.subheader(row[0])

with col4:
    for index, row in df[10:20].iterrows():
        st.subheader(row[0])