import streamlit as st
import pandas as pd

# --- INITIAL PAGE AND BLACK CANVAS CONFIGURATION ---
st.set_page_config(
    page_title="Horizon Addis Tyre - Dynamic Hoshin Suite",
    page_icon="🎯",
    layout="wide"
)

# --- STRICT MATTE BLACK THEME & GLOWING PILLAR TYPOGRAPHY INJECTION ---
st.markdown("""
    <style>
    /* Absolute Matte Black Canvas */
    .stApp, [data-testid="stHeader"], header {
        background-color: #000000 !important;
    }
    
    /* Global Content Contrast Controls */
    p, span, label, th, td, .stMarkdown {
        color: #FFFFFF !important;
    }
    
    /* Dark Entry Sidebar Custom Parameters */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-right: 2px solid #222222;
    }
    
    /* --- PILLAR SPECIFIC NEON GLOW CLASSES --- */
    .glow-supply-chain {
        color: #FFFFFF !important;
        font-family: 'Courier New', monospace;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFFFF, 0 0 20px #888888;
        font-size: 24px !important;
    }
    .glow-capacity {
        color: #FFFF00 !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFF00, 0 0 20px #BBBB00;
        font-size: 24px !important;
    }
    .glow-cost {
        color: #00D2FF !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #00D2FF, 0 0 20px #006699;
        font-size: 24px !important;
    }
    .glow-sales {
        color: #FF3333 !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #FF3333, 0 0 20px #990000;
        font-size: 24px !important;
    }
    
    /* Corporate Health Score */
    .corporate-score {
        font-size: 48px !important;
        font-weight: bold;
        color: #00FF66 !important;
        text-shadow: 0 0 15px #00FF66;
        text-align: center;
        padding: 10px;
    }
    
    /* Visual Diagram Layout Cells */
    .diagram-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-bottom: 30px;
    }
    .diagram-card {
        background-color: #111111;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- READ AND MAP REAL HISTORICAL RAW STRUCTURES ---
@st.cache_data
def ingest_hoshin_framework():
    pillars = {
        "Supply Chain Enhancement": {"color": "white", "glow": "glow-supply-chain", "desc": "የግብዓት አቅርቦትን አስተማማኝ ማድረግ (Reliable Raw Material Pipeline)"},
        "Capacity Building": {"color": "yellow", "glow": "glow-capacity", "desc": "የሰው ሀብት አቅም ማሳደግና መሳሪያዎች አጠቃቀም (HR Capacity & Plant Utilization)"},
        "Overall Cost Reduction": {"color": "blue", "glow": "glow-cost", "desc": "የምርት ወጪን በከፍተኛ ሁኔታ መቀነስ (Rigorous Cost Reduction)"},
        "Sales & Marketing": {"color": "red", "glow": "glow-sales", "desc": "የገበያ ድርሻንና የሽያጭ መረብን ማስፋፋት (Market Share Optimization)"}
    }
    
    kpi_registry = [
        {"KPI_ID": "1.1.1", "Pillar": "Supply Chain Enhancement", "Objective": "ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በክምችት ማሳደግ ከ27.7% ወደ 95%", "Target": 0.95, "Direction": "Up", "Dept": "Purchase"},
        {"KPI_ID": "1.1.2", "Pillar": "Supply Chain Enhancement", "Objective": "የመለዋወጫ አቅርቦት ጊዜ ከ115 ቀን ወደ 21 ቀናት ዝቅ ማድረግ", "Target": 21.0, "Direction": "Down", "Dept": "Plant Engineering"},
        {"KPI_ID": "2.1.1", "Pillar": "Capacity Building", "Objective": "የሠራተኛውን አፈጻጸም ከ82 በመቶ ወደ 95 በመቶ ማሳደግ", "Target": 0.95, "Direction": "Up", "Dept": "HR"},
        {"KPI_ID": "3.1.7", "Pillar": "Overall Cost Reduction", "Objective": "የፈርነስ ፍጆታን (ቶን/ቶን) ከ 0.56 ወደ 0.25 መቀነስ", "Target": 0.25, "Direction": "Down", "Dept": "Production"},
        {"KPI_ID": "3.1.8", "Pillar": "Overall Cost Reduction", "Objective": "ኤሌክትሪክ ፍጆታን በ (KWH/ton) ከ 1529 ወደ 1200 መቀነስ", "Target": 1200.0, "Direction": "Down", "Dept": "Plant Engineering"},
        {"KPI_ID": "3.2.2", "Pillar": "Sales & Marketing", "Objective": "የክሌም ወጪን ከ 0.006% ወደ 0.003% መቀነስ", "Target": 0.003, "Direction": "Down", "Dept": "PIQA"}
    ]
    return pillars, pd.DataFrame(kpi_registry)

pillars_meta, df_kpis = ingest_hoshin_framework()

# --- STEP 1: INTERACTIVE MONTHLY KPI PERFORMANCE UPDATER (SIDEBAR) ---
st.sidebar.markdown("<h2 style='color:#00FF66; text-shadow: 0 0 10px #00FF66;'>📆 MONTHLY TRACKING GATE</h2>", unsafe_allow_html=True)
selected_month = st.sidebar.selectbox("Select Business Tracking Month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

st.sidebar.markdown("---")
st.sidebar.markdown("#### Input Operational Actuals:")

# Dynamic state tracking key based on selected month
if "monthly_state" not in st.session_state:
    st.session_state.monthly_state = {
        "1.1.1": 0.45, "1.1.2": 80.0, "2.1.1": 0.85, "3.1.7": 0.45, "3.1.8": 1400.0, "3.2.2": 0.005
    }

# Render inputs inside sidebar safely
updated_actuals = {}
for idx, row in df_kpis.iterrows():
    kid = row["KPI_ID"]
    prev_val = st.session_state.monthly_state[kid]
    
    if row["Target"] < 1.0:
        val = st.sidebar.number_input(f"[{kid}] ({row['Dept']})", value=float(prev_val), format="%.4f", step=0.001)
    else:
        val = st.sidebar.number_input(f"[{kid}] ({row['Dept']})", value=float(prev_val), step=1.0)
    updated_actuals[kid] = val

# Save to state tracking array
st.session_state.monthly_state = updated_actuals

# --- CORE MATHS ENGINE: COMPUTE INTERLOCKED ACHIEVEMENT ---
def engine_achievement(row):
    act = st.session_state.monthly_state[row["KPI_ID"]]
    tgt = row["Target"]
    if row["Direction"] == "Up":
        score = (act / tgt) * 100 if tgt != 0 else 0
    else:
        score = (tgt / act) * 100 if act != 0 else 0
    return min(max(score, 0.0), 120.0)

df_kpis["Current_Actual"] = df_kpis["KPI_ID"].map(st.session_state.monthly_state)
df_kpis["Achievement_Pct"] = df_kpis.apply(engine_achievement, axis=1)
global_corporate_health = df_kpis["Achievement_Pct"].mean()


# =========================================================
#   DASHBOARD VISUAL INTERFACE
# =========================================================

st.markdown(f"<h1 style='text-align:center; color:#FFFFFF;'>🎯 HORIZON ADDIS TYRE INTERLOCKED HOSHIN EXECUTIVE SUITE</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#888888; font-size:16px;'>Active Window Segment: <b>{selected_month} Deployment Cycle</b></p>", unsafe_allow_html=True)

# --- HEAD 1: SEPARATE OVERALL COMPANY ACHIEVEMENT INDICATOR ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #00FF66; padding-left:10px;'>📊 HEAD 1 // GLOBAL CORPORATE PERFORMANCE STATUS</h3>", unsafe_allow_html=True)
c_col1, c_col2 = st.columns([1, 2])
with c_col1:
    st.markdown(f'<div class="corporate-score">{global_corporate_health:.2f}%</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888888;'>Interlocked Company Alignment Index</p>", unsafe_allow_html=True)
with c_col2:
    st.markdown("<p style='margin-top:15px;'>All structural indices are cross-compiled instantly upon entry changes. Operational targets align with the 5-Year Master strategic roadmaps.</p>", unsafe_allow_html=True)

st.markdown("---")

# --- HEAD 2: ALL-IN-ONE VISUAL HOSHIN DIAGRAM CARD SYSTEM ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #FFFFFF; padding-left:10px;'>🔄 HEAD 2 // UNIFIED ALL-IN-ONE COMPACT X-MATRIX VISUAL DIAGRAM</h3>", unsafe_allow_html=True)

st.markdown('<div class="diagram-container">', unsafe_allow_html=True)

for p_name, meta in pillars_meta.items():
    p_kpis = df_kpis[df_kpis["Pillar"] == p_name]
    avg_perf = p_kpis["Achievement_Pct"].mean() if not p_kpis.empty else 0.0
    
    st.markdown(f"""
    <div class="diagram-card">
        <div class="{meta['glow']}">{p_name}</div>
        <p style='font-size:12px; color:#A0A0A0; margin:10px 0;'>{meta['desc']}</p>
        <h2 style='color:#FFFFFF; margin:5px 0;'>{avg_perf:.1f}%</h2>
        <div style='background-color:#222; border-radius:4px; height:6px;'>
            <div style='background-color:{"#FFFFFF" if meta["color"]=="white" else "#FFFF00" if meta["color"]=="yellow" else "#00D2FF" if meta["color"]=="blue" else "#FF3333"}; width:{min(avg_perf,100)}%; height:100%; border-radius:4px;'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

# --- HEAD 3: FOUR SEPARATE STRATEGIC PILLARS BREAKDOWN HEADERS ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #00D2FF; padding-left:10px;'>🎯 HEAD 3 // SEPARATED OPERATIONS SECTOR PERFORMANCE VIEWS</h3>", unsafe_allow_html=True)

for p_name, meta in pillars_meta.items():
    st.markdown(f'<div class="{meta["glow"]}" style="margin-top:20px; margin-bottom:10px;">• {p_name.upper()} PILLAR LAYER</div>', unsafe_allow_html=True)
    
    p_kpis = df_kpis[df_kpis["Pillar"] == p_name]
    if p_kpis.empty:
        st.caption("No indicators linked directly in this matrix track.")
    else:
        for idx, row in p_kpis.iterrows():
            r1, r2, r3, r4 = st.columns([4, 2, 2, 2])
            with r1:
                st.markdown(f"ID: `{row['KPI_ID']}` | **{row['Objective']}**")
            with r2:
                st.markdown(f"Target Line: `{row['Target']}`")
            with r3:
                st.markdown(f"Actual Input: <span style='color:#00FF66;'><b>{row['Current_Actual']}</b></span>", unsafe_allow_html=True)
            with r4:
                st.markdown(f"Status Rating: **{row['Achievement_Pct']:.1f}%**")

st.markdown("---")

# --- HEAD 4: INTERLINKED INTEGRATED LOG VERIFICATION TABLE ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #FF3333; padding-left:10px;'>📊 HEAD 4 // LIVE INTERLOCKED OPERATIONAL MATRIX LOG</h3>", unsafe_allow_html=True)

# Format lookups to clean dataset display bounds
df_display = df_kpis.copy()
df_display.columns = ["KPI ID", "Strategic Pillar Location", "Annual Executive Objective", "Target Threshold", "Tracking Direction", "Responsible Department", "Monthly Actual Status", "Achievement Performance %"]

st.dataframe(
    df_display[["KPI ID", "Strategic Pillar Location", "Annual Executive Objective", "Target Threshold", "Responsible Department", "Monthly Actual Status", "Achievement Performance %"]],
    use_container_width=True,
    hide_index=True
)
