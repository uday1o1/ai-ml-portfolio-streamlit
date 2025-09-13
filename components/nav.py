# components/nav.py
import streamlit as st

def top_nav(active: str = ""):
    # Wide layout, hide sidebar
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    st.markdown("""
        <style>
          /* Hide sidebar + hamburger */
          [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }

          /* Sticky top bar */
          .topnav-wrap { position: sticky; top: 0; z-index: 999; backdrop-filter: blur(6px); }
          .topnav { padding: 10px 0 14px; border-bottom: 1px solid rgba(148,163,184,.25); }

          /* Make the row of buttons look like pills */
          .topnav .stButton>button {
            display: inline-flex; align-items: center; gap: 8px;
            padding: 8px 14px; border-radius: 9999px; font-weight: 600; font-size: .95rem;
            border: 1px solid rgba(148,163,184,.35); background: rgba(148,163,184,.08); color: inherit;
          }
          .topnav .stButton>button:hover { background: rgba(148,163,184,.15); }
          /* Active state */
          .topnav .active > button {
            border-color: rgba(99,102,241,.45); background: rgba(99,102,241,.18);
          }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="topnav-wrap"><div class="topnav">', unsafe_allow_html=True)

    cols = st.columns(5, gap="small")

    _nav_button(cols[0], "👋 About",      "pages/1_About.py",     active == "About")
    _nav_button(cols[1], "📦 Projects",   "pages/2_Projects.py",  active == "Projects")
    _nav_button(cols[2], "💼 Experience", "pages/3_Experience.py",active == "Experience")
    _nav_button(cols[3], "📄 Research",   "pages/4_Research.py",  active == "Research")
    _nav_button(cols[4], "✉️ Contact",    "pages/5_Contact.py",   active == "Contact")

    st.markdown('</div></div>', unsafe_allow_html=True)

def _nav_button(col, label: str, target: str, is_active: bool):
    # put button inside a column so the row is horizontal
    with col:
        # add an 'active' class to style the current page
        container_class = "active" if is_active else ""
        st.markdown(f'<div class="{container_class}">', unsafe_allow_html=True)
        if st.button(label, use_container_width=True):
            st.switch_page(target)
        st.markdown('</div>', unsafe_allow_html=True)
