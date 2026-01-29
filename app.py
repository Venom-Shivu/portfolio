import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Shivansh Yadav | Data Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# GLOBAL PATHS
# --------------------------------------------------
DATA_PATH = Path("data/ecommerce_sales_data.csv")
DASHBOARD_IMAGE = Path("images/nexus_dashboard_mockup.png")

# --------------------------------------------------
# HEADER / INTRODUCTION
# --------------------------------------------------
st.title("Shivansh Yadav")
st.subheader("Data Analyst | Python | SQL | Excel | Power BI")

st.write(
    """
    I build data analytics and business intelligence solutions that transform
    raw data into **clear, decision-ready insights**.
    
    This portfolio presents my projects with a focus on:
    - Realistic business problems  
    - Structured analytical workflows  
    - KPI-driven dashboards and insights  
    """
)

st.divider()

# --------------------------------------------------
# ABOUT SECTION
# --------------------------------------------------
st.header("👤 About Me")

st.write(
    """
    I am a data analytics enthusiast focused on **sales performance analysis,
    KPI design, and dashboarding**. My work emphasizes clarity, correctness,
    and business relevance over visual noise.

    I follow an end-to-end analytics approach:
    **Problem → Data → Analysis → Insight → Recommendation**.
    """
)

# --------------------------------------------------
# PROJECTS SECTION
# --------------------------------------------------
st.header("📊 Featured Project")

st.subheader("Nexus Analytics — E-Commerce Performance Dashboard")

st.write(
    """
    **Nexus Analytics** is a professional-grade analytics project focused on
    evaluating e-commerce sales performance across products, regions,
    customer segments, and time.

    The project demonstrates:
    - Analytical problem definition
    - KPI planning and metric design
    - Dataset-driven analysis
    - Executive-style dashboard thinking
    """
)

# --------------------------------------------------
# PROJECT DOCUMENTATION
# --------------------------------------------------
with st.expander("📄 Project Documentation"):
    st.markdown(
        """
        **Problem Statement**  
        Businesses often lack consolidated visibility into revenue, orders,
        customer behavior, and operational performance, limiting data-driven
        decision-making.

        **Proposed Solution**  
        Design and implement an analytics workflow that converts transactional
        data into KPIs, trends, and dashboards to support executive decisions.
        """
    )

# --------------------------------------------------
# DATASET SECTION
# --------------------------------------------------
st.subheader("📁 Dataset Overview")

if DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)

    st.write(
        f"""
        - **Records:** {len(df):,} transactions  
        - **Time Period:** 2022–2024  
        - **Nature:** Synthetic e-commerce sales data  
        """
    )

    with st.expander("🔍 Preview Dataset"):
        st.dataframe(df.head(10), use_container_width=True)
else:
    st.warning("Dataset not found. Please ensure the CSV file exists in /data.")

# --------------------------------------------------
# DASHBOARD BLUEPRINT (IMPORTANT: HONEST LABELING)
# --------------------------------------------------
st.subheader("📌 Dashboard Blueprint (Proposed)")

st.write(
    """
    The following dashboard is a **conceptual design mockup** that defines
    the target KPIs, layout, and analytical structure of the final solution.

    > This is a **planning artifact**, not an output generated from the dataset.
    """
)

if DASHBOARD_IMAGE.exists():
    st.image(
        str(DASHBOARD_IMAGE),
        caption="Proposed KPI & Dashboard Layout (Concept Design)",
        use_column_width=True
    )
else:
    st.info("Dashboard mockup image not found in /images.")

# --------------------------------------------------
# PLANNED KPIs
# --------------------------------------------------
st.subheader("🔑 Planned Key Performance Indicators")

st.markdown(
    """
    **Financial Metrics**
    - Total Revenue
    - Average Order Value (AOV)
    - Revenue Growth (YoY)

    **Customer Metrics**
    - Customer Satisfaction Score
    - Segment-wise Revenue Contribution

    **Operational Metrics**
    - Order Fulfillment Rate
    - Cancellation & Return Rates
    """
)

# --------------------------------------------------
# PROJECT STATUS
# --------------------------------------------------
st.subheader("🚧 Project Status")

st.write(
    """
    **Current Stage:**  
    ✔ Problem definition  
    ✔ Solution planning  
    ✔ KPI & dashboard design  

    **Next Steps:**  
    ⏳ Data cleaning & transformation  
    ⏳ KPI computation using Python  
    ⏳ Interactive Streamlit dashboard implementation  
    """
)

# --------------------------------------------------
# SKILLS SECTION
# --------------------------------------------------
st.header("🧠 Technical Skills")

st.markdown(
    """
    - **Programming:** Python (Pandas, NumPy, Matplotlib)  
    - **Databases:** SQL (Joins, CTEs, Aggregations)  
    - **BI Tools:** Power BI, Microsoft Excel  
    - **Analytics:** KPI design, trend analysis, segmentation  
    - **Visualization:** Executive dashboards & reporting  
    """
)

# --------------------------------------------------
# CONTACT / LINKS
# --------------------------------------------------
st.header("🔗 Connect")

st.markdown(
    """
    - **GitHub:** https://github.com/Venom-Shivu  
    - **LinkedIn:** *(https://www.linkedin.com/in/the-venom/)*  
    - **Email:** *(optional)*  
    """
)

st.divider()

st.caption(
    "© 2026 Shivansh Yadav | Portfolio Project — Built with Python & Streamlit"
)
