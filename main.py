import streamlit as st
import pandas as pd
from datetime import date
import os
import requests

today = date.today()
# dd/mm/YY
t_date = today.strftime("%d/%m/%Y")

url = "https://raw.githubusercontent.com/elrampa92/first_try_streamlit/main/db_RPE.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

#df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#df_excel = pd.DataFrame(columns=['Player', 'Data', 'RPE'])

#os.makedirs('/Users/elrampa/Desktop/prova_streamlit/data', exist_ok=True)
#df_excel.to_excel('/Users/elrampa/Desktop/prova_streamlit/data/DF_RPE.xlsx', index = False)


#df["data"] = pd.to_datetime(df.data)
#df['data'] = df['data'].dt.strftime('%m/%d/%Y')


st.title("RPE PAGE")
from PIL import Image
#image = Image.open('https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/2022_Venezia_FC_logo.svg/800px-2022_Venezia_FC_logo.svg.png')
#st.image(image, width=130)
st.text("Insert your RPE value")


#col1, col2, col3 = st.columns(3)


sel_player = st.selectbox(
        "Who are you?",
        ('BADOUIN NOAH','BORECKI KRYSTIAN','BOUDRI AMIN','BUSATO LORENZO','CAMBER DAVID','CAMOLESE NICOLA',
         'DA POZZO LORENZO','ENEM JAY','IVARSSON ISAK','JONSSON KRISTOFER','KARAGIANNIDIS GEORGIOS',
         'KYVIK LEO', 'MAGNUSSON ARON','MAKADJI MORRE','MIKAELSSON HILMIR','MOZZO FILIPPO','OKORO ALVIN OBINHA',
         'REMY MELVIN','RODRIGUES ALVES JAMES','SALVADOR TOMMASO','SANDBERG GABRIEL','SLOWIKOWSKI ERIK',
         'SPERANDIO TOMMASO','VELCEA VALENTIN')
)
sel_date = st.date_input(
        "Training session date",)
sel_session = st.radio(
        "Select the session",
        options=["Morning", "Afternoon"],
)
st.write("Today is: ",t_date)


rpe = st.selectbox(
        'Rate effort of the session',
        (0, 0.3, 0.5, 0.7, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10, 11), index = 8)
#    rpe = st.slider('Rate effort of the session', 0, 10, 3)
#    st.write("RPE value",rpe)
b_confirm = st.button(label ='Confirm!')
if b_confirm:
    #st.write(sel_player,"- RPE:", rpe,"during ",sel_session," session on", sel_date)
    new_row = {'Player':sel_player, 'Data':f'{sel_date} - {sel_session}', 'RPE':rpe}
    #st.write(new_row)
    #df_rpe = pd.read_excel('https://github.com/elrampa92/first_try_streamlit/blob/main/DF_RPE.xlsx?raw=true')
    #df_rpe = df_rpe.append(new_row, ignore_index=True)
    #df_rpe.to_excel('https://github.com/elrampa92/first_try_streamlit/blob/main/DF_RPE.xlsx?raw=true', index = False)
    df_RPE = pd.read_csv(url)
    df_RPE = df_RPE.append(new_row, ignore_index=True)
    df_RPE.to_csv(url, index = False)
    st.write(df_RPE)



    #df_rpe.insert(f"{sel_date}_{sel_session}")

    #df['gioc1'][0] = rpe

#print(df_rpe.loc[0])
#st.write(df_rpe)
#print(sel_player," ", sel_date, "", rpe, "", sel_session)

#print(df)

