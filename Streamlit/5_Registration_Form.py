import datetime

import streamlit as st
st.header("student registration form")
my_form=st.form(key="form-1")
fname=my_form.text_input("student first name")
lname=my_form.text_input("student last name")
email=my_form.text_input("student email")
mobile=my_form.text_input("student number")
gender=my_form.radio('gender',('male','female'))
age=my_form.slider("age",1,100)
dob=my_form.date_input('enter date of birth',min_value=datetime.date(1990,1,1))
addr=my_form.text_area("enter address")
ressume=my_form.file_uploader("upload you r ressume")
my_form.form_submit_button("submit")

st.write("first name:",fname)
st.write("last name:",lname)
st.write("email:",email)
st.write("number:",mobile)
st.write("gender:",gender)
st.write("age:",age)
st.write("address:",addr)