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
# HEADER WITH PROFILE IMAGE + RESUME BUTTON
# --------------------------------------------------
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if os.path.exists("images/profile.jpeg"):
        st.image("images/profile.jpeg", width=160)
    else:
        st.warning("Profile image not found")

with col2:
    st.title("Shivansh Yadav")
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Visualization")
    st.write("""
    I design **data-driven solutions** that convert raw data into reliable insights
    and scalable systems, prioritizing clarity, performance, and durability.
    """)

with col3:
    if os.path.exists("resume/Shivansh_Yadav_Resume.pdf"):
        with open("resume/Shivansh_Yadav_Resume.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="Shivansh_Yadav_Resume.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Resume not found")

st.divider()

# ==================================================
# ABOUT SECTION
# ==================================================
if st.session_state.section == "About":

    st.header("👋 About Me")

    st.write("""
    I work across the **full data lifecycle** — from high-performance SQL extraction
    and Python-based analysis to dashboarding and machine learning model development.

    I value **correctness, efficiency, and long-term maintainability** over flashy
    or over-engineered solutions.
    """)

    st.subheader("🧠 Technical Stack")

    st.markdown("""
    **Programming & Data Engineering**
    - Python (Pandas, NumPy)
    - SQL (Advanced Analytics, Optimization)
    - Data Structures & Algorithms

    **Machine Learning & AI**
    - Scikit-learn, TensorFlow, PyTorch
    - Classical ML & Deep Learning
    - Generative AI & Prompt Engineering

    **Analytics & Visualization**
    - Power BI, Tableau
    - DAX & KPI Design
    - Excel, Jupyter
    """)

    st.subheader("🏆 HackerRank Achievements")

    st.markdown("""
    **HackerRank Profile:**  
    🔗 https://www.hackerrank.com/profile/Venom001  

    **Badges**
    - ⭐⭐⭐⭐⭐ **Python – Gold Badge**
    - ⭐⭐⭐⭐⭐ **SQL – Gold Badge**
    - ⭐⭐⭐⭐⭐ **Problem Solving – Gold Badge**

    **Certifications**
    - SQL (Basic, Intermediate, Advanced) – *All challenges completed*
    - Python (Basic)
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

    st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")

    st.write("""
    A professional analytics project evaluating e-commerce performance across
    revenue, customers, regions, and operations using KPI-driven analysis and
    executive dashboard design.
    """)

    st.markdown("""
    **Core Areas**
    - Sales & revenue analysis
    - KPI planning & metric design
    - Dashboard blueprinting
    - Business insight generation
    """)

    if os.path.exists("images/nexus_dashboard_mockup.png"):
        st.image(
            "images/nexus_dashboard_mockup.png",
            caption="Proposed KPI & Dashboard Layout (Concept Design)",
            use_container_width=True
        )

    st.markdown("🔗 https://github.com/Venom-Shivu/portfolio")

    st.divider()

    st.subheader("📁 Other Notable Repositories")

    st.markdown("""
    **🎮 Python Console Games**  
    https://github.com/Venom-Shivu/python-console-games  

    **📈 VenomSQL – Executive Analytics Dashboard**  
    https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard  

    **🐍 Python Journey**  
    https://github.com/Venom-Shivu/My-Python-Journey  

    **🗄️ SQL Journey**  
    https://github.com/Venom-Shivu/MySQL-JOURNEY  

    **📚 Python Practice Workbook**  
    https://github.com/Venom-Shivu/Comprehensive-Python-Practice-Workbook-Venom  
    """)

# ==================================================
# CONTACT SECTION
# ==================================================
elif st.session_state.section == "Contact":

    st.header("📬 Contact Me")

    st.markdown("""
    - **LinkedIn:** https://www.linkedin.com/in/the-venom/  
    - **GitHub:** https://github.com/Venom-Shivu  
    - **HackerRank:** https://www.hackerrank.com/profile/Venom001  
    - **Email:** mrshivusinghyadav@gmail.com  
    """)

    st.write("""
    Open to **Data Science, Analytics, and Machine Learning roles**,
    internships, and high-impact collaborations.
    """)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption("© 2026 Shivansh Yadav | Built with Python & Streamlit")
