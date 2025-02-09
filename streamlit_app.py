import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

st.title('My first app2124')
st.write("Here's our first attempt at using data to create a table:")
# st.markdown
# st.header
# st.subheader
# st.caption
# st.text
# st.latex
# st.code

st.button('Say hello')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

st.write('Below is a df', df, 'Above is a df')

df2 = pd.DataFrame({
    'first column': ['a', 'b', 'c', 'd'],
    'second column': [10, 20, 30, 40],
    'third column': [100, 200, 300, 400]
    })

# create a plot to show on streamlit
fig, ax = plt.subplots()
ax.plot(df2['first column'], df2['second column'])
st.pyplot(fig)

# create a plot by pandas to show on streamlit
fig2 = df2.plot(x='third column', y='second column')
st.pyplot(fig2.figure)


# create a table to show on streamlit, with the red header, total row and column blue font
df3 = df2.copy()
df3.set_index('first column', inplace=True)
df3.loc['Total'] = df3.sum()
df3['Total'] = df3.sum(axis=1)
st.table(df3.style.set_table_styles(
    [{'selector': 'th', 'props': [('background', 'red'), ('color', 'black')]},
     {'selector': 'td', 'props': [('color', 'blue')]}
    ]))


st.code('''
def hello():
    print('Hello, Streamlit!')
''')
