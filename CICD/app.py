import streamlit as st 
st.title("Power Calculator")
st.write("Enter a Number to Calculate its Squuare, Cube and Fifth Power")

n=st.number_input("Enter an Integer",value=1,step=1)
square = n**2 
cube = n**3 
fifth_power = n ** 5 

st.write(f"The Square  of {n} is : {square}")
st.write(f"The Cube of {n} is : {cube}")
st.write(f"The Fifth Power of {n} is : {fifth_power}")