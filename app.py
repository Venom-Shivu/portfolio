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
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 0 !important;
}
.element-container {
    margin-bottom: 0 !important;
}
hr { display: none !important; }

/* CONTINUOUS ANALYTICAL BACKGROUND */
.stApp {
    background:
        radial-gradient(circle at 20% 10%, #111827 0%, #0b0f14 45%, #0a0d12 100%);
}

/* NAVBAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(11,15,20,0.92);
    backdrop-filter: blur(10px);
    padding: 12px 0;
}

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

/* SOFT CARDS */
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
        "I build data-driven systems that transform raw data into trusted insights "
        "and decision-ready intelligence, with strong emphasis on analytical rigor, "
        "business relevance, and long-term maintainability."
    )

# ==================================================
# ABOUT
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.header("About Me")

st.write("""
I am a **data professional with advanced expertise in Python and SQL**, and strong
hands-on experience across **Data Analytics, Business Analytics, and foundational
Data Science & Machine Learning**.

My work covers the **entire analytical lifecycle** — from raw data extraction and
modeling to statistical validation, dashboarding, and predictive analysis.
""")

st.subheader("🧠 Core Technical Skills")

st.markdown("""
### 🐍 Python — *Advanced*
- Pandas, NumPy for large-scale data analysis  
- Analytical automation & reusable pipelines  
- Feature engineering & data preprocessing  
- Scikit-learn for machine learning workflows  

### 🗄️ SQL — *Advanced Analytics*
- Complex joins, CTEs, window functions  
- KPI definition & metric validation  
- Query optimization & performance tuning  
- Business reporting & analytical datasets  

### 📊 Excel — *Business Analytics*
- Pivot tables & analytical modeling  
- Business reporting & validation checks  
- Ad-hoc analysis for stakeholders  

### 📈 Power BI — *Business Intelligence*
- Data modeling & relationships  
- DAX measures & calculated tables  
- Executive dashboards & storytelling  
- KPI frameworks & performance tracking  

### 📉 Data Analytics & Business Analysis
- Requirements gathering & stakeholder alignment  
- Translating business questions into metrics  
- Data storytelling & insight communication  
- Decision-support analytics  

### 🤖 Machine Learning — *Foundational*
- Supervised & unsupervised learning  
- Model evaluation & validation  
- Bias–variance trade-offs  
- Practical ML for business use cases  

### 📐 Statistics & Hypothesis Testing
- Descriptive & inferential statistics  
- Probability distributions  
- Confidence intervals  
- Hypothesis testing (A/B testing, t-tests, chi-square)  
- Statistical reasoning for decision-making  
""")

st.subheader("🏆 Coding & Problem-Solving Credentials")

st.markdown("""
- ⭐⭐⭐⭐⭐ **Python – HackerRank (Gold)**  
- ⭐⭐⭐⭐⭐ **SQL – HackerRank (Gold)**  
- ⭐⭐⭐⭐⭐ **Problem Solving – HackerRank (Gold)**  
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
A **SQL-first executive analytics project** focused on KPI design,
performance tracking, and decision-ready reporting for business stakeholders.
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
End-to-end analytics project analyzing e-commerce sales, customer behavior,
regional performance, and operational KPIs.
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
and serious project collaborations.

I’m particularly interested in roles involving:
- SQL-heavy analytics  
- KPI ownership & business reporting  
- Data-driven decision support  
- Applied analytics & ML use cases  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com/in/the-venom/" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view" target="_blank">Resume</a>
<a href="mailto:mrshivusinghyadav@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 Shivansh Yadav | Data & Analytics Portfolio")
