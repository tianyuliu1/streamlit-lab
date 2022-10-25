import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Tianyu Liu')
df = pd.read_csv('housing.csv')
price_filter = st.slider('Median House Price', 0.0, 500001.0, 1000.0)  

ocean_proximity_filter = st.sidebar.multiselect(
     'ocean_proximity Selector',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())  

form = st.sidebar.form("country_form")
country_filter = form.radio('choose input level', ('Low','Medium','High'))
form.form_submit_button('submit')

df = df[df.median_house_value <= price_filter]
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]
if country_filter == 'Low':
    df = df[df.median_income<=2.5]
elif country_filter == 'Medium':
    df = df[(df.median_income>=2.5)&(df.median_income<=4.5)]
else:
    df = df[df.median_income>=4.5]
st.subheader('See more filters in the sidebar :')
st.map(df)


st.subheader('Histogram of the Median House Value :')
fig, ax = plt.subplots(figsize=(15, 15))
a = df
a.median_house_value.hist(bins=30)
st.pyplot(fig)