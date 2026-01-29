import streamlit as st
import pandas as pd
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
# SESSION STATE (NAVIGATION)
# --------------------------------------------------
if "section" not in st.session_state:
    st.session_state.section = "About"

# --------------------------------------------------
# TOP NAVIGATION
# --------------------------------------------------
nav1, nav2, nav3 = st.columns(3)

with nav1:
    if st.button("👤 About"):
        st.session_state.section = "About"

with nav2:
    if st.button("📊 Projects"):
        st.session_state.section = "Projects"

with nav3:
    if st.button("📬 Contact"):
        st.session_state.section = "Contact"

st.divider()

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("Shivansh Yadav")
st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")

st.write("""
I design **data-driven solutions** that convert raw data into reliable insights
and scalable systems, focusing on clarity, performance, and business relevance.
""")

st.divider()

# ==================================================
# ABOUT SECTION
# ==================================================
if st.session_state.section == "About":

    st.header("👋 About Me")

    st.write("""
    I work across the **full data lifecycle** — from extracting and optimizing data,
    to building analytical systems, dashboards, and machine learning models.

    My approach prioritizes **durability and correctness** over flashy or
    over-engineered solutions.
    """)

    st.subheader("🧠 Core Capabilities")

    st.markdown("""
    **Programming & Data Engineering**
    - Python (Pandas, NumPy)
    - SQL (Joins, CTEs, Performance Optimization)
    - Data Structures & Algorithms

    **Machine Learning & AI**
    - Scikit-learn, TensorFlow, PyTorch
    - Classical ML & Deep Learning
    - Generative AI & Prompt Engineering

    **Analytics & Visualization**
    - Power BI, Tableau
    - DAX & KPI Design
    - Excel & Jupyter Notebooks
    """)

    st.subheader("🎯 Current Focus")
    st.markdown("""
    - Advanced SQL performance tuning  
    - End-to-end ML projects with real datasets  
    - Business-driven analytics & storytelling  
    """)

# ==================================================
# PROJECTS SECTION
# ==================================================
elif st.session_state.section == "Projects":

    st.header("📊 Featured Projects")

    # -------------------------------
    # Nexus Analytics
    # -------------------------------
    st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")

    st.write("""
    A professional analytics project focused on evaluating e-commerce sales,
    customer behavior, and operational performance through KPI-driven analysis
    and executive dashboard design.
    """)

    st.markdown("""
    **Focus Areas**
    - Sales & revenue analysis
    - KPI planning and metric design
    - Dashboard blueprinting
    - Business insight generation
    """)

    if os.path.exists("images/nexus_dashboard_mockup.png"):
        st.image(
            "images/nexus_dashboard_mockup.png",
            caption="Proposed KPI & Dashboard Layout (Concept Design)",
            use_container_width=True
        )
    else:
        st.info("Dashboard mockup image not available.")

    st.markdown("[🔗 View Repository](https://github.com/Venom-Shivu/portfolio)")

    st.divider()

    # -------------------------------
    # Other GitHub Projects
    # -------------------------------
    st.subheader("📁 Other Notable Repositories")

    st.markdown("""
    **🎮 Python Console Games**  
    Logic-building and OOP-focused Python games  
    🔗 https://github.com/Venom-Shivu/python-console-games

    **📈 VenomSQL – Executive Analytics Dashboard**  
    Advanced SQL analytics, KPI design, Power BI dashboards  
    🔗 https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard

    **🐍 Python Journey**  
    Python fundamentals, DSA, and problem-solving  
    🔗 https://github.com/Venom-Shivu/My-Python-Journey

    **🗄️ SQL Journey**  
    SQL analytics, query optimization, and practice  
    🔗 https://github.com/Venom-Shivu/MySQL-JOURNEY

    **📚 Python Practice Workbook**  
    Interview prep, statistics, and data science exercises  
    🔗 https://github.com/Venom-Shivu/Comprehensive-Python-Practice-Workbook-Venom
    """)

# ==================================================
# CONTACT SECTION
# ==================================================
elif st.session_state.section == "Contact":

    st.header("📬 Contact Me")

    st.markdown("""
    - **LinkedIn:** https://www.linkedin.com/in/the-venom/  
    - **GitHub:** https://github.com/Venom-Shivu  
    - **Email:** mrshivusinghyadav@gmail.com  
    """)

    st.write("""
    Open to data science, analytics, and machine learning opportunities,
    internships, and collaborative projects.
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption("© 2026 Shivansh Yadav | Built with Python & Streamlit")
