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
hr { display: none; }

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

/* SECTIONS */
.section {
    padding: 52px 0;
}

.section.alt {
    background-color: rgba(255,255,255,0.02);
}

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
# HERO
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
I am a **data professional with strong mastery across analytics, engineering, and applied machine learning**.
My work spans the **entire data lifecycle**, from raw data extraction to insight delivery and model deployment.

I don’t treat tools as isolated skills — I focus on **how they work together in real business systems**.
""")

st.subheader("Core Technical Strengths")

st.markdown("""
**Python (Advanced)**
- Data manipulation with Pandas and NumPy  
- Analytical workflows and automation  
- Model development using Scikit-learn  
- Clean, maintainable, production-oriented code  

**SQL (Advanced)**
- Complex analytical queries and joins  
- Window functions, CTEs, and subqueries  
- Performance tuning and query optimization  
- KPI computation and metric validation  

**Excel (Advanced Analytics)**
- Pivot tables and analytical modeling  
- Business-oriented reporting  
- Data validation and exploratory analysis  

**Power BI**
- KPI and metric design  
- DAX for analytical measures  
- Executive dashboards and storytelling  
- Data modeling for scalable reporting  

**Machine Learning**
- Supervised and unsupervised learning  
- Feature engineering and model evaluation  
- Bias–variance trade-offs and interpretability  
- Practical ML for decision support, not theory-only models  
""")

st.subheader("How I Work")

st.write("""
I prioritize **clarity over complexity** and **durability over short-term demos**.

My approach emphasizes:
- Strong data foundations before modeling  
- Business context behind every metric  
- Explainable insights instead of black-box outputs  
- Solutions that scale with data growth and organizational needs  
""")

st.subheader("Problem-Solving & Coding Discipline")

st.markdown("""
- ⭐⭐⭐⭐⭐ Python – HackerRank (Gold)  
- ⭐⭐⭐⭐⭐ SQL – HackerRank (Gold)  
- ⭐⭐⭐⭐⭐ Problem Solving – HackerRank (Gold)  
- SQL Certified: Basic, Intermediate, Advanced  
- Python Certified: Basic  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.hackerrank.com/profile/Venom001" target="_blank">View HackerRank Profile</a>
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
regional trends, and KPI-driven decision-making for business stakeholders.
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
    ("Python Console Games", "Logic building, OOP, and control-flow mastery using Python.", "https://github.com/Venom-Shivu/python-console-games"),
    ("VenomSQL Analytics", "Advanced SQL analytics, KPI computation, and executive reporting.", "https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard"),
    ("Python Journey", "Structured progression through Python, DSA, and problem-solving.", "https://github.com/Venom-Shivu/My-Python-Journey"),
    ("SQL Journey", "Hands-on SQL analytics, optimization, and real-world query scenarios.", "https://github.com/Venom-Shivu/MySQL-JOURNEY"),
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
I am open to **Data Analytics, Data Science, and Machine Learning roles** —
including internships, full-time opportunities, and serious project collaborations.

I am particularly interested in roles where **data quality, analytical depth,
and decision impact** matter more than surface-level dashboards.
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
