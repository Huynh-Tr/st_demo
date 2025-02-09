import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_all_icon = """
#MainMenu {
  visibility: hidden;
}
"""
st.markdown(hide_all_icon, unsafe_allow_html=True)

st.title("😂")

st.header("st.button")

if st.button("😅 Say hello"):
    st.write("Hello, world!")
else:
    st.write("Goodbye, world!")


st.markdown('$$ n_1 = n^1 + 1 $$')
st.code('''
    def hello():
        print('some things')    
''')
