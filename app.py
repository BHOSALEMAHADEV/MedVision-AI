import streamlit as st
from config import *
import database
from src.auth import login, logout

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load CSS
# ==========================================================

def load_css():

    try:

        with open(
            "assets/css/style.css",
            "r",
            encoding="utf-8"
        ) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


load_css()

# ==========================================================
# Session State
# ==========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = ""

if "user_role" not in st.session_state:
    st.session_state.user_role = "Medical Professional"

# ==========================================================
# Login
# ==========================================================

if not st.session_state.logged_in:
    login()
    st.stop()

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title(APP_NAME)

    st.caption(TAGLINE)

    st.success(st.session_state.user_role)

    st.write("--------------------------------")

    menu = st.radio(

        "Navigation",

        [

            "Dashboard",

            "Patient Management",

            "Medical Image Upload",

            "Blood Cell Analyzer",

            "Lung CT Analyzer",

            "Brain MRI Analyzer",

            "Retinal Disease Analyzer",

            "Histopathology Analyzer",

            "Analytics",

            "Settings"

        ]

    )

    st.write("--------------------------------")

    st.info(f"Version : {VERSION}")

    logout()

# ==========================================================
# Dashboard
# ==========================================================

if menu == "Dashboard":

    st.title("Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Patients", "0")
    c2.metric("Reports", "0")
    c3.metric("AI Accuracy", "--")
    c4.metric("Modules", "5")

    st.divider()

    st.success("Welcome to MedVision AI")

    st.write(
        """
This platform provides AI-powered medical image analysis.

Available modules

• Blood Cell Analyzer

• Lung CT Analyzer

• Brain MRI Analyzer

• Retinal Disease Analyzer

• Histopathology Analyzer
"""
    )

# ==========================================================
# Patient Management
# ==========================================================

elif menu == "Patient Management":

    with open(
        "pages/patients.py",
        "r",
        encoding="utf-8"
    ) as file:

        exec(file.read())

# ==========================================================
# Medical Image Upload
# ==========================================================

elif menu == "Medical Image Upload":

    with open(
        "pages/upload.py",
        "r",
        encoding="utf-8"
    ) as file:

        exec(file.read())

# ==========================================================
# Blood Cell Analyzer
# ==========================================================

# ==========================================================
# Blood Cell Analyzer
# ==========================================================

elif menu == "Blood Cell Analyzer":

    with open(
        "pages/blood_analyzer.py",
        "r",
        encoding="utf-8"
    ) as file:

        exec(file.read())

# ==========================================================
# Lung CT Analyzer
# ==========================================================

elif menu == "Lung CT Analyzer":

    st.header("Lung CT Analyzer")

    st.info("Coming in Module 5")

# ==========================================================
# Brain MRI Analyzer
# ==========================================================

elif menu == "Brain MRI Analyzer":

    st.header("Brain MRI Analyzer")

    st.info("Coming in Module 4")

# ==========================================================
# Retinal Disease Analyzer
# ==========================================================

elif menu == "Retinal Disease Analyzer":

    st.header("Retinal Disease Analyzer")

    st.info("Coming in Module 6")

# ==========================================================
# Histopathology Analyzer
# ==========================================================

elif menu == "Histopathology Analyzer":

    st.header("Histopathology Analyzer")

    st.info("Coming in Module 7")

# ==========================================================
# Analytics
# ==========================================================

elif menu == "Analytics":

    st.header("Analytics")

    st.info("Coming Soon")

# ==========================================================
# Settings
# ==========================================================

elif menu == "Settings":

    st.header("Settings")

    st.info("Coming Soon")

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    f"{APP_NAME} | Version {VERSION} | Developed by {AUTHOR}"
)