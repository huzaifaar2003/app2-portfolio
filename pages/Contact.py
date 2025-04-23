import streamlit as st


st.title("Contact Me")

with st.form(key="input_form"):
    st.text_input("Your email address", placeholder="someone@something.com", key= "form_email")

    st.text_area("Your message", key= "form_message")

    submitted = st.form_submit_button("Submit")
