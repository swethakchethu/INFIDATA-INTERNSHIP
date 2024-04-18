import streamlit as st
st.title("arithmatic operation")
st.markdown("please give the input")

st.sidebar.title("select the operation")
st.sidebar.markdown("select the options accordingly:")

choice = st.sidebar.selectbox("select",('add','mul'))
selcted_status=st.sidebar.selectbox('select number',opotions=['2N','3N'])

if choice='add':
    if selcted_status=='2N':
        n1=st.number_input("enter n1:")
        n2=st.number_input("enter n2:")
        sum=n1+n2
        st.success(sum)
elif selcted_status=='3N':
    n1 = st.number_input("enter n1:")
    n2 = st.number_input("enter n2:")
    n3=  st.number_input("enter n3:")
    sum = n1 + n2 +n3
    st.success(sum)
elif choice=='mul':
    if selcted_status=='2N':
        n1 = st.number_input("enter n1:")
        n2 = st.number_input("enter n2:")
        mul = n1 + n2
        st.success(mul)