import streamlit as st
from components.nav import top_nav
from components.projects import load_projects, all_tags, render_project_card, render_project_detail

top_nav(active="Projects")

st.set_page_config(page_title="Projects — Your Name", page_icon="📦", layout="wide")

projects = load_projects()
slug = st.query_params.get("p")

if slug:
    # Detail page
    proj = next((p for p in projects if p["slug"] == slug), None)
    if proj is None:
        st.error("Project not found.")
    else:
        st.page_link("pages/2_Projects.py", label="← Back to Projects")
        render_project_detail(proj)
else:
    # Index page
    st.title("Projects")
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("Search", placeholder="keyword, model, dataset…")
    with col2:
        tag_filter = st.multiselect("Filter tags", options=all_tags(projects))

    def ok(p):
        blob = " ".join([p["title"], p["summary"], " ".join(p.get("tags", []))]).lower()
        has = (search.lower() in blob) if search else True
        tags_ok = set(tag_filter).issubset(set(p.get("tags", []))) if tag_filter else True
        return has and tags_ok

    filtered = [p for p in projects if ok(p)]
    st.write(f"Showing **{len(filtered)}** project(s).")
    for p in filtered:
        render_project_card(p)
        st.divider()
