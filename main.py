import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_btc.sav', 'rb'))

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
       
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction'])
if app_mode=='Home':
    st.title('BTC/USDT Price Prediction :')
    st.image('btc.jpg') 
    st.markdown('Dataset :')
    data = pd.read_csv('BTCUSDT-1Month.csv')
    st.write(data.head())
    st.markdown('open VS close')
    st.bar_chart(data[['open','close']].head(20))


elif app_mode == 'Prediction':
    st.title('Prediksi Harga BTC/USDT')

st.header("Dataset")
#open file csv
df1 = pd.read_csv('BTCUSDT-1d.csv')
st.dataframe(df1)

df4 = pd.read_csv('BTCUSDT-1Month.csv')
st.dataframe(df4)

df5 = pd.read_csv('BTCUSDT-1w.csv')
st.dataframe(df5)

df6 = pd.read_csv('BTCUSDT-2h.csv')
st.dataframe(df6)

df9 = pd.read_csv('BTCUSDT-4h.csv')
st.dataframe(df9)


st.write("Grafik Open")
chart_open = pd.DataFrame(df1, columns=["open"])
st.line_chart(chart_open)

st.write("Grafik Close")
chart_close = pd.DataFrame(df1, columns=["close"])
st.line_chart(chart_close)

st.write("Grafik Volume")
chart_volume = pd.DataFrame(df1, columns=["volume"])
st.line_chart(chart_volume)

open = st.number_input('open:', min_value=0)
close = st.number_input('close:', min_value=0)
volume = st.number_input('volume:', min_value=0)

if st.button('Prediksi'):
    btc_prediction = model.predict([[open, close, volume]])
    
    # convert float to string
    harga_btc_str = np.array(btc_prediction)
    harga_btc_float = float(harga_btc_str[0][0])
    harga_btc_formatted = f'Harga Btc $ {harga_btc_float:,.2f}'

    st.write(harga_btc_formatted)
