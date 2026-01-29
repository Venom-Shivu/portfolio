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
# ANALYTICAL MINIMAL THEME (DARK)
# --------------------------------------------------
st.markdown("""
<style>
hr { display: none; }

.stApp {
    background: radial-gradient(circle at top, #0e1117 0%, #0b0f14 70%);
}

/* NAV BAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background-color: rgba(13,17,23,0.95);
    backdrop-filter: blur(6px);
    padding: 14px 0;
    border-bottom: 1px solid #1f2937;
}

.nav-items {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 34px;
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

.nav-sep {
    width: 1px;
    height: 18px;
    background-color: #374151;
}

/* SECTIONS */
.section {
    border cost: 1px solid #1f2937;
    border: 1px solid #1f2937;
    border-radius: 14px;
    padding: 36px;
    margin: 70px 0;
    background-color: #0e1117;
}

/* CARDS */
.card {
    border: 1px solid #1f2937;
    border-radius: 12px;
    padding: 24px;
    margin-top: 26px;
    background-color: #111827;
}

.section p, .card p, .card li {
    color: #9ca3af;
    line-height: 1.65;
}

/* BUTTONS */
.icon-btn a {
    text-decoration: none;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid #1f2937;
    margin: 6px 6px 0 0;
    display: inline-block;
    color: #e5e7eb;
    background-color: #0d1117;
}

.icon-btn a:hover {
    background-color: #1f2937;
}

img { border-radius: 14px; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="nav-items">
        <a href="#about">👤 About</a>
        <div class="nav-sep"></div>
        <a href="#projects">📊 Projects</a>
        <div class="nav-sep"></div>
        <a href="#contact">📬 Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
c1, c2 = st.columns([1, 4])

with c1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=150)

with c2:
    st.title("Shivansh Yadav")
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")
    st.write(
        "I design data-driven solutions that transform raw data into reliable insights "
        "and scalable systems, with strong emphasis on clarity, performance, and durability."
    )

# ==================================================
# ABOUT SECTION
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("👋 About Me")

st.write("""
I work across the **full data lifecycle** — from high-performance SQL extraction
and Python-based data processing to analytical modeling, dashboarding,
and machine learning development.

My approach is grounded in **engineering discipline and business context**:
I prioritize correctness, interpretability, and long-term maintainability
over flashy or over-engineered solutions.

I am comfortable working with:
- Large analytical datasets  
- KPI definition and metric ownership  
- Executive-level dashboards  
- ML pipelines built for real-world constraints  
""")

st.subheader("🏆 Coding & Problem-Solving Credentials")

st.markdown("""
- ⭐⭐⭐⭐⭐ **Python (Gold)** – HackerRank  
- ⭐⭐⭐⭐⭐ **SQL (Gold)** – HackerRank  
- ⭐⭐⭐⭐⭐ **Problem Solving (Gold)** – HackerRank  
- **SQL Certifications:** Basic, Intermediate, Advanced  
- **Python Certification:** Basic  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.hackerrank.com/profile/Venom001" target="_blank">🏆 View HackerRank Profile</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# PROJECTS SECTION
# ==================================================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("📊 Featured Projects")

# --- Nexus Analytics ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")

st.write("""
An end-to-end analytics project designed to evaluate e-commerce business performance
across revenue, customers, products, and operations.

**Key Focus Areas**
- KPI design and metric standardization  
- Sales, customer, and regional analysis  
- Executive-ready dashboard planning  
- Data storytelling for decision-makers  
""")

if os.path.exists("images/nexus_dashboard_mockup.png"):
    st.image(
        "images/nexus_dashboard_mockup.png",
        caption="Proposed Executive Dashboard Blueprint",
        use_container_width=True
    )

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/portfolio" target="_blank">💻 View Repository</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Other Repositories ---
repos = [
    (
        "🎮 Python Console Games",
        "A collection of Python-based console games focused on logic building, "
        "object-oriented programming, and control-flow mastery.",
        "https://github.com/Venom-Shivu/python-console-games"
    ),
    (
        "📈 VenomSQL – Executive Analytics",
        "Advanced SQL analytics project centered on KPI creation, complex joins, "
        "window functions, and executive reporting workflows.",
        "https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard"
    ),
    (
        "🐍 Python Journey",
        "Structured learning repository covering Python fundamentals, "
        "data structures, algorithms, and problem-solving patterns.",
        "https://github.com/Venom-Shivu/My-Python-Journey"
    ),
    (
        "🗄️ SQL Journey",
        "Comprehensive SQL practice repository covering analytics queries, "
        "optimization techniques, and real-world problem scenarios.",
        "https://github.com/Venom-Shivu/MySQL-JOURNEY"
    ),
]

for name, desc, link in repos:
    st.markdown(f"""
    <div class="card">
        <strong>{name}</strong>
        <p>{desc}</p>
        <div class="icon-btn">
            <a href="{link}" target="_blank">🔗 View Repository</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# CONTACT SECTION
# ==================================================
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("📬 Contact & Availability")

st.write("""
I am actively open to **Data Science, Analytics, and Machine Learning roles**,
including internships, full-time positions, and collaborative projects.

I’m particularly interested in:
- Business-driven analytics  
- SQL-heavy analytical roles  
- Dashboarding & BI systems  
- Applied machine learning projects  
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com/in/the-venom/" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view" target="_blank">Resume</a>
<a href="mailto:mrshivusinghyadav@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.caption("© 2026 Shivansh Yadav | Data & Analytics Portfolio")
