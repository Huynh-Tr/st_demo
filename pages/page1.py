import streamlit as st

st.markdown(
    """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > header > div.stAppToolbar.st-emotion-cache-15ecox0.e4hpqof2 {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Rest of your Streamlit app code

st.title("😂 Ahixahaaa 12332231 ê")

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
