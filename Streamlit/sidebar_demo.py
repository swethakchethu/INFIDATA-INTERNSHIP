import streamlit as st
add_selectbox =st.sidebar.selectbox(
    "how would be like to be contected?",
    ("email","home phone","mobile phone")

)

with st.sidebar:
    add_radio=st.radio(
        "choose a shipping method",
        ("standard (5-15 days)","express (2-15 days)")

    )
    name=st.text_input("enter costemer name")