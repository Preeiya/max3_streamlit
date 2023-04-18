import streamlit as st

def find_largest(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    return largest

st.title('Largest of 3 numbers')

num1 = st.number_input('Enter the first number',step=1)
num2 = st.number_input('Enter the second number',step=1)
num3 = st.number_input('Enter the third number',step=1)

if st.button('Find Largest'):
    largest =find_largest(num1, num2, num3)
    st.write(f'The largest number is: {largest}',format='%d')
