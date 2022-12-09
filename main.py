import streamlit as st
import pandas as pd
st.write("PROVA RPE")

number = st.number_input('Insert a number')
st.write('The current number is ', number)


#st.write("Here's our first attempt at using data to create a table:")
#df = pd.DataFrame({
    #'first column': [1, 2, 3, 4],
    #'second column': [10, 20, 30, 40]
#})
#st.write(df)
#st.bar_chart(df)'''
