import streamlit as st
from menu import menu_with_redirect


st.title("Admin Panel")
st.markdown("This is the admin panel of our app. Here you can manage users, view logs, and more.")

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")