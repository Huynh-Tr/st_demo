import streamlit as st
import yagmail
import numpy as np

# Store your Gmail credentials in Streamlit secrets for security
# secrets.toml:
# [gmail]
# user = "your_gmail_username@gmail.com"
# password = "your_gmail_app_password"  # Use an App Password!

# OTP = np.random.randint(1000,9999)

# st.write(OTP)
# if st.button("Send Email"):   
#     try:
#         yag = yagmail.SMTP(st.secrets["gmail"]["user"], st.secrets["gmail"]["password"])
#         yag.send(
#             to="huynhvietjetair@gmail.com",
#             subject="Test Email from Streamlit",
#             contents=f'{OTP}'
#         )
#         st.success("Email sent successfully!")
#     except Exception as e:
#         st.error(f"Error sending email: {e}")

# OTP_check = st.text_input('OTP', 0)

# if int(OTP_check) == OTP:  
#     st.write('right')
# else:
#     st.write(f'{OTP}')

# Initialize OTP in session state if it doesn't exist
if "otp" not in st.session_state:
    st.session_state.otp = None  # Start with no OTP

if "otp_generated" not in st.session_state:
    st.session_state.otp_generated = False # start with no OTP generated

if not st.session_state.otp_generated: # Only generate if OTP is not generated yet.
    OTP = np.random.randint(1000, 9999)
    # np.random.seed(0) # Keep seed for testing purpose. Remove it in production.
    st.session_state.otp = OTP  # Store OTP in session state
    # st.write(OTP)
st.write('fill out the email')
send_to_email = st.text_input()
if st.button("Send Email") and not st.session_state.otp_generated:  # Only send if OTP hasn't been sent.
    try:
        yag = yagmail.SMTP(st.secrets["gmail"]["user"], st.secrets["gmail"]["password"])
        yag.send(
            to=send_to_email,
            subject="OTP Test!",
            contents=f'{st.session_state.otp}'  # Use the stored OTP
        )
        st.success("Email sent successfully!")
        st.session_state.otp_generated = True # Mark as generated
    except Exception as e:
        st.error(f"Error sending email: {e}")

OTP_check = st.text_input('OTP', 0)

if st.session_state.otp is not None and int(OTP_check) == st.session_state.otp:
    st.write('Right')
elif st.session_state.otp is not None and int(OTP_check)!= st.session_state.otp and OTP_check!= '0': # Added this condition to avoid showing "wrong" immediately.
    st.write('Wrong')
