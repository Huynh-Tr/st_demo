import streamlit as st
import yagmail
import numpy as np

# Store your Gmail credentials in Streamlit secrets for security
# secrets.toml:
# [gmail]
# user = "your_gmail_username@gmail.com"
# password = "your_gmail_app_password"  # Use an App Password!

if st.button("Send Email"):
    OTP = np.ranndom.randint(1000,9999)
    try:
        yag = yagmail.SMTP(st.secrets["gmail"]["user"], st.secrets["gmail"]["password"])
        yag.send(
            to="huynhvietjetair@gmail.com",
            subject="Test Email from Streamlit",
            contents=OTP
        )
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")
