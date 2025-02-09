import streamlit as st
import yagmail

# Store your Gmail credentials in Streamlit secrets for security
# secrets.toml:
# [gmail]
# user = "your_gmail_username@gmail.com"
# password = "your_gmail_app_password"  # Use an App Password!

if st.button("Send Email"):
    try:
        yag = yagmail.SMTP("huynh.gemini.0@gmail.com", "Android.123")
        yag.send(
            to="huynhvietjetair@gmail.com",
            subject="Test Email from Streamlit",
            contents="12345"
        )
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")