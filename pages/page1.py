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
footer="""

<style> your css code put here</style>

<div class='footer'>

<p>the word you want to tell<a style='display:block;text-align:center;' 

href='https://www.streamlit.io' target='_blank'>your email address put here</a></p>

</div>"""

st.markdown(footer, unsafe_allow_html=True)
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
