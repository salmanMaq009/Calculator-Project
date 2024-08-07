import streamlit as st

st.title("Simple Calculator")

# User input for the two numbers
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# User input for the operation
operation = st.selectbox("Choose operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation
result = None
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
if result is not None:
    st.write(f"The result of {operation} is: {result}")
