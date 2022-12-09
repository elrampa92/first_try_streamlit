import streamlit as st
import pandas as pd
st.write("vediamo se vaaa")

st.write("proviamo")

st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.bar_chart(df)
