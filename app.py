import streamlit as st

st.title("Hello, This is a Streamlit App!")
st.write("This is a simple example of a Streamlit application.")

name = st.text_input("Enter the name ")

if name:
    st.write("Hello",name)
    if st.button("Click Me"):
       st.write("Button Clicked!")

    option = st.selectbox("Choose an option", ["Option 1", "Option 2","Option 3"])
    st.write("You selected:",option)