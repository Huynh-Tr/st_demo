import streamlit as st


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("😂")

st.header("st.button")

if st.button("😅 Say hello"):
    st.write("Hello, world!")
else:
    st.write("Goodbye, world!")

st.markdown(r"$$n^1$$")
