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
# STYLING (DARK THEME SAFE)
# --------------------------------------------------
st.markdown("""
<style>
/* NAV BAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background-color: #0d1117;
    padding: 12px 0;
    border-bottom: 1px solid #30363d;
}

/* NAV ITEMS */
.nav-items {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
}

.nav-items a {
    text-decoration: none;
    font-weight: 600;
    color: #f0f6fc;
    padding: 8px 16px;
    border-radius: 8px;
}

.nav-items a:hover {
    background-color: #21262d;
}

/* SEPARATOR */
.nav-sep {
    width: 1px;
    height: 22px;
    background-color: #30363d;
}

/* SECTION */
.section {
    border: 1px solid #30363d;
    border-radius: 16px;
    padding: 32px;
    margin: 60px 0;
    background-color: #0e1117;
}

/* CARD */
.card {
    border: 1px solid #30363d;
    border-radius: 14px;
    padding: 22px;
    margin-top: 24px;
    background-color: #161b22;
    color: #e6edf3;
}

/* TEXT */
.section p, .card p, .card li {
    color: #c9d1d9;
}

/* BUTTONS */
.icon-btn a {
    text-decoration: none;
    font-weight: 600;
    padding: 10px 18px;
    border-radius: 10px;
    border: 1px solid #30363d;
    margin: 6px 6px 0 0;
    display: inline-block;
    color: #f0f6fc;
    background-color: #0d1117;
}

.icon-btn a:hover {
    background-color: #21262d;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION BAR (REAL, EQUAL, SEPARATED)
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
h1, h2 = st.columns([1, 4])

with h1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=150)

with h2:
    st.title("Shivansh Yadav")
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")
    st.write(
        "I design data-driven solutions that convert raw data into reliable insights "
        "and scalable systems, prioritizing clarity, performance, and durability."
    )

# ==================================================
# ABOUT SECTION
# ==================================================
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("👋 About Me")
st.write("""
I work across the full data lifecycle — from high-performance SQL extraction
and Python-based analysis to dashboarding and machine learning development.

I value correctness and sustainability over flashy or over-engineered solutions.
""")

st.subheader("🏆 HackerRank Achievements")
st.markdown("""
- ⭐⭐⭐⭐⭐ Python (Gold)  
- ⭐⭐⭐⭐⭐ SQL (Gold)  
- ⭐⭐⭐⭐⭐ Problem Solving (Gold)  
- SQL Basic, Intermediate & Advanced Certified  
- Python Basic Certified
""")

st.markdown("""
<div class="icon-btn">
<a href="https://www.hackerrank.com/profile/Venom001" target="_blank">🏆 HackerRank</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# PROJECTS SECTION
# ==================================================
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown('<div class="section">', unsafe_allow_html=True)

st.header("📊 Featured Projects")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")
st.write("""
KPI-driven analytics project evaluating e-commerce sales, customer behavior,
and operational performance with executive dashboard planning.
""")

if os.path.exists("images/nexus_dashboard_mockup.png"):
    st.image(
        "images/nexus_dashboard_mockup.png",
        caption="Proposed Dashboard Blueprint",
        use_container_width=True
    )

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/portfolio" target="_blank">💻 View Repository</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

repos = [
    ("🎮 Python Console Games", "https://github.com/Venom-Shivu/python-console-games"),
    ("📈 VenomSQL – Executive Analytics", "https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard"),
    ("🐍 Python Journey", "https://github.com/Venom-Shivu/My-Python-Journey"),
    ("🗄️ SQL Journey", "https://github.com/Venom-Shivu/MySQL-JOURNEY"),
]

for name, link in repos:
    st.markdown(f"""
    <div class="card">
        <strong>{name}</strong><br><br>
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

st.header("📬 Contact")

st.markdown("""
<div class="icon-btn">
<a href="https://www.linkedin.com/in/the-venom/" target="_blank">LinkedIn</a>
<a href="https://github.com/Venom-Shivu" target="_blank">GitHub</a>
<a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view" target="_blank">Resume</a>
<a href="mailto:mrshivusinghyadav@gmail.com">Email</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.caption("© 2026 Shivansh Yadav | Built with Streamlit")
