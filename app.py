import streamlit as st
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Shivansh Yadav | Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# PROFESSIONAL ANALYTICS THEME
# --------------------------------------------------
st.markdown("""
<style>
/* REMOVE STREAMLIT DEFAULT SEPARATORS */
hr { display: none; }

/* GLOBAL BACKGROUND (ANALYTICS FEEL) */
.stApp {
    background:
        linear-gradient(180deg, #0b0f14 0%, #0e1117 35%, #0b0f14 100%);
}

/* NAVBAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background-color: rgba(13,17,23,0.95);
    backdrop-filter: blur(8px);
    padding: 12px 0;
}

/* NAV ITEMS */
.nav-items {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 36px;
}

.nav-items a {
    text-decoration: none;
    font-weight: 600;
    color: #e5e7eb;
    padding: 6px 14px;
    border-radius: 6px;
}

.nav-items a:hover {
    background-color: #1f2937;
}

/* HEADER TEXT */
h1, h2, h3 {
    color: #f9fafb;
}

/* SECTION WRAPPER (NO BORDERS) */
.section {
    padding: 48px 0;
}

/* ALT SECTION BACKGROUND */
.section.alt {
    background-color: rgba(255,255,255,0.02);
}

/* CONTENT WIDTH CONTROL */
.section-inner {
    max-width: 1200px;
    margin: auto;
}

/* CARDS */
.card {
    background-color: #111827;
    border-radius: 12px;
    padding: 24px;
    margin-top: 24px;
}

/* TEXT */
p, li {
    color: #9ca3af;
    line-height: 1.7;
}

/* BUTTONS */
.icon-btn a {
    text-decoration: none;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 8px;
    margin-right: 8px;
    display: inline-block;
    color: #e5e7eb;
    background-color: #0d1117;
    border: 1px solid #1f2937;
}

.icon-btn a:hover {
    background-color: #1f2937;
}

img { border-radius: 14px; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="nav-items">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO / HEADER
# --------------------------------------------------
hero1, hero2 = st.columns([1, 4])

with hero1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=150)

with hero2:
    st.title("Shivansh Yadav")
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")
    st.write(
        "I design data-driven solutions that convert raw data into reliable insights "
        "and scalable systems, with strong emphasis on correctness, performance, "
        "and long-term maintainability."
    )

# ==================================================
# ABOUT
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-inner">', unsafe_allow_html=True)

st.header("About Me")
st.write("""
I work across the full data lifecycle — from SQL-heavy data extraction
and Python-based analytics to dashboarding and machine learning systems.

My focus is on **business-aligned analytics**, **clean data models**, and
solutions that survive real-world usage rather than demo-only prototypes.
""")

st.markdown("""
- Strong in SQL analytics and performance tuning  
- Experienced with KPI design and executive dashboards  
- Solid foundation in machine learning and statistics  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.hackerrank.com/profile/Venom001" target="_blank">HackerRank</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown('<div class="section alt">', unsafe_allow_html=True)
st.markdown('<div class="section-inner">', unsafe_allow_html=True)

st.header("Projects")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")
st.write("""
End-to-end analytics project focused on sales performance, customer behavior,
regional trends, and KPI-driven decision making.
""")

if os.path.exists("images/nexus_dashboard_mockup.png"):
    st.image("images/nexus_dashboard_mockup.png", use_container_width=True)

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/portfolio" target="_blank">View Repository</a>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

repos = [
    ("Python Console Games", "Logic building and OOP practice through console games.", "https://github.com/Venom-Shivu/python-console-games"),
    ("VenomSQL Analytics", "Advanced SQL analytics and KPI-focused reporting.", "https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard"),
    ("Python Journey", "Structured Python, DSA, and problem-solving progression.", "https://github.com/Venom-Shivu/My-Python-Journey"),
    ("SQL Journey", "Hands-on SQL analytics and query optimization practice.", "https://github.com/Venom-Shivu/MySQL-JOURNEY"),
]

for name, desc, link in repos:
    st.markdown(f"""
    <div class="card">
        <strong>{name}</strong>
        <p>{desc}</p>
        <div class="icon-btn">
            <a href="{link}" target="_blank">View Repository</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# ==================================================
# CONTACT
# ==================================================
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-inner">', unsafe_allow_html=True)

st.header("Contact")
st.write("""
Open to data science, analytics, and machine learning opportunities.
Available for internships, full-time roles, and serious collaborations.
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com/in/the-venom/" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view" target="_blank">Resume</a>
<a href="mailto:mrshivusinghyadav@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

st.caption("© 2026 Shivansh Yadav")
