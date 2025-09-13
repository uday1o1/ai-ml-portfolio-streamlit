# pages/1_About.py
import glob
import os
import streamlit as st
from components.nav import top_nav
from components.skills import render_skills

# (Optional) keep per-page title/icon; nav sets layout + hides sidebar
st.set_page_config(page_title="About — Uday", page_icon="👋")
top_nav(active="About")

# ---------- THEME-AWARE + TIGHTER STYLES ----------
st.markdown("""
<style>
/* Reduce top padding a bit under the sticky nav */
.block-container { padding-top: 1.25rem; }

/* Hero */
.hero h1{
  font-size: clamp(2.2rem, 5vw, 4.0rem);
  line-height: 1.05; margin: 0 0 .6rem 0; font-weight: 800;
}
.hero .subhead{
  font-size: clamp(1.05rem, 2.1vw, 1.25rem);
  line-height: 1.6; opacity: .9; margin: 0 0 1.1rem 0; max-width: 68ch;
}

/* Profile image */
.profile img{ border-radius: 16px; box-shadow: 0 8px 30px rgba(0,0,0,.25); }
.profile .caption{ opacity:.75; font-size:.9rem; margin-top:.35rem; }

/* Optional skill logos strip (if you want a row under the hero) */
.skills-strip{ display:flex; flex-wrap:wrap; align-items:center; gap: 14px 18px; margin-top: 10px; }
.skills-strip img{ height: 38px; width:auto; display:block; opacity:.95; filter: saturate(1.05);
                   transition: transform .15s ease, opacity .15s ease; }
.skills-strip img:hover{ transform: translateY(-2px); opacity:1; }

/* Resume row styling */
.resume-row {
    display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;
}
.resume-btn {
    background-color: #2563eb;
    color: white !important;
    padding: 6px 14px;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    transition: background 0.2s ease;
}
.resume-btn:hover { background-color: #1e40af; }
</style>
""", unsafe_allow_html=True)

# ---------- HERO (center text + right photo) ----------
col_text, col_img = st.columns([2.2, 1.2], vertical_alignment="center")

with col_text:
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown("<h1>Hi, I’m Uday — I build practical AI/ML systems</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p class="subhead">Passionate about advancing ML and AI to build scalable, real-world solutions. '
        'Experienced across LLMs, predictive modeling, and intelligent agents — focused on turning ideas into impact.</p>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # icons = sorted(glob.glob("assets/icons/*.*"))
    # if icons:
    #     html = ['<div class="skills-strip">']
    #     for path in icons:
    #         html.append(f'<img src="{path}" alt="{os.path.basename(path)}"/>')
    #     html.append('</div>')
    #     st.markdown("\n".join(html), unsafe_allow_html=True)

with col_img:
    st.markdown('<div class="profile">', unsafe_allow_html=True)
    st.image("assets/profile.png", width="stretch")
    st.markdown('<div class="caption">Based in San Jose, California</div>', unsafe_allow_html=True)
    st.markdown('<div class="caption">Open to opportunities across the U.S.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# # ---- BIO
# st.subheader("About me")
# st.write(
#     "Short bio: what you work on, key interests (LLMs, CV, time series), "
#     "tooling you enjoy, and what you’re exploring next."
# )

# ---- SKILLS (images only, from assets/icons/)
render_skills(cols=5)

# ---- Resume Section (inline title + button)
st.markdown("""
    <div class="resume-row">
        <h3 style="margin:0;">Resume</h3>
        <a href="assets/resume.pdf" class="resume-btn" target="_blank" download>
            ⬇️ Download
        </a>
    </div>
""", unsafe_allow_html=True)

# ---- CONTACT QUICK
st.subheader("Contact")
st.write(
    "Email: [udayarora2012@gmail.com](mailto:udayarora2012@gmail.com)  ·  "
    "GitHub: [uday1o1](https://github.com/uday1o1)  ·  "
    "LinkedIn: [uday_arora](https://www.linkedin.com/in/uday-arora-1a6501217/)"
)
