import streamlit as st
import pandas as pd
on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")

st.write("HIIIII")

color = st.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
st.write("My favorite color is", color)

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    value=("red", "blue"))
st.write("You selected wavelengths between", start_color, "and", end_color)

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe