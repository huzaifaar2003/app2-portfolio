import streamlit as st
import pandas as pd
import time


col1, col2 = st.columns([1.5,2]) #rezised columns

with col1:
    st.image("images/HAR_photo.jpg")

with col2:
    st.title("Huzaifa Abdul Rab")
    content ="""Hi! Hope you're having a great day! Huzaifa Abdul Rab here. 
    I'm a 2025 Mechatronics Engineering Graduate from NUST. 
    Gradually shifting from Mechatronics to the Fields of Data In Sha Allah, I've started by learning Python.
    Join me on my learning journey!  
    """
    # """...""" for multiline (dynamically and automatically sizing) string.
    st.info(content)

content2 = """<i><h3>Here are some of my Python projects. Feel free to view them below!</h3></i>"""
st.write(content2,
         unsafe_allow_html=True)

df = pd.read_csv("data.csv", sep=";")


col3, empty_col, col4 = st.columns([1.5,0.75,1.5]) #Added empty column for "padding"

with col3:
    for index, row in df[:10].iterrows():
        st.header(f"{index+1} - {row["title"]}")
        st.subheader(row["description"])
        st.write(f"[Source Code]({row["url"]})")
        #st.write(f"[Text to be displayed](link to be embedded)")
        st.image(f"images/{row["image"]}")
        st.write("___")
        #"___" (and any more underscores "_") makes a horizontal line across the column


with col4:
    for index, row in df[10:].iterrows():
        st.header(f"{index+1} - {row["title"]}")
        st.subheader(row["description"])
        st.write(f"[Source Code]({row["url"]})")
        st.image(f"images/{row["image"]}")
        st.write("__________", font="Helvetica")
