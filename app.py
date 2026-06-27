import streamlit as st
import pandas as pd

# --- INITIAL PAGE & CANVAS CONFIGURATION ---
st.set_page_config(
    page_title="Horizon Addis Tyre - Hoshin Kanri Suite",
    page_icon="🎯",
    layout="wide"
)

# --- IMMERSIVE MATTE BLACK THEME WITH EMISSIVE NEON GLOW STYLES ---
st.markdown("""
    <style>
    /* Force Solid Matte Black App Canvas */
    .stApp, [data-testid="stHeader"], header {
        background-color: #000000 !important;
    }
    
    /* Global Element Typography Adjustments */
    p, span, label, th, td, .stMarkdown, h1, h2, h3, h4 {
        color: #FFFFFF !important;
    }
    
    /* Sidebar Matte Black Container Styles */
    [data-testid="stSidebar"] {
        background-color: #0A0A0A !important;
        border-right: 2px solid #222222;
    }
    
    /* --- HOSHIN MATRICES SPECIFIC NEON GLOW CLASSES --- */
    .glow-title-yellow {
        color: #FFFF00 !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFF00, 0 0 20px #CCCC00;
        font-size: 24px !important;
        margin-top: 20px;
    }
    .glow-title-blue {
        color: #00D2FF !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #00D2FF, 0 0 20px #006699;
        font-size: 24px !important;
        margin-top: 20px;
    }
    .glow-title-red {
        color: #FF3333 !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #FF3333, 0 0 20px #990000;
        font-size: 24px !important;
        margin-top: 20px;
    }
    .glow-title-white {
        color: #FFFFFF !important;
        font-family: 'Courier New', monospace;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #888888;
        font-size: 24px !important;
        margin-top: 20px;
    }
    
    /* Segment Framework Block Panels */
    .data-card {
        background-color: #0F0F0F;
        border: 1px solid #262626;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 15px;
    }
    
    /* Core Interlocking Diagram Node Styles */
    .matrix-node {
        border-radius: 4px;
        padding: 10px;
        margin-bottom: 8px;
        font-size: 13px;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

# --- COMPREHENSIVE RAW HOSHIN REGISTRY ENGINE ---
@st.cache_data
def load_structured_hoshin_maps():
    # 1. South Matrix Core
    bottom_5year = [
        {"ID": "1.1", "Pillar": "Supply Chain Enhancement", "Issue": "የግብዓት አቅርቦትን አስተማማኝ ማድረግ (Reliable Raw Material Supply)"},
        {"ID": "2.1", "Pillar": "Capacity Building", "Issue": "የሰው ሀብት አቅም ማሳደግና ማምረቻ መሳሪያዎች አጠቃቀም (HR Capacity & Plant Utilization)"},
        {"ID": "3.1", "Pillar": "Overall Cost Reduction", "Issue": "የምርት ወጪን በከፍተኛ ሁኔታ መቀነስ (Rigorous Production Cost Reduction)"},
        {"ID": "3.2", "Pillar": "Sales & Marketing", "Issue": "የገበያ ድርሻንና የሽያጭ መረብን ማስፋፋት (Market Share Optimization)"}
    ]
    
    # 2. West & East Matrix Core
    annual_kpi_registry = [
        {"KPI_ID": "1.1.1", "Pillar": "Supply Chain Enhancement", "Objective": "ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በክምችት ማሳደግ ከ27.7% ወደ 95%", "Target": 0.95, "Direction": "Up", "Dept": "Purchase"},
        {"KPI_ID": "1.1.2", "Pillar": "Supply Chain Enhancement", "Objective": "የመለዋወጫ አቅርቦት ጊዜ ከ115 ቀን ወደ 21 ቀናት ዝቅ ማድረግ", "Target": 21.0, "Direction": "Down", "Dept": "Plant Engineering"},
        {"KPI_ID": "2.1.1", "Pillar": "Capacity Building", "Objective": "የሠራተኛውን አፈጻጸም ከ82 በመቶ ወደ 95 በመቶ ማሳደግ", "Target": 0.95, "Direction": "Up", "Dept": "HR"},
        {"KPI_ID": "3.1.7", "Pillar": "Overall Cost Reduction", "Objective": "የፈርነስ ፍጆታን (ቶን/ቶን) ከ 0.56 ወደ 0.25 መቀነስ", "Target": 0.25, "Direction": "Down", "Dept": "Production"},
        {"KPI_ID": "3.1.8", "Pillar": "Overall Cost Reduction", "Objective": "ኤሌክትሪክ ፍጆታን በ (KWH/ton) ከ 1529 ወደ 1200 መቀነስ", "Target": 1200.0, "Direction": "Down", "Dept": "Plant Engineering"},
        {"KPI_ID": "3.2.2", "Pillar": "Sales & Marketing", "Objective": "የክሌም ወጪን ከ 0.006% ወደ 0.003% መቀነስ", "Target": 0.003, "Direction": "Down", "Dept": "PIQA"}
    ]
    
    # 3. North Matrix Core
    top_priorities = [
        {"KPI_ID": "1.1.1", "Dept": "Purchase", "Priority": "አምራች አቅራቢዎችን ለይቶ ማወቅ፣ የተሻሉትን መምረጥና በአካል ሄዶ ማነጋገር"},
        {"KPI_ID": "1.1.2", "Dept": "Plant Engineering", "Priority": "ለማምረቻ መሣሪዎችና መገልገያዎች ትክለኛውን ስፔሲፊኬሽን በወቅቱ ማቅረብ"},
        {"KPI_ID": "2.1.1", "Dept": "HR", "Priority": "የሠራተኛውን የሥራ ተነሳሽነትና የባለቤትነት ስሜት (Employee Engagement) ስልጠናዎች መስጠት"},
        {"KPI_ID": "3.1.7", "Dept": "Production", "Priority": "የሃይል አጠቃቀምን መከታተልና ብክነትን ማስወገድ"},
        {"KPI_ID": "3.1.8", "Dept": "Plant Engineering", "Priority": "የማሽነሪዎችን ብቃት ማሳደግና የኃይል ኪሳራዎችን መቆጣጠር"},
        {"KPI_ID": "3.2.2", "Dept": "PIQA", "Priority": "የጥሬ ዕቃዎች ሲመጡ ጥራት ፍተሻ በማድረግ ማረጋገጥ እና የክሌም መነሻዎችን መገምገም"}
    ]
    
    return pd.DataFrame(bottom_5year), pd.DataFrame(annual_kpi_registry), pd.DataFrame(top_priorities)

df_5yr, df_annual, df_priorities = load_structured_hoshin_maps()

# --- RUNTIME MONTHLY METRIC CACHE VALIDATION ---
if "monthly_state" not in st.session_state:
    st.session_state.monthly_state = {
        "1.1.1": 0.65, "1.1.2": 45.0, "2.1.1": 0.88, "3.1.7": 0.40, "3.1.8": 1350.0, "3.2.2": 0.004
    }

# --- SIDEBAR INTERACTIVE TRACKING INTERFACE ---
st.sidebar.markdown("<h2 style='color:#FFFF00; font-weight:900;'>📆 OPERATIONAL UPDATES</h2>", unsafe_allow_html=True)
selected_month = st.sidebar.selectbox("Select Active Business Window:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Update Monthly Performance Status:")

updated_state = {}
for idx, row in df_annual.iterrows():
    kid = row["KPI_ID"]
    current_stored = st.session_state.monthly_state[kid]
    if row["Target"] < 1.0:
        val = st.sidebar.number_input(f"[{kid}] {row['Dept']} Actual:", value=float(current_stored), format="%.4f", step=0.001)
    else:
        val = st.sidebar.number_input(f"[{kid}] {row['Dept']} Actual:", value=float(current_stored), step=1.0)
    updated_state[kid] = val

st.session_state.monthly_state = updated_state

# --- INTERLOCK CALCULATIONS CORE ENGINE ---
def compute_interlocked_score(row):
    act = st.session_state.monthly_state[row["KPI_ID"]]
    tgt = row["Target"]
    if row["Direction"] == "Up":
        return min(max((act / tgt) * 100, 0.0), 120.0) if tgt != 0 else 0
    else:
        return min(max((tgt / act) * 100, 0.0), 120.0) if act != 0 else 0

df_annual["Current_Actual"] = df_annual["KPI_ID"].map(st.session_state.monthly_state)
df_annual["Achievement_%"] = df_annual.apply(compute_interlocked_score, axis=1)

# Map pillars to specified corporate highlight colors
color_map = {
    "Supply Chain Enhancement": "#FFFFFF", # White
    "Capacity Building": "#FFFF00",          # Yellow
    "Overall Cost Reduction": "#00D2FF",     # Blue
    "Sales & Marketing": "#FF3333"           # Red
}

# =========================================================
#   MAIN DASHBOARD DISPLAY RENDER
# =========================================================
st.markdown("<h1 style='text-align:center;'>🎯 HORIZON ADDIS TYRE INTERLOCKED HOSHIN EXECUTIVE SUITE</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#888888;'>Dynamic Operational Interlocking State — Month: <b>{selected_month}</b></p>", unsafe_allow_html=True)
st.markdown("---")

# =========================================================
#   VISUAL LINK MATRIX: WHERE THE INTERLOCKING ARISES FROM
# =========================================================
st.markdown("<h2 style='color:#FFFFFF; border-left: 5px solid #00FF66; padding-left:12px;'>🔄 UNIFIED DIAGRAM: HOW THE MATRIX INTERLOCKS</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#AAAAAA; font-size:14px;'>This structural panel shows how each <b>5-Year Strategic Issue</b> triggers a specific <b>Annual Operational Objective</b>, evaluated via live <b>KPI Metrics</b>, and assigned to a department as a <b>Top Priority Action</b>.</p>", unsafe_allow_html=True)

for idx, row in df_annual.iterrows():
    kid = row["KPI_ID"]
    p_color = color_map.get(row["Pillar"], "#FFFFFF")
    corr_priority = df_priorities[df_priorities["KPI_ID"] == kid]["Priority"].values[0]
    corr_5yr = df_5yr[df_5yr["Pillar"] == row["Pillar"]]["Issue"].values[0]
    
    # Interlinked Node Row Grid View
    g1, g2, g3, g4 = st.columns(4)
    with g1:
        st.markdown(f'<div class="matrix-node" style="background-color:#111; border: 1px solid {p_color};"><span style="color:{p_color}; font-weight:bold;">[SOUTH] 5-Year Strategy:</span><br>{corr_5yr}</div>', unsafe_allow_html=True)
    with g2:
        st.markdown(f'<div class="matrix-node" style="background-color:#111; border: 1px solid {p_color};"><span style="color:{p_color}; font-weight:bold;">[WEST] Annual Objective:</span><br><b>({kid})</b> {row["Objective"]}</div>', unsafe_allow_html=True)
    with g3:
        st.markdown(f'<div class="matrix-node" style="background-color:#111; border: 1px solid {p_color};"><span style="color:{p_color}; font-weight:bold;">[EAST] KPI actual Status:</span><br>Target: {row["Target"]}<br>Actual: <span style="color:#00FF66;"><b>{row["Current_Actual"]}</b></span> ({row["Achievement_%"]:.1f}%)</div>', unsafe_allow_html=True)
    with g4:
        st.markdown(f'<div class="matrix-node" style="background-color:#111; border: 1px solid {p_color};"><span style="color:{p_color}; font-weight:bold;">[NORTH] Priority ({row["Dept"]}):</span><br>{corr_priority}</div>', unsafe_allow_html=True)

st.markdown("---")

# =========================================================
#   THE FOUR SEPARATE STRATEGIC PANELS (ISOLATED DISPLAY)
# =========================================================

# --- 1. TOP PRIORITIES (NORTH) ---
st.markdown('<div class="glow-title-white">⬆️ NORTH PANEL: PRIORITIZED DEPLOYMENT ACTIVITIES (TOP)</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#888888;'>Immediate actionable initiatives executed across factory divisions.</p>", unsafe_allow_html=True)
t_col1, t_col2 = st.columns(2)
for i, row in df_priorities.iterrows():
    target_col = t_col1 if i % 2 == 0 else t_col2
    with target_col:
        st.markdown(f"""
        <div class="data-card">
            <span style='color:#FFFFFF; font-weight:bold; border-bottom: 1px solid #FFF;'>DEPARTMENT: {row['Dept'].upper()}</span>
            <p style='margin-top:8px; font-size:14px; color:#E0E0E0;'>• Link ID {row['KPI_ID']}: {row['Priority']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- 2. ANNUAL OPERATIONAL OBJECTIVES (LEFT) ---
st.markdown('<div class="glow-title-yellow">⬅️ WEST PANEL: ANNUAL BUSINESS OBJECTIVES (LEFT)</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#888888;'>Target milestones established for the current fiscal operational window.</p>", unsafe_allow_html=True)
for idx, row in df_annual.iterrows():
    st.markdown(f"""
    <div class="data-card" style="border-left: 4px solid #FFFF00;">
        <span style="color:#FFFF00; font-weight:bold;">[OBJECTIVE {row['KPI_ID']}]</span> — {row['Objective']}
        <br><span style='color:#888888; font-size:12px;'>Assigned Accountability Matrix Owner: {row['Dept']}</span>
    </div>
    """, unsafe_allow_html=True)

# --- 3. ANNUAL KEY PERFORMANCE INDICATORS (RIGHT) ---
st.markdown('<div class="glow-title-blue">➡️ EAST PANEL: KEY PERFORMANCE INDICATORS (RIGHT)</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#888888;'>Live quantitative tracking vectors with real-time monthly execution records.</p>", unsafe_allow_html=True)
k_col1, k_col2, k_col3 = st.columns(3)
for i, row in df_annual.iterrows():
    target_kcol = k_col1 if i % 3 == 0 else k_col2 if i % 3 == 1 else k_col3
    with target_kcol:
        st.markdown(f"""
        <div class="data-card" style="border-top: 2px solid #00D2FF;">
            <b style="color:#00D2FF;">KPI {row['KPI_ID']} Status Profile</b><br>
            Target Metric: <code style="color:#FFFFFF;">{row['Target']}</code><br>
            Current Actual: <span style="color:#00FF66;"><b>{row['Current_Actual']}</b></span><br>
            Performance Evaluation: <b style="color:#FFFF00;">{row['Achievement_%']:.1f}%</b>
        </div>
        """, unsafe_allow_html=True)

# --- 4. 5-YEAR STRATEGIC ROADMAP (BOTTOM) ---
st.markdown('<div class="glow-title-white">⬇️ SOUTH PANEL: 5-YEAR STRATEGIC MASTER PLAN ISSUES (BOTTOM)</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#888888;'>Long-term strategic pillars anchoring corporate direction.</p>", unsafe_allow_html=True)
for idx, row in df_5yr.iterrows():
    p_color = color_map.get(row["Pillar"], "#FFFFFF")
    st.markdown(f"""
    <div class="data-card" style="border-right: 4px solid {p_color};">
        <span style="color:{p_color}; font-weight:bold;">PILLAR: {row['Pillar'].upper()}</span><br>
        <span style="font-size:15px; color:#FFFFFF;">Strategic Issue: {row['Issue']}</span>
    </div>
    """, unsafe_allow_html=True)
