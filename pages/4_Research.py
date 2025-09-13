import streamlit as st
from components.nav import top_nav
top_nav(active="Research")


st.set_page_config(page_title="Research Contributions — Uday", page_icon="📄", layout="wide")

st.title("Research Contributions")

# ---- Publications ----
st.subheader("Publications")

st.markdown("""
**Performance Analysis of Detection Models for Depth-Aware Robotic Cleaning Systems**  
*Submitted to IEEE Access, Under Review (2025)*  

Presents a comparative study of computer vision models for depth-aware robotic cleaning, evaluating detection performance and system integration for autonomous operation.
""")

# ---- Talks & Posters (optional) ----
#st.subheader("Talks & Posters")
#st.write("Add here if you give a seminar, workshop, or conference poster 📌.")
