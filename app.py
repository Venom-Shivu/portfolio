import streamlit as st
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Shivansh Yadav | Data & Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# HARD OVERRIDE STREAMLIT LAYOUT (NO SEPARATORS)
# --------------------------------------------------
st.markdown("""
<style>

/* REMOVE ALL DEFAULT STREAMLIT SPACING & SEPARATORS */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 0 !important;
}

.element-container {
    margin-bottom: 0 !important;
}

hr {
    display: none !important;
}

/* FULL CONTINUOUS BACKGROUND – ANALYTICAL THEME */
.stApp {
    background:
        radial-gradient(circle at 20% 10%, #111827 0%, #0b0f14 45%, #0a0d12 100%);
}

/* NAVBAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(11, 15, 20, 0.92);
    backdrop-filter: blur(10px);
    padding: 12px 0;
}

/* NAV ITEMS */
.nav-items {
    display: flex;
    justify-content: center;
    gap: 42px;
}

.nav-items a {
    color: #e5e7eb;
    font-weight: 600;
    text-decoration: none;
    padding: 6px 14px;
    border-radius: 6px;
}

.nav-items a:hover {
    background-color: rgba(255,255,255,0.06);
}

/* TYPOGRAPHY */
h1, h2, h3 {
    color: #f9fafb;
    letter-spacing: 0.3px;
}

p, li {
    color: #9ca3af;
    line-height: 1.75;
}

/* SOFT CONTENT CARDS (NO VISUAL SEPARATION) */
.card {
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    padding: 24px;
    margin-top: 22px;
}

/* BUTTONS */
.icon-btn a {
    display: inline-block;
    margin-top: 8px;
    margin-right: 10px;
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.12);
    color: #e5e7eb;
    text-decoration: none;
    font-weight: 600;
    background: rgba(0,0,0,0.2);
}

.icon-btn a:hover {
    background: rgba(255,255,255,0.08);
}

img {
    border-radius: 14px;
}
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
# HERO
# --------------------------------------------------
c1, c2 = st.columns([1, 4])

with c1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=150)

with c2:
    st.title("Shivansh Yadav")
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")
    st.write(
        "I build data-driven systems that turn raw data into trusted insights and "
        "decision-ready intelligence, with a strong focus on analytical depth, "
        "business relevance, and long-term maintainability."
    )

# ==================================================
# ABOUT
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.header("About Me")

st.write("""
I am a **data professional with deep hands-on expertise across Data Analytics,
Business Intelligence, and Applied Machine Learning**.

My work spans the full analytics lifecycle — from raw data extraction and
transformation to KPI modeling, dashboarding, and predictive analysis.
""")

st.markdown("""
**Core Strengths**
- 🐍 **Python** – data analysis, automation, ML pipelines  
- 🗄️ **SQL** – advanced analytics, performance tuning, KPI computation  
- 📊 **Excel** – analytical modeling, validation, business reporting  
- 📈 **Power BI** – DAX, data modeling, executive dashboards  
- 🤖 **Machine Learning** – supervised & unsupervised models  
- 📉 **Business & Data Analysis** – KPI design, storytelling, decision support  
""")

st.markdown("""
**Credentials**
- ⭐⭐⭐⭐⭐ Python – HackerRank (Gold)  
- ⭐⭐⭐⭐⭐ SQL – HackerRank (Gold)  
- ⭐⭐⭐⭐⭐ Problem Solving – HackerRank (Gold)  
- SQL Certified: Basic, Intermediate, Advanced  
- Python Certified: Basic  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.hackerrank.com/profile/Venom001" target="_blank">View HackerRank</a>
</div>
""", unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("Projects")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("VenomSQL — Executive Analytics Dashboard")
st.write("""
A SQL-first executive analytics project focused on business KPIs,
performance tracking, and decision-ready reporting.
""")

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard" target="_blank">
View Repository
</a>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")
st.write("""
End-to-end analytics project analyzing e-commerce sales, customers,
regions, and operational KPIs.
""")

if os.path.exists("images/nexus_dashboard_mockup.png"):
    st.image("images/nexus_dashboard_mockup.png", use_container_width=True)

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/portfolio" target="_blank">View Repository</a>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# CONTACT
# ==================================================
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("Contact & Opportunities")

st.write("""
I am actively open to **Data Analyst, Business Analyst, Data Scientist,
and Machine Learning roles**, including internships, full-time positions,
and serious collaborations.

If you’re looking for someone who understands **both data and business impact**,
I’d be glad to connect.
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com/in/the-venom/" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view" target="_blank">Resume</a>
<a href="mailto:mrshivusinghyadav@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 Shivansh Yadav")
