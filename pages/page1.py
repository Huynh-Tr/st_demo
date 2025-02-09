import streamlit as st

hide_st_style = """ 
<style>
    #MainMenu{visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True) 

# Rest of your Streamlit app code

st.title("😂 Ahixahaaa")

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
