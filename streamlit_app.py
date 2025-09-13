import streamlit as st

# Make About the landing page
try:
    st.switch_page("pages/1_About.py")
except Exception:
    # Fallback if older Streamlit: simple links
    st.set_page_config(page_title="Portfolio", page_icon="🤖", layout="wide")
    st.title("AI/ML Portfolio")
    st.warning("If you see this, your Streamlit version may not support st.switch_page. "
               "Use the sidebar to open 'About', or upgrade Streamlit.")
    st.page_link("pages/1_About.py", label="Go to About / Intro", icon="👋")
