import json
from pathlib import Path
import streamlit as st

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "projects.json"

@st.cache_data
def load_projects():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def all_tags(projects):
    tags = set()
    for p in projects:
        tags.update(p.get("tags", []))
    return sorted(tags)

def render_project_card(p):
    cols = st.columns([1, 2])
    with cols[0]:
        if p.get("thumbnail"):
            st.image(p["thumbnail"], use_container_width=True)
    with cols[1]:
        st.subheader(p["title"])
        st.caption(str(p.get("year", "")))
        st.write(p["summary"])
        if p.get("tags"):
            st.write(" ".join([f"`{t}`" for t in p["tags"]]))
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if st.button("Case study", key=f"case_{p['slug']}"):
                st.query_params["p"] = p["slug"]
                st.rerun()
        with c2:
            if p.get("demo"):
                st.link_button("Live demo", p["demo"])
        with c3:
            if p.get("repo"):
                st.link_button("Code", p["repo"])
        with c4:
            if p.get("paper"):
                st.link_button("Paper", p["paper"])
        if p.get("metrics"):
            st.markdown("**Key metrics**")
            mcols = st.columns(min(3, len(p["metrics"])))
            for i, m in enumerate(p["metrics"]):
                with mcols[i % len(mcols)]:
                    st.metric(m["name"], m["value"])

def render_project_detail(p):
    st.title(p["title"])
    st.caption(f"{p.get('year','')} • " + " ".join([f"`{t}`" for t in p.get("tags", [])]))
    if p.get("thumbnail"):
        st.image(p["thumbnail"], use_container_width=True)
    st.markdown("### Summary")
    st.write(p["summary"])
    if p.get("metrics"):
        st.markdown("### Results")
        for m in p["metrics"]:
            st.metric(m["name"], m["value"])
    links = []
    if p.get("demo"):  links.append(f"[Live demo]({p['demo']})")
    if p.get("repo"):  links.append(f"[Code]({p['repo']})")
    if p.get("paper"): links.append(f"[Paper]({p['paper']})")
    if links:
        st.markdown("### Links\n" + " • ".join(links))
    st.divider()
    st.markdown("### Lessons / Notes")
    st.info("Add bullets on what worked and what you’d change next time.")
