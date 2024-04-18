import streamlit as st
from PIL import Image
img1=Image.open('img.png')
st.title('DISPLAYING IMAGE')
st.header("BUNNY")
st.image(img1,width=500)
img2=Image.open('img_1.png')
st.image(img2,width=500)
st.subheader("AA")