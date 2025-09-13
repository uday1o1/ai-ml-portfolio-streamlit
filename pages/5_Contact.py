import streamlit as st
import requests
from components.nav import top_nav
top_nav(active="Contact")

st.set_page_config(page_title="Contact — Your Name", page_icon="✉️", layout="wide")

st.title("Contact Me")
st.write("Feel free to reach out — I’m happy to connect!")

FORMSPREE_URL = "https://formspree.io/f/xpwjnowj"

with st.form("contact_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        if not name or not email or not message:
            st.error("Please fill in all fields.")
        else:
            data = {
                "name": name,
                "email": email,
                "message": message,
            }
            try:
                resp = requests.post(FORMSPREE_URL, data=data)
                if resp.status_code == 200:
                    st.success("✅ Message sent successfully! I’ll get back to you soon.")
                else:
                    st.error(f"Something went wrong: {resp.text}")
            except Exception as e:
                st.error(f"Error sending message: {e}")

st.divider()
st.markdown("Or email me directly: [udayarora2012@gmail.com](mailto:udayarora2012@gmail.com)")
