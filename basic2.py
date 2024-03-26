import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Title of our app
st.title("Data Display with Streamlit")

#Create a sample Dataframe
data = {
    'A': np.random.randn(50),
    'B': np.random.randn(50),
    'C': np.random.randn(50)
}

df = pd.DataFrame(data)

#Display a table with Streamlit
st.header("Display a table in streamlit")
st.table(df.head(10))

#Displaying a DataFrame with Streamlit (more interactive than table)
st.header("Display DataFrame in Streamlit")
st.write(df.head(10))

#Using line_chart to visualize the data
st.header("Using Built-in line Chart")
st.line_chart(df)

# Displaying dynamic content
st.header("Dynamic Content: Markdown, Images and Videos")
st.markdown("This is  **Markdown** in action in Streamlit")

st.image("https://media.baodautu.vn/Images/huutuan/2024/02/29/Bitcoin.jpg", caption="Bitcoin")

st.video("https://www.youtube.com/watch?v=hhzCeqyUlJ8")