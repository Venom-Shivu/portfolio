import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Shivansh Yadav | Data & Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# GLOBAL ANALYTICAL THEME (NO SEPARATORS)
# --------------------------------------------------
st.markdown("""
<style>
.block-container { padding-top: 1.5rem; }
hr { display: none; }

.stApp {
    background: radial-gradient(circle at 20% 10%, #111827 0%, #0b0f14 45%, #0a0d12 100%);
}

h1, h2, h3 { color: #f9fafb; }
p, li { color: #9ca3af; line-height: 1.75; }

.card {
    background: rgba(255,255,255,0.03);
    border-radius: 12px;
    padding: 24px;
    margin-top: 22px;
}

.icon-btn a {
    display: inline-block;
    margin-top: 8px;
    margin-right: 10px;
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.15);
    color: #e5e7eb;
    text-decoration: none;
    font-weight: 600;
}

.icon-btn a:hover {
    background: rgba(255,255,255,0.08);
}

img { border-radius: 14px; }
</style>
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
    st.subheader("Data Scientist | Machine Learning | Data Analytics & Business Intelligence")
    st.write(
        "I design and build data-driven systems that convert raw data into "
        "decision-ready insights using advanced analytics, SQL, and machine learning."
    )

# ==================================================
# ABOUT ME (EXPANDED, HONEST, PROFESSIONAL)
# ==================================================
st.header("About Me")

st.write("""
I am a **data analytics and data science professional** with strong hands-on mastery
in **Python and SQL**, and deep experience across **Business Analytics, BI, and foundational
Machine Learning**.

I work across the **entire analytics lifecycle** — from raw data extraction and modeling,
to KPI definition, dashboarding, statistical analysis, and predictive insights.
""")

st.markdown("""
### 🔹 Advanced Technical Skills

**🐍 Python (Advanced)**
- Pandas, NumPy for large-scale data analysis  
- End-to-end analytical pipelines  
- Feature engineering & model evaluation  
- Clean, maintainable, production-oriented code  

**🗄️ SQL (Advanced)**
- Complex joins, CTEs, subqueries  
- Window functions & analytical aggregations  
- KPI computation & metric validation  
- Query optimization & performance tuning  

**📊 Business & Data Analytics**
- KPI framework design  
- Metric ownership & validation  
- Requirements gathering  
- Translating business questions into data solutions  

**📈 BI & Reporting**
- Power BI dashboards & data modeling  
- DAX measures & calculated metrics  
- Executive reporting & storytelling  
- Excel (advanced pivots, analytics, validation)  

**🤖 Machine Learning (Foundational–Applied)**
- Supervised learning (regression, classification)  
- Unsupervised learning (clustering, segmentation)  
- Model evaluation & bias–variance trade-offs  
- ML for decision support, not academic demos  

**📐 Statistics & Hypothesis Testing**
- Descriptive & inferential statistics  
- Probability distributions  
- Hypothesis testing (A/B testing, t-test, chi-square)  
- Confidence intervals & statistical significance  
""")

st.markdown("""
**Coding Credentials**
- ⭐⭐⭐⭐⭐ Python – HackerRank (Gold)  
- ⭐⭐⭐⭐⭐ SQL – HackerRank (Gold)  
- ⭐⭐⭐⭐⭐ Problem Solving – HackerRank (Gold)  
- SQL Certified: Basic, Intermediate, Advanced  
- Python Certified: Basic  
""")

# ==================================================
# VENOMSQL — LIVE KPIs & ANALYTICS
# ==================================================
st.header("VenomSQL — Executive Analytics Dashboard (Live Demo)")

st.write("""
This section demonstrates **live KPI computation and analytics logic**
similar to what is implemented in VenomSQL using SQL-first thinking.
""")

# -------------------------
# Simulated Business Data
# -------------------------
np.random.seed(42)

orders = pd.DataFrame({
    "order_id": range(1, 501),
    "order_date": pd.date_range("2024-01-01", periods=500, freq="D"),
    "revenue": np.random.gamma(2.0, 150.0, 500),
    "region": np.random.choice(["North", "South", "East", "West"], 500),
    "customer_type": np.random.choice(["New", "Returning"], 500)
})

# -------------------------
# KPIs (SQL-like logic)
# -------------------------
total_revenue = orders["revenue"].sum()
total_orders = orders["order_id"].nunique()
avg_order_value = total_revenue / total_orders
returning_rate = (
    orders[orders["customer_type"] == "Returning"].shape[0] / total_orders
) * 100

# -------------------------
# KPI CARDS
# -------------------------
k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Revenue", f"${total_revenue:,.0f}")
k2.metric("Total Orders", total_orders)
k3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
k4.metric("Returning Customer %", f"{returning_rate:.1f}%")

# ==================================================
# REAL CHARTS (EXECUTIVE ANALYTICS)
# ==================================================
st.subheader("Revenue Analysis")

# Revenue trend
rev_trend = orders.groupby("order_date")["revenue"].sum().reset_index()
fig_trend = px.line(
    rev_trend,
    x="order_date",
    y="revenue",
    title="Revenue Trend Over Time"
)
st.plotly_chart(fig_trend, use_container_width=True)

# Revenue by region
rev_region = orders.groupby("region")["revenue"].sum().reset_index()
fig_region = px.bar(
    rev_region,
    x="region",
    y="revenue",
    title="Revenue by Region",
    text_auto=True
)
st.plotly_chart(fig_region, use_container_width=True)

# Customer segmentation
cust_seg = orders.groupby("customer_type")["revenue"].sum().reset_index()
fig_cust = px.pie(
    cust_seg,
    names="customer_type",
    values="revenue",
    title="Revenue by Customer Type"
)
st.plotly_chart(fig_cust, use_container_width=True)

st.markdown("""
<div class="icon-btn">
<a href="https://github.com/Venom-Shivu/VenomSQL-Executive-Analytics-Dashboard" target="_blank">
View VenomSQL Repository
</a>
</div>
""", unsafe_allow_html=True)

# ==================================================
# CONTACT
# ==================================================
st.header("Contact & Opportunities")

st.write("""
I am open to **Data Analyst, Business Analyst, Data Scientist, and ML-focused roles**,
including internships, full-time opportunities, and real-world analytics projects.

If your work involves **SQL-heavy analytics, KPI ownership, dashboards, or applied ML**,
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

st.caption("© 2026 Shivansh Yadav | Data & Analytics Portfolio")
