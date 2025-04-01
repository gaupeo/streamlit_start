import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

import streamlit as st

st.title("Interactive Streamlit App")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")

if st.button("Click Me"):
    st.write("You clicked the button!")


import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Data Visualization")

# Generate random data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(data)