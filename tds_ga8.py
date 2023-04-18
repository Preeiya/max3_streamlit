import streamlit as st

def find_largest_number(num1, num2, num3):
    largest_num = max(num1, num2, num3)
    return largest_num

# Streamlit app
def app():
    st.title("Find the Largest Number")
    st.write("Enter three numbers and find the largest among them.")

    num1 = st.number_input("Enter Number 1", step=1)
    num2 = st.number_input("Enter Number 2", step=1)
    num3 = st.number_input("Enter Number 3", step=1)

    if st.button("Find Largest"):
        largest_num = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest_num}")
 st.run tds_ga8.py
