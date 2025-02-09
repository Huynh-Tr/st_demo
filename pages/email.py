import streamlit as st
import yagmail
import numpy as np

# Store your Gmail credentials in Streamlit secrets for security
# secrets.toml:
# [gmail]
# user = "your_gmail_username@gmail.com"
# password = "your_gmail_app_password"  # Use an App Password!
np.random.seed(0)
OTP = np.random.randint(1000,9999)
st.write(OTP)
if st.button("Send Email"):   
    try:
        yag = yagmail.SMTP(st.secrets["gmail"]["user"], st.secrets["gmail"]["password"])
        yag.send(
            to="huynhvietjetair@gmail.com",
            subject="Test Email from Streamlit",
            contents=f'{OTP}'
        )
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

OTP_check = st.text_input('OTP')
st.write(OTP_check)
if int(OTP_check) == OTP:  
    st.write('right')
else:
    st.write(f'{OTP}')

