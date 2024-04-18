import streamlit as st
import pandas as pd
import plotly.graph_bjects as go

st.title("Smock Prediction Dashboard")
st.markdown("the dashboard will healp a reseacher to get to know \
            more about the given data set and its output")

#side bar
st.sidebar.title("select visual charts")
st.sidebar.markdown("select the charts/plots accordingly:")

data=pd.read_csv("demo_data_set.csv")

chat_visual=st.sidebar.selectbox("select chats/plots type",("line chart","bar chart","bubble chart"))

st.sidebar.checkbox("show analyse by amooking status",true,key=1)
selected_status=st.sidebar.selectbox("select smoking status",
                                     options=["formely_smoked","smoked","never smoked","unknown"])
fig = go.Figure()
if chart_visual == 'LineChart':
    if selected_status == 'Formely_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formely_Smoked,
                                 mode='Lines',
                                 name='Formerly_Smoked'))
    elif selected_status == 'Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formely_Smoked,
                                 mode='Lines',
                                 name='Smoked'))
    elif selected_status == 'Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formely_Smoked,
                                 mode='Lines',
                                 name='Never_Smoked'))
    elif selected_status == 'Unknow':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formely_Smoked,
                                 mode='Lines',
                                 name='Unknow'))
st.plotly_chart(fig3)



