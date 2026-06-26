import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION & INJECTED IMMERSIVE MATTE BLACK THEME ---
st.set_page_config(
    page_title="Horizon Addis Tyre - Hoshin Kanri Executive Suite",
    page_icon="🎯",
    layout="wide"
)

# --- ADVANCED GLOWING TYPOGRAPHY AND MATTE BLACK STYLES ---
st.markdown("""
    <style>
    /* Force Solid Matte Black App-Wide Canvas */
    .stApp {
        background-color: #0F0F0F !important;
    }
    header, [data-testid="stHeader"] {
        background-color: #0F0F0F !important;
    }
    
    /* Global Text Visibility Improvements for Dark Contrast */
    p, span, label, .stMarkdown, div {
        color: #E5E7EB !important;
    }
    
    /* Interactive Sidebar Matte Dark Adjustments */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A !important;
        border-right: 1px solid #333333;
    }
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p {
        color: #FFFFFF !important;
    }
    
    /* Unified Data Entry Button styling */
    .stButton>button {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: 2px solid #FEF08A !important;
        font-weight: bold;
    }
    
    /* --- THE FOUR CUSTOM SPECIFIED GLOWING HEADERS --- */
    .hoshin-header-1 {
        font-family: 'Courier New', Courier, monospace;
        font-size: 32px !important;
        font-weight: 900 !important;
        color: #FFFF00 !important; /* Yellow */
        text-shadow: 0 0 10px #FFFF00, 0 0 20px #CCCC00;
        letter-spacing: 2px;
        margin-top: 25px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    
    .hoshin-header-2 {
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 28px !important;
        font-weight: 800 !important;
        color: #3B82F6 !important; /* Blue */
        text-shadow: 0 0 10px #3B82F6, 0 0 20px #1D4ED8;
        letter-spacing: 1px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    
    .hoshin-header-3 {
        font-family: 'Lucida Console', Monaco, monospace;
        font-size: 26px !important;
        font-weight: bold !important;
        color: #FFFFFF !important; /* White */
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #9CA3AF;
        border-bottom: 2px dashed #FFFFFF;
        padding-bottom: 5px;
        margin-top: 35px;
        margin-bottom: 20px;
    }
    
    .hoshin-header-4 {
        font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
        font-size: 30px !important;
        font-weight: normal !important;
        color: #FFFFFF !important; /* White */
        text-shadow: 0 0 8px #FFFFFF, 0 0 15px #F3F4F6;
        letter-spacing: 3px;
        margin-top: 35px;
        margin-bottom: 15px;
    }
    
    /* Metrics block styling inside dark mode container */
    div[data-testid="stMetricValue"] > div {
        color: #FFFF00 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATASET PROCESSING ---
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
        "Direction": ["Up", "Down", "Up", "Down", "Down", "Down"],
        "Department": ["Purchase", "Plant Engineering", "HR", "Production", "Plant Engineering", "PIQA"]
    }
    top_priorities = {
        "Department": ["Purchase", "Plant Engineering", "HR", "Production", "PIQA", "Sales & Marketing"],
        "Prioritized Action Item": [
            "አምራች አቅራቢዎችን ለይቶ ማወቅ፣ የተሻሉትን መምረጥና በአካል ሄዶ ማነጋገር",
            "ለማምረቻ መሣሪዎችና መገልገያዎች ትክለኛውን ስፔሲፊኬሽን በወቅቱ ማቅረብ",
            "የሠራተኛውን የሥራ ተነሳሽነትና የባለቤትነት ስሜት ስልጠናዎች መስጠት",
            "የሃይል አጠቃቀምን መከታተልና ብክነትን ማስወገድ",
            "የጥሬ ዕቃዎች ሲመጡ ጥራት ፍተሻ በማድረግ ማረጋገጥ",
            "የገበያ ስለላ (Market Intelligence) ስራን ማጠናከር"
        ]
    }
    return pd.DataFrame(bottom_5yr), pd.DataFrame(left_annual), pd.DataFrame(top_priorities)

df_5yr, df_annual, df_priorities = load_hoshin_base_data()

if "actuals" not in st.session_state:
    st.session_state.actuals = {"1.1.1": 0.88, "1.1.2": 35.0, "2.1.1": 0.89, "3.1.7": 0.32, "3.1.8": 1310.0, "3.2.2": 0.004}

# --- SIDEBAR INTERFACE ---
st.sidebar.markdown("<h2 style='color:#FFFF00;'>🔧 DATA ENTRY GATE</h2>", unsafe_allow_html=True)
selected_dept = st.sidebar.selectbox("Select Submitting Department:", df_priorities["Department"].unique())
dept_metrics = df_annual[df_annual["Department"] == selected_dept]

if not dept_metrics.empty:
    for idx, row in dept_metrics.iterrows():
        kpi_id = row["KPI_ID"]
        current_actual = st.session_state.actuals[kpi_id]
        if row["Target"] < 1.0:
            new_val = st.sidebar.number_input(f"KPI {kpi_id}", value=float(current_actual), step=0.001, format="%.4f")
        else:
            new_val = st.sidebar.number_input(f"KPI {kpi_id}", value=float(current_actual), step=1.0)
        st.session_state.actuals[kpi_id] = new_val

# Calculate updated states
def calculate_achievement(row):
    act = st.session_state.actuals[row["KPI_ID"]]
    tgt = row["Target"]
    if row["Direction"] == "Up":
        score = (act / tgt) * 100 if tgt != 0 else 0
    else:
        score = (tgt / act) * 100 if act != 0 else 0
    return min(max(score, 0.0), 120.0)

df_annual["Actual"] = df_annual["KPI_ID"].map(st.session_state.actuals)
df_annual["Achievement%"] = df_annual.apply(calculate_achievement, axis=1)
overall_score = df_annual["Achievement%"].mean()


# ==========================================
#   RENDER STYLED GLOWING DASHBOARD HEADERS
# ==========================================

# --- HEADER 1 (YELLOW GLOW) ---
st.markdown('<div class="hoshin-header-1">⚡ HEAD 1 // OVERALL COMPANY ACHIEVEMENT INDICATORS</div>', unsafe_allow_html=True)
m_col1, m_col2, m_col3 = st.columns(3)
with m_col1:
    st.metric(label="Global Matrix Execution Rating", value=f"{overall_score:.2f} %")
with m_col2:
    st.metric(label="Interlocked Target Thresholds Met", value=f"{len(df_annual[df_annual['Achievement%']>=90])} / {len(df_annual)}")
with m_col3:
    st.metric(label="Active Plant Tracking Channels", value="6 Departments")

# --- HEADER 2 (BLUE GLOW) ---
st.markdown('<div class="hoshin-header-2">🗺️ Head 2 // Balanced Four Categories Breakdown</div>', unsafe_allow_html=True)
tabs = st.tabs(["Supply Chain Enhancement", "Capacity Building", "Overall Cost Reduction", "Sales & Marketing"])
for tab, pillar in zip(tabs, df_5yr["Pillar"].unique()):
    with tab:
        st.markdown(f"<p style='color:#3B82F6; font-weight:bold;'>5-Year Objective Context: {df_5yr[df_5yr['Pillar']==pillar]['Strategy Issue'].values[0]}</p>", unsafe_allow_html=True)
        pillar_annual = df_annual[df_annual["Parent_Pillar"] == pillar]
        for idx, row in pillar_annual.iterrows():
            c_lbl, c_tgt, c_act = st.columns([5, 3, 2])
            with c_lbl:
                st.markdown(f"• **[{row['KPI_ID']}]** {row['Objective']}")
            with c_tgt:
                st.markdown(f"Target Threshold: `<code style='color:#3B82F6;'>{row['Target']}</code>`", unsafe_allow_html=True)
            with c_act:
                st.markdown(f"Current Performance: **{row['Achievement%']:.1f}%**")

# --- HEADER 3 (WHITE GLOW TYPE A) ---
st.markdown('<div class="hoshin-header-3">🔄 Head 3 // Interlinked Cross-Matrix Verification Layout</div>', unsafe_allow_html=True)
x_matrix_simulation = df_annual.merge(df_priorities, on="Department", how="left")
st.dataframe(
    x_matrix_simulation[[
        "Parent_Pillar", "KPI_ID", "Objective", "Target", "Actual", "Achievement%", "Department", "Prioritized Action Item"
    ]].rename(columns={
        "Parent_Pillar": "SOUTH (5-Yr Strategic Pillar)",
        "Objective": "WEST (Annual Matrix Objective)",
        "Target": "EAST Target Value",
        "Actual": "EAST Operational Actual",
        "Achievement%": "Performance Metric %",
        "Department": "NORTH Assigned Owner",
        "Prioritized Action Item": "NORTH (Prioritized Issue)"
    }),
    use_container_width=True,
    hide_index=True
)

# --- HEADER 4 (WHITE GLOW TYPE B) ---
st.markdown('<div class="hoshin-header-4">🎯 HEAD 4 // PRIORITIZED ISSUES EXTRACTION LOG</div>', unsafe_allow_html=True)
for idx, row in df_priorities.iterrows():
    st.markdown(f"""
    <div style='border: 1px solid #333; padding: 12px; margin-bottom: 8px; background-color: #141414;'>
        <span style='color:#FFFF00; font-weight:bold;'>[DEPT: {row['Department']}]</span> 
        <span style='color:#FFFFFF;'>{row['Prioritized Action Item']}</span>
    </div>
    """, unsafe_allow_html=True)    
