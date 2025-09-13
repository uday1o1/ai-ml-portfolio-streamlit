import os
import streamlit as st
from pathlib import Path

ICONS_PATH = Path("assets/icons")

def render_skills(cols: int = 5):
    """Render skills as a grid of images from assets/icons/"""
    if not ICONS_PATH.exists():
        st.warning("⚠️ Add your skill icons into `assets/icons/`")
        return

    files = sorted([f for f in ICONS_PATH.iterdir() if f.suffix.lower() in [".png", ".jpg", ".jpeg", ".svg"]])
    if not files:
        st.info("No icons found in `assets/icons/`.")
        return

    st.subheader("Skills")
    grid = st.columns(cols)
    for i, f in enumerate(files):
        with grid[i % cols]:
            st.image(str(f), width="content")

