import streamlit as st
import pandas as pd
st.write("PROVA RPE")


from PIL import Image
image = Image.open("https://github.com/elrampa92/first_try_streamlit/blob/3f023c9ae83765254772d058c2fa1615add9b696/VFC_LOGO.png")
st.image(image)

number = st.number_input('Insert a number')
st.write('The current number is ', number)


#st.write("Here's our first attempt at using data to create a table:")
#df = pd.DataFrame({
    #'first column': [1, 2, 3, 4],
    #'second column': [10, 20, 30, 40]
#})
#st.write(df)
#st.bar_chart(df)'''
