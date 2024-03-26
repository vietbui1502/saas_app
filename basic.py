import streamlit as st

st.title("Streamlit Session Demo")

st.sidebar.header("Options")

slider_val = st.slider('Choose a value', min_value=1, max_value= 200, value=25)
st.write(f"You selected {slider_val} using the slider.")

if st.sidebar.checkbox("Show more information"):
    st.write("This is some additional info displayed based on checkbox choice!")

option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option3"])
st.write(f"You selected: {option}")

date = st.sidebar.date_input("Pick a date")
st.write(f"Selected Date: {date}")


# Multi page layout using ratio button
page = st.radio("Choose a page: ", ["Home", "About", "Contact"])
if page == "Home":
    st.write("Welcome to Home Page")
elif page == "About":
    st.write("This is about Session")
else:
    st.write("Feel free to contact us")

# Using st.session_state for single counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment = st.button('Counter')
if increment:
    st.session_state.counter +=1

st.write(f"Counter Value: {st.session_state.counter}")
