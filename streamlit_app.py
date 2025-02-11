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

# withd and height of the page
import streamlit as st

# title in the center of the page
st.title('Report')
st.divider()
st.header('Operation PnL')
st.subheader('Period: 2025-01-01 to 2025-01-31')
# create a blank line
st.write('')
st.write("Here's our first attempt at using data to create a table:")

def df():
    # create a dataframe with 5 columns and 10 rows
    return pd.DataFrame({
        'first column': list(range(1, 11)),
        'second column': list(range(11, 21)),
        'third column': [""] * 10,
        'fourth column': list(range(31, 41)),
        'fifth column': list(range(41, 51))
    }, index=list('abcdefghij'))
    
# divide the screen into two parts
# left_column, right_column = st.columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     left_column.write("Woohoo!")
# else:
#     left_column.write("Press the button")

# expander = st.expander("FAQ")

# expander.write("Here you could put in some really, really long explanations...")
# value = ('Email', 'Home phone', 'Mobile phone', 'Pager', 'Fax')
# right_column.selectbox('How would you like to be contacted?', value)

# multi = right_column.multiselect('Where are you now?', ['Home', 'Office', 'Remote'])

# set style for the dataframe: add color to the cells
df1 = (df()
    .style.bar(subset=['first column', 'second column'], color='red')
    .applymap(lambda x: 'color: red' if x > 35 else '', subset='fourth column')
    # hide index of the dataframe
    
    
)

# set percentage format for the dataframe
# df1 = df1.style.format("{:.2%}")

st.table(df1)

# df1 = df().style.bar(subset=['first', 'second'], color='#d65f5f', width=100)

st.dataframe(df1, hide_index=True, )


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