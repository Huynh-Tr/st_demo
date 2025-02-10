import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Hide the Streamlit menu
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

# Hide sidebar
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

st.markdown(
    """
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > section.stSidebar.st-emotion-cache-vmpjyt.e1c29vlm0 > div.st-emotion-cache-6qob1r.e1c29vlm8 {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App
st.title('My first app')
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

# create a table to show on streamlit, with the red header, total row and column blue font
df3 = df2.copy()
df3.set_index('first column', inplace=True)
df3.loc['Total'] = df3.sum()
df3['Total'] = df3.sum(axis=1)
st.table(df3.style.set_table_styles(
    [{'selector': 'th', 'props': [('background', 'red'), ('color', 'black')]},
     {'selector': 'td', 'props': [('color', 'blue')]}
    ]))

# create a line chart
chart_data = pd.DataFrame(
    [[1, 2], [2, 3], [3, 6], [4, 8]],
    columns=['x', 'y']
    )
st.line_chart(chart_data)

# use matplotlib to create a chart
chart_data = pd.DataFrame(
    [[1, 2], [2, 3], [3, 6], [4, 8]],
    columns=['x', 'y']
    )
fig, ax = plt.subplots()
ax.plot(chart_data['x'], chart_data['y'])
st.pyplot(fig)

st.code('''
def hello():
    print('Hello, Streamlit!')
''')

st.markdown('''
    $$n^1$$
''')
