import streamlit as st
import pandas as pd

st.write("""
# Largest of Three Numbers
This app finds the largest number of the given three numbers
""")

#Get Input

st.header('User Input Parameters')

def user_input_features():
        Number_1 = st.number_input('NUMBER_1',min_value= 0 , max_value= 10000000000)
        Number_2 = st.number_input('NUMBER_2',min_value= 0 , max_value= 10000000000)
        Number_3 = st.number_input('NUMBER_3',min_value= 0 , max_value= 10000000000)
        data = {'NUMBER_1' : Number_1,
                'NUMBER_2' : Number_2,
                'NUMBER_3' : Number_3}
        features = pd.DataFrame(data,index=[0])
        return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

def Largest(data):
    a = data.iloc[0]['NUMBER_1']
    b = data.iloc[0]['NUMBER_2']
    c = data.iloc[0]['NUMBER_3']
    if a>b:
        if a>c:
            return a
        elif c>b:
            return c
    elif b>a:
        if b>c:
            return b
        elif c>b:
            return c

st.subheader('The Largest of the Three Numbers is')
st.write(Largest(df))