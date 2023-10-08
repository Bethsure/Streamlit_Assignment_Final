import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
st.title('Distribution of ATC Telecommunication Towers across Kenya')
file_path = 'C:/Users/Betty.Ogato/OneDrive - American Tower/Betsy/Betty Ogato Files/Betsy Personal Work/Data Science Course/My_Final_Project.csv'
df = pd.read_csv(file_path)
st.dataframe(df)
import matplotlib.pyplot as plt
file_path = 'C:/Users/Betty.Ogato/OneDrive - American Tower/Betsy/Betty Ogato Files/Betsy Personal Work/Data Science Course/My_Final_Project.csv'
df = pd.read_csv(file_path)
df
df.plot(x="Longitude", y="Latitude", kind="scatter", color="blue")
st.header ('Map Showing the Distribution of ATC Sites')
st.write('The Below Scatter map of Telecommunication shows that the higher the population distribution, the more the number of Telecommunication Towers.The most numebr of Telecommunication Towers are located in Naiorbi and this can be attributed to the high population in the city as compared to Wajir County whose population is scattered. The vast number of facilities in the city attracts a huge population from all over the country (Kenya)')
fig=px.scatter(df, x="Longitude", y="Latitude")
st.plotly_chart(fig)
import matplotlib.pyplot as plt
st.header ('Graph showing Number of Telecommunication Towers Per County')
fig2=px.bar(df['County'].value_counts())
st.plotly_chart(fig2)
import pandas as pd
import plotly.express as px
st.header ('Table Showing Total Population Per County')
file_path = 'C:/Users/Betty.Ogato/OneDrive - American Tower/Betsy/Betty Ogato Files/Betsy Personal Work/Data Science Course/Kenya Population 2019.csv'
df = pd.read_csv(file_path)
df
