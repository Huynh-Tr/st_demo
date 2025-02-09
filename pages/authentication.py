import streamlit as st

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if not st.session_state.logged_in:
#     st.write("Please log in.")
#     with st.form("login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         submitted = st.form_submit_button("Log In")

#     if submitted:
#         # Replace this with your actual authentication logic
#         if username == "test" and password == "password":  # Example (insecure!)
#             st.session_state.logged_in = True
#             st.experimental_rerun()  # Refresh the page
#         else:
#             st.error("Invalid username or password.")

# else:  # User is logged in
#     st.write(f"Welcome, {username}!")  # Or get the user's name from your system
#     #... your app logic for logged-in users...

#     if st.button("Log Out"):
#         st.session_state.logged_in = False
#         st.experimental_rerun()  # Refresh the page

import streamlit as st

if st.experimental_user.is_logged_in:
    st.write(st.experimental_user)
