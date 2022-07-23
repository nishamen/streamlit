import streamlit as st

st.title('Addition App')

st.header('User Input Parameters')
number1= st.number_input("Number1",min_value=0,max_value=20000,step=1)
number2= st.number_input("Number2",min_value=0,max_value=20000,step=1)

if(number1 !=0 and number2!=0):
	st.header('Result')
	st.write(number1+number2)
