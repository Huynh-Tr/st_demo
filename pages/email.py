import streamlit as st
import yagmail

# Store your Gmail credentials in Streamlit secrets for security
# secrets.toml:
# [gmail]
# user = "your_gmail_username@gmail.com"
# password = "your_gmail_app_password"  # Use an App Password!

if st.button("Send Email"):
    try:
        yag = yagmail.SMTP("huynh.gemini.0@gmail.com", "yarb qygv maio refe")
        yag.send(
            to="huynhvietjetair@gmail.com",
            subject="Test Email from Streamlit",
            contents="12345"
        )
        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# import streamlit as st
# import smtplib
# from email.mime.text import MIMEText

#... (Get your email server settings, username, password, etc.)...

# if st.button("Send Email"):
#     try:
#         msg = MIMEText("12345")  # Email content
#         msg['Subject'] = "Test Email from Streamlit"
#         msg['From'] = "your_email@example.com"  # Your email address
#         msg['To'] = "huynh@gmail.com"

#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Example for Gmail
#             smtp.login("huynh.gemini.0@gmail.com", "Android.123") # Or use app password
#             smtp.send_message(msg)

#         st.success("Email sent successfully!")
#     except Exception as e:
#         st.error(f"Error sending email: {e}")


# import streamlit as st
# import sendgrid
# from sendgrid.helpers.mail import Mail

#... (Get your SendGrid API key)...
