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
# MINIMAL ANALYTICAL THEME
# --------------------------------------------------
st.markdown("""
<style>
hr { display: none; }

/* Background */
.stApp {
    background: linear-gradient(180deg, #0b0f14 0%, #0e1117 40%, #0b0f14 100%);
}

/* Navbar */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background-color: rgba(13,17,23,0.95);
    backdrop-filter: blur(8px);
    padding: 12px 0;
}

.nav-items {
    display: flex;
    justify-content: center;
    gap: 36px;
}

.nav-items a {
    color: #e5e7eb;
    font-weight: 600;
    text-decoration: none;
    padding: 6px 14px;
    border-radius: 6px;
}

.nav-items a:hover {
    background-color: #1f2937;
}

/* Sections */
.section {
    padding: 60px 0;
}

.section.alt {
    background-color: rgba(255,255,255,0.025);
}

.section-inner {
    max-width: 1200px;
    margin: auto;
}

/* Cards */
.card {
    background-color: #111827;
    border-radius: 12px;
    padding: 26px;
    margin-top: 28px;
}

/* Text */
p, li {
    color: #9ca3af;
    line-height: 1.7;
}

/* Buttons */
.icon-btn a {
    display: inline-block;
    margin-right: 10px;
    margin-top: 6px;
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid #1f2937;
    color: #e5e7eb;
    text-decoration: none;
    font-weight: 600;
    background-color: #0d1117;
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
        "and decision-ready intelligence, with strong focus on analytical depth, "
        "business relevance, and long-term maintainability."
    )

# ==================================================
# ABOUT
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-inner">', unsafe_allow_html=True)

st.header("About Me")

st.write("""
I am a **data professional with strong mastery across Data Analytics, Business Intelligence,
and Applied Machine Learning**. I work end-to-end — from raw data extraction to executive
insight delivery and model-driven decision support.

My strength lies in combining **technical depth with business understanding**.
I don’t just analyze data — I design systems that help stakeholders make
better, faster, and more confident decisions.
""")

st.subheader("🧠 Core Skills & Tooling")

st.markdown("""
**🐍 Python (Advanced)**
- Pandas, NumPy for data analysis  
- Automation & analytical pipelines  
- Scikit-learn for ML modeling  

**🗄️ SQL (Advanced Analytics)**
- Complex joins, CTEs, window functions  
- KPI computation & validation  
- Query optimization and performance tuning  

**📊 Excel (Analytics & Reporting)**
- Pivot tables & analytical models  
- Business reporting & validation  
- Ad-hoc analysis for stakeholders  

**📈 Power BI**
- KPI design & metric frameworks  
- DAX measures & calculated tables  
- Executive dashboards & storytelling  

**🤖 Machine Learning**
- Supervised & unsupervised models  
- Feature engineering & evaluation  
- Practical ML for business use cases  

**📉 Data & Business Analysis**
- Requirements gathering & KPI definition  
- Translating business questions into metrics  
- Insight communication & data storytelling  
""")

st.subheader("🏆 Coding & Problem-Solving Credentials")

st.markdown("""
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

st.markdown("</div></div>", unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown('<div class="section alt">', unsafe_allow_html=True)
st.markdown('<div class="section-inner">', unsafe_allow_html=True)

st.header("Projects")

# --- VenomSQL ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("VenomSQL — Executive Analytics Dashboard")

st.write("""
A **SQL-first executive analytics project** focused on business KPIs, performance tracking,
and decision-ready reporting.

**Highlights**
- Advanced SQL analytics & KPI design  
- Executive-level reporting mindset  
- Clean, optimized analytical queries  
- Business-oriented insight delivery  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard" target="_blank">
View Repository
</a>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Nexus Analytics ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")

st.write("""
End-to-end analytics project analyzing e-commerce sales, customers, regions,
and operations with KPI-driven dashboard planning.
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
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-inner">', unsafe_allow_html=True)

st.header("Contact & Opportunities")

st.write("""
I am actively open to **Data Analyst, Business Analyst, Data Scientist,
and Machine Learning roles**, including internships, full-time positions,
and high-impact collaborations.

I’m particularly interested in roles that involve:
- KPI ownership and business analytics  
- SQL-heavy analytical work  
- Dashboarding & BI systems  
- Data-driven decision support  
""")

st.write("""
If you’re looking for someone who understands **both the data and the business side**,
I’d be happy to connect.
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com/in/the-venom/" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view" target="_blank">Resume</a>
<a href="mailto:mrshivusinghyadav@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

st.caption("© 2026 Shivansh Yadav | Data & Analytics Portfolio")
