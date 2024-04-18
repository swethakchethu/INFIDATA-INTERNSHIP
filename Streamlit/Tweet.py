import streamlit as st
st.sidebar.title("reg form")
with st.form(key='form1'):
    with st.sidebar:

        user_word=st.text_input("enter a keyword")
        select_language=st.radio ("Tweet language",('all',"english","hindi"))
        include_retweets=st.checkbox("include retweets in data")
        num_of_tweets= st.number_input("minimum no of tweets",100)
        submitted1 = st.form_submit_button(label='Search twitter')
st.write("Keyword is:",user_word)
st.write("language is:",select_language)
