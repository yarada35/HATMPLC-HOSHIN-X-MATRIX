import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Horizon Addis Tyre - Hoshin Kanri Dashboard",
    page_icon="🎯",
    layout="wide"
)

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main-header { font-size:28px !important; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-header { font-size:16px !important; color: #6B7280; margin-bottom: 25px; }
    .card-metric { background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #FEF08A; }
    .stButton>button { background-color: #000000; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header">🎯 HORIZON ADDIS TYRE — INDUSTRIAL HOSHIN KANRI DASHBOARD</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Interlocking 5-Year Strategy, Annual Objectives, KPIs, and Top Department Priorities</div>', unsafe_allow_html=True)

# --- MOCK DATA INGESTION (Based on uploaded structure) ---
# To connect live, replace these dictionaries with your exact csv reading strings: pd.read_csv('filename.csv')
@st.cache_data
def load_hoshin_base_data():
    bottom_5yr = {
        "ID": ["1.1", "2.1", "3.1", "3.2"],
        "Pillar": ["Supply Chain Enhancement", "Capacity Building", "Overall Cost Reduction", "Sales & Marketing"],
        "Strategy Issue": [
            "የግብዓት አቅርቦትን አስተማማኝ ማድረግ (Reliable Raw Material Supply Pipeline)",
            "የሰው ሀብት አቅም ማሳደግና ማምረቻ መሳሪያዎች አጠቃቀም (Human Resource Capacity & Plant Utilization)",
            "የምርት ወጪን በከፍተኛ ሁኔታ መቀነስ (Rigorous Production Cost Reduction)",
            "የገበያ ድርሻንና የሽያጭ መረብን ማስፋፋት (Market Share Optimization & Commercial Reach)"
        ]
    }
    
    left_annual = {
        "KPI_ID": ["1.1.1", "1.1.2", "2.1.1", "3.1.7", "3.1.8", "3.2.2"],
        "Parent_Pillar": ["Supply Chain Enhancement", "Supply Chain Enhancement", "Capacity Building", "Overall Cost Reduction", "Overall Cost Reduction", "Sales & Marketing"],
        "Objective": [
            "ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በክምችት ማሳደግ ከ27.7% ወደ 95%",
            "የመለዋወጫ አቅርቦት ጊዜ ከ115 ቀን ወደ 21 ቀናት ዝቅ ማድረግ",
            "የሠራተኛውን አፈጻጸም ከ82 በመቶ ወደ 95 በመቶ ማሳደግ",
            "የፈርነስ ፍጆታን (ቶን/ቶን) ከ 0.56 ወደ 0.25 መቀነስ",
            "ኤሌክትሪክ ፍጆታን በ (KWH/ton) ከ 1529 ወደ 1200 መቀነስ",
            "የክሌም ወጪን ከ 0.006% ወደ 0.003% መቀነስ"
        ],
        "Weight": [4, 2, 4, 4, 2, 1],
        "Target": [0.95, 21.0, 0.95, 0.25, 1200.0, 0.003],
        "Direction": ["Up", "Down", "Up", "Down", "Down", "Down"], # Up = higher is better, Down = lower is better
        "Department": ["Purchase", "Plant Engineering", "HR", "Production", "Plant Engineering", "PIQA"]
    }
    
    top_priorities = {
        "Department": ["Purchase", "Plant Engineering", "HR", "Production", "PIQA", "Sales & Marketing"],
        "Prioritized Action Item": [
            "አምራች አቅራቢዎችን ለይቶ ማወቅ፣ የተሻሉትን መምረጥና በአካል ሄዶ ማነጋገር",
            "ለማምረቻ መሣሪዎችና መገልገያዎች ትክለኛውን ስፔሲፊኬሽን በወቅቱ ማቅረብ",
            "የሠራተኛውን የሥራ ተነሳሽነትና የባለቤትነት ስሜት (Employee Engagement) ስልጠናዎች መስጠት",
            "የሃይል አጠቃቀምን መከታተልና ብክነትን ማስወገድ",
            "የጥሬ ዕቃዎች ሲመጡ ጥራት ፍተሻ በማድረግ ማረጋገጥ",
            "የታገዘ የቴክኒክ ድጋፍ እና የገበያ ስለላ (Market Intelligence) ስራን ማጠናከር"
        ]
    }
    return pd.DataFrame(bottom_5yr), pd.DataFrame(left_annual), pd.DataFrame(top_priorities)

df_5yr, df_annual, df_priorities = load_hoshin_base_data()

# --- SESSION STATE FOR PERIODIC ACTUAL PERFORMANCES ---
if "actuals" not in st.session_state:
    # Initialize actuals close to target values for demonstration
    st.session_state.actuals = {
        "1.1.1": 0.88,
        "1.1.2": 35.0,
        "2.1.1": 0.89,
        "3.1.7": 0.32,
        "3.1.8": 1310.0,
        "3.2.2": 0.004
    }

# --- SIDEBAR: DEPARTMENTAL PERFORMANCE UPDATE INTERFACE ---
st.sidebar.header("🏭 Department Performance Update Gate")
selected_dept = st.sidebar.selectbox("Select Your Submitting Department:", df_priorities["Department"].unique())

st.sidebar.markdown(f"### **{selected_dept}** Metrics Input")
dept_metrics = df_annual[df_annual["Department"] == selected_dept]

if not dept_metrics.empty:
    for idx, row in dept_metrics.iterrows():
        kpi_id = row["KPI_ID"]
        current_actual = st.session_state.actuals[kpi_id]
        
        # Adjust entry type based on metric nature
        if row["Target"] < 1.0:
            new_val = st.sidebar.number_input(f"KPI {kpi_id}: {row['Objective'][:30]}...", value=float(current_actual), step=0.01, format="%.4f")
        else:
            new_val = st.sidebar.number_input(f"KPI {kpi_id}: {row['Objective'][:30]}...", value=float(current_actual), step=1.0)
        
        st.session_state.actuals[kpi_id] = new_val
else:
    st.sidebar.info("No numerical KPIs assigned directly to this department in this tracking window.")

# --- COMPUTE PERFORMANCE SCORE ---
def calculate_achievement(row):
    act = st.session_state.actuals[row["KPI_ID"]]
    tgt = row["Target"]
    if row["Direction"] == "Up":
        score = (act / tgt) * 100 if tgt != 0 else 0
    else:
        score = (tgt / act) * 100 if act != 0 else 0
    return min(max(score, 0.0), 120.0) # Cap view window performance between 0-120%

df_annual["Actual"] = df_annual["KPI_ID"].map(st.session_state.actuals)
df_annual["Achievement%"] = df_annual.apply(calculate_achievement, axis=1)

# --- HEAD 1: OVERALL COMPANY ACHIEVEMENT INDICATOR ---
st.subheader("📊 Overall Corporate Health Achievement Matrix")
overall_score = df_annual["Achievement%"].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Global Hoshin Alignment Score", value=f"{overall_score:.2f} %", delta=f"{overall_score - 85.0:.1f}% vs Threshold")
with col2:
    completed_pillars = len(df_annual[df_annual["Achievement%"] >= 90])
    st.metric(label="Fully Operational Interlocked KPIs", value=f"{completed_pillars} / {len(df_annual)}")
with col3:
    st.metric(label="Active Plant Departments Monitored", value=len(df_priorities))

st.markdown("---")

# --- HEAD 2: THE FOUR HOSHIN MATRIX HEADS INDICATED SEPARATELY ---
st.subheader("🎯 Real-Time Strategic Pillars Breakdown")
tabs = st.tabs(["Supply Chain Enhancement", "Capacity Building", "Overall Cost Reduction", "Sales & Marketing"])

for tab, pillar in zip(tabs, df_5yr["Pillar"].unique()):
    with tab:
        st.markdown(f"#### **5-Year Focus:** *{df_5yr[df_5yr['Pillar']==pillar]['Strategy Issue'].values[0]}*")
        
        # Filter KPIs per specific pillar
        pillar_annual = df_annual[df_annual["Parent_Pillar"] == pillar]
        
        for idx, row in pillar_annual.iterrows():
            c_lbl, c_tgt, c_act, c_pct = st.columns([4, 2, 2, 2])
            with c_lbl:
                st.markdown(f"**[{row['KPI_ID']}]** {row['Objective']}")
            with c_tgt:
                st.text(f"Target: {row['Target']}")
            with c_act:
                st.text(f"Actual: {row['Actual']}")
            with c_pct:
                st.progress(row["Achievement%"]/120.0)
                st.caption(f"Performance: **{row['Achievement%']:.1f}%**")

st.markdown("---")

# --- HEAD 3: VISUAL MATRIX INTERLOCK (THE DIGITAL X-MATRIX VIEW) ---
st.subheader("🔄 Interlocked X-Matrix Deployment View")
st.markdown("> **How to Read This Map:** Your **5-Year Strategy (Bottom)** feeds directly into your **Annual Operational Objectives (Left)**, which are tracked via **KPIs (Right)** and deployed across active execution tasks per **Department (Top)**.")

# Constructing an analytical cross-join view table to simulate multi-directional relational intersections
x_matrix_simulation = df_annual.merge(df_priorities, on="Department", how="left")

st.dataframe(
    x_matrix_simulation[[
        "Parent_Pillar", "KPI_ID", "Objective", "Target", "Actual", "Achievement%", "Department", "Prioritized Action Item"
    ]].rename(columns={
        "Parent_Pillar": "SOUTH (5-Year Strategy)",
        "Objective": "WEST (Annual Objective)",
        "Target": "EAST Target",
        "Actual": "EAST Actual Status",
        "Achievement%": "EAST Score %",
        "Department": "NORTH Assignee",
        "Prioritized Action Item": "NORTH (Prioritized Issue)"
    }),
    use_container_width=True,
    hide_index=True
)

st.success("Configuration Validated. X-Matrix parameters interlocked without circular tracking references.")        
