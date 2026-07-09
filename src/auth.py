import streamlit as st
from database import cursor

# -------------------------------------------------------
# Login Function
# -------------------------------------------------------

def login():

    st.title("🔐 User Login")

    st.markdown("### Welcome to MedVision AI")
    st.write("Please sign in to continue.")

    username = st.text_input("Username")

    password = st.text_input("Password", type="password")

    remember = st.checkbox("Remember Me")

    login_button = st.button("Login", use_container_width=True)

    if login_button:

        if username == "" or password == "":
            st.warning("Please enter both username and password.")
            return

        cursor.execute(
            """
            SELECT * FROM users
            WHERE username=? AND password=?
            """,
            (username, password)
        )

        user = cursor.fetchone()

        if user:

            st.session_state.logged_in = True
            st.session_state.user_id = user[0]
            st.session_state.username = user[1]
            st.session_state.user_role = user[3]

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error("Invalid username or password.")

# -------------------------------------------------------
# Logout Function
# -------------------------------------------------------

def logout():

    if st.sidebar.button("🚪 Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.username = ""
        st.session_state.user_role = ""

        st.success("Logged out successfully.")

        st.rerun()