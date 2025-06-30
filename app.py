import streamlit as st

#streamlit UI
st.title("Power Calculator")
st.write(" enter a number to calculate its square, cube, and fifth power")

#get user input
n=st.number_input("enter an integer",value=1,step=1)

#calculate result
square= n ** 2
cube= n**3
fifth_power= n**5

#display result
st.write(f"sqaure is:{square}")
st.write(f"cube is:{cube}")
st.write(f"fifth power is:{fifth_power}")