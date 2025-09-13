import streamlit as st
from components.nav import top_nav
top_nav(active="Experience")

st.set_page_config(page_title="Experience — Your Name", page_icon="💼", layout="wide")

st.title("Industry Experience & Internships")

def job_card(title: str, org_team: str, dates: str, bullets: list[str], metrics: list[tuple[str, str]] | None = None, tech: list[str] | None = None):
    with st.container(border=True):
        top = st.columns([3, 2])
        with top[0]:
            st.subheader(title)
            st.caption(org_team)
        with top[1]:
            st.markdown(f"**{dates}**")

        st.markdown("**Highlights**")
        for b in bullets:
            st.markdown(f"- {b}")

        if metrics:
            st.markdown("**Impact**")
            cols = st.columns(len(metrics))
            for i, (name, value) in enumerate(metrics):
                with cols[i]:
                    st.metric(name, value)

        if tech:
            st.markdown("**Tech**")
            st.write(" ".join([f"`{t}`" for t in tech]))


# ==== Role 1 ====
job_card(
    title="AI Engineer Intern",
    org_team="Bid Sense Team, Tata Communications",
    dates="May 2025 – July 2025",
    bullets=[
        "Designed an intelligent agent system leveraging LLMs (GPT, LLaMA) with RAG pipelines (LangChain, LlamaIndex, FAISS) to automate workflow tasks such as information retrieval, summarization, and decision support for RFP documents.",
        "Delivered a scalable, production-ready solution with Python, Docker, AWS, and MLflow, plus a Streamlit interface that reduced research time and improved usability for cross-functional teams.",
    ],
    metrics=[
        ("Research Time ↓", "60%"),
    ],
    tech=["GPT", "LLaMA", "LangChain", "LlamaIndex", "FAISS", "Python", "Docker", "AWS", "MLflow", "Streamlit"],
)

st.divider()

# ==== Role 2 ====
job_card(
    title="ML Engineer Intern",
    org_team="SAE Team, Bharti Airtel",
    dates="Aug 2023 – Oct 2023",
    bullets=[
        "Developed ML pipelines to analyze large-scale 5G RAN data, enabling intelligent agents to detect patterns for network optimization and automated resource allocation.",
        "Enhanced throughput and latency KPIs through time-series forecasting, anomaly detection, and clustering models implemented with scikit-learn, XGBoost, and TensorFlow.",
    ],
    metrics=[
        ("Throughput/Latency KPIs ↑", "15%"),
    ],
    tech=["5G RAN", "Time-series", "Anomaly Detection", "Clustering", "scikit-learn", "XGBoost", "TensorFlow"],
)

st.divider()

