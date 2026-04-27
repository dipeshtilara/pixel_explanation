import streamlit as st
import os

st.set_page_config(
    page_title="Making Machines See — Class XII AI",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit UI elements for a professional, "handmade" feel
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        iframe { border: none; }
    </style>
""", unsafe_allow_html=True)

# Path to your uploaded HTML file
html_file = os.path.join(os.path.dirname(__file__), "ultimate_cv_learning.html")

try:
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Render the interactive notes
    st.components.v1.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("HTML file not found. Please ensure 'ultimate_cv_learning.html' is in the same directory.")
