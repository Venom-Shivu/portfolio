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
# DARK-THEME SAFE STYLING
# --------------------------------------------------
st.markdown("""
<style>
/* Section container */
.section-box {
    border: 1px solid #2c2f36;
    border-radius: 14px;
    padding: 28px;
    margin-bottom: 40px;
    background-color: #0e1117;
}

/* Card container */
.card {
    border: 1px solid #2c2f36;
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 25px;
    background-color: #161b22;
    color: #e6edf3;
}

/* Headings */
.card h3, .card strong {
    color: #f0f6fc;
}

/* Text */
.section-box p, .card p, .card li {
    color: #c9d1d9;
}

/* Center alignment */
.center {
    text-align: center;
}

/* Buttons */
.icon-btn a {
    text-decoration: none;
    font-weight: 600;
    padding: 10px 18px;
    border-radius: 10px;
    border: 1px solid #30363d;
    margin: 6px;
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
# SESSION STATE (NAVIGATION)
# --------------------------------------------------
if "section" not in st.session_state:
    st.session_state.section = "About"

# --------------------------------------------------
# TOP NAVIGATION
# --------------------------------------------------
n1, n2, n3 = st.columns(3)

with n1:
    if st.button("👤 About"):
        st.session_state.section = "About"

with n2:
    if st.button("📊 Projects"):
        st.session_state.section = "Projects"

with n3:
    if st.button("📬 Contact"):
        st.session_state.section = "Contact"

st.divider()

# --------------------------------------------------
# HEADER (PROFILE)
# --------------------------------------------------
h1, h2 = st.columns([1, 4])

with h1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=150)
    else:
        st.warning("Profile image not found")

with h2:
    st.title("Shivansh Yadav")
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")
    st.write("""
    I design **data-driven solutions** that convert raw data into reliable insights
    and scalable systems, prioritizing clarity, performance, and long-term durability.
    """)

st.divider()

# ==================================================
# ABOUT SECTION
# ==================================================
if st.session_state.section == "About":

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("👋 About Me")

    st.write("""
    I work across the **full data lifecycle** — from high-performance SQL extraction
    and Python-based data analysis to dashboarding and machine learning model development.

    I value **correctness and sustainability** over flashy or over-engineered solutions.
    """)

    st.subheader("🧠 Technical Expertise")

    st.markdown("""
    **Programming & Data Engineering**
    - Python (Pandas, NumPy)
    - SQL (Advanced Analytics & Optimization)
    - Data Structures & Algorithms

    **Machine Learning & AI**
    - Scikit-learn, TensorFlow, PyTorch
    - Classical ML & Deep Learning
    - Generative AI & Prompt Engineering

    **Analytics & Visualization**
    - Power BI, Tableau
    - DAX & KPI Design
    - Excel & Jupyter
    """)

    st.subheader("🏆 HackerRank Achievements")

    st.markdown("""
    **⭐ 5-Star Gold Badges**
    - Python  
    - SQL  
    - Problem Solving  

    **📜 Certifications**
    - SQL (Basic, Intermediate, Advanced)  
    - Python (Basic)
    """)

    st.markdown("""
    <div class="icon-btn">
        <a href="https://www.hackerrank.com/profile/Venom001" target="_blank">🏆 HackerRank Profile</a>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Current Focus")
    st.markdown("""
    - Advanced SQL performance tuning  
    - End-to-end ML projects with real datasets  
    - Business-driven analytics & storytelling  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# PROJECTS SECTION
# ==================================================
elif st.session_state.section == "Projects":

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📊 Featured Projects")

    # Nexus Analytics
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")

    st.write("""
    KPI-driven analytics project focused on evaluating e-commerce sales,
    customer behavior, and operational performance with executive-style
    dashboard planning.
    """)

    if os.path.exists("images/nexus_dashboard_mockup.png"):
        st.image(
            "images/nexus_dashboard_mockup.png",
            caption="Proposed KPI & Dashboard Layout (Concept Design)",
            use_container_width=True
        )

    st.markdown("""
    <div class="icon-btn">
        <a href="https://github.com/Venom-Shivu/portfolio" target="_blank">💻 View Repository</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("📁 Other Notable Repositories")

    repos = [
        ("🎮 Python Console Games", "https://github.com/Venom-Shivu/python-console-games"),
        ("📈 VenomSQL – Executive Analytics", "https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard"),
        ("🐍 Python Journey", "https://github.com/Venom-Shivu/My-Python-Journey"),
        ("🗄️ SQL Journey", "https://github.com/Venom-Shivu/MySQL-JOURNEY"),
        ("📚 Python Practice Workbook", "https://github.com/Venom-Shivu/Comprehensive-Python-Practice-Workbook-Venom"),
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
elif st.session_state.section == "Contact":

    st.markdown('<div class="section-box center">', unsafe_allow_html=True)
    st.header("📬 Connect With Me")

    st.markdown("""
    <div class="icon-btn">
        <a href="https://www.linkedin.com/in/the-venom/" target="_blank">🔗 LinkedIn</a>
        <a href="https://github.com/Venom-Shivu" target="_blank">🐙 GitHub</a>
        <a href="https://www.hackerrank.com/profile/Venom001" target="_blank">🏆 HackerRank</a>
        <a href="https://drive.google.com/file/d/1WDtScZmczuYFGEnJv2BkCMnsw2bXPRBA/view?usp=sharing" target="_blank">📄 Resume</a>
        <a href="mailto:mrshivusinghyadav@gmail.com">📧 Email</a>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Open to **Data Science, Analytics, and Machine Learning roles**,
    internships, and meaningful collaborations.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption("© 2026 Shivansh Yadav | Built with Python & Streamlit")
