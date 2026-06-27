import streamlit as st
import pandas as pd

# --- STAGE CONFIGURATION & SOLID BLACK BACKDROP ---
st.set_page_config(
    page_title="Horizon Addis Tyre - Hoshin Executive Matrix",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
    <style>
    /* Force Deep Matte Black App-wide Canvas */
    .stApp, [data-testid="stHeader"], header {
        background-color: #000000 !important;
    }
    
    /* Global Content Contrast Controls */
    p, span, label, th, td, .stMarkdown, h1, h2, h3, h4, li {
        color: #FFFFFF !important;
    }
    
    /* Interactive Dropdown (Expander) Custom Frame Headers */
    .stAccordion {
        background-color: #0B0B0B !important;
        border: 1px solid #222222 !important;
        margin-bottom: 10px !important;
    }
    
    /* Emissive Typography Rules per Pillar */
    .glow-white {
        color: #FFFFFF !important;
        font-family: 'Courier New', monospace;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFFFF, 0 0 15px #888888;
    }
    .glow-yellow {
        color: #FFFF00 !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFF00, 0 0 15px #BBBB00;
    }
    .glow-blue {
        color: #00D2FF !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #00D2FF, 0 0 15px #006699;
    }
    .glow-red {
        color: #FF3333 !important;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 10px #FF3333, 0 0 15px #990000;
    }
    
    /* Static Block Styling for Core Diagram Blueprint */
    .one-page-matrix {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .matrix-card {
        background-color: #0D0D0D;
        border: 1px solid #333333;
        border-radius: 6px;
        padding: 15px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- COMPLETE RAW REPOSITORY INGESTION ---
@st.cache_data
def load_complete_unlinked_inventories():
    # Complete Bottom 5-Year Master Data Strategy List
    bottom_5yr_raw = [
        {"ID": "1.1", "Pillar": "Supply Chain Enhancement", "Issue": "የግብዓት አቅርቦትን አስተማማኝ ማድረግ (Reliable Raw Material Supply)"},
        {"ID": "2.1", "Pillar": "Capacity Building", "Issue": "የሰው ሀብት አቅም ማሳደግና ማምረቻ መሳሪያዎች አጠቃቀም (HR Capacity & Plant Utilization)"},
        {"ID": "3.1", "Pillar": "Overall Cost Reduction", "Issue": "የምርት ወጪን በከፍተኛ ሁኔታ መቀነስ (Rigorous Production Cost Reduction)"},
        {"ID": "3.2", "Pillar": "Sales & Marketing", "Issue": "የገበያ ድርሻንና የሽያጭ መረብን ማስፋፋት (Market Share Optimization)"}
    ]
    
    # Complete Left Annual Objective Data List
    left_annual_raw = [
        {"ID": "1.1.1", "Objective": "ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በክምችትና በግዢ ሂደት እንዲኖር ማድረግን ከ27.7% ወደ 95% ማሳደግ"},
        {"ID": "1.1.2", "Objective": "የመለዋወጫ አቅርቦት ጊዜ ከ115 ቀን ወደ 21 ቀናት ዝቅ ማድረግ"},
        {"ID": "1.1.3", "Objective": "ለማሻሻያ ፕሮጀክት የሚሆኑ የማምረቻ መሳሪያዎች 100% በወቅቱ ማቅረብ"},
        {"ID": "1.1.4", "Objective": "ከአምራቾች የሚገዛውን ጥሬ ዕቃ (በአቅራቢዎች ቁጥር) ከ 63% ወደ 80% ማሳደግ"},
        {"ID": "1.1.5", "Objective": "የፈርነስ ዘይት አቅርቦት 100% እንዲሆን ማድረግ"},
        {"ID": "2.1.1", "Objective": "የሠራተኛውን አፈጻጸም ከ82 በመቶ ወደ 95 በመቶ ማሳደግ"},
        {"ID": "2.1.2", "Objective": "የሠራተኛው ዕርካታ (employee satisfaction) ከ75% ወደ 95% ማሳደግ"},
        {"ID": "2.1.3", "Objective": "የሠራተኛው የሥራ ተነሳሽነትና የባለቤትነት ስሜት (employee engagement) ከ60% ወደ 85% ማሳደግ"},
        {"ID": "3.1.7", "Objective": "የፈርነስ ፍጆታን (ቶን/ቶን) ከ 0.56 ወደ 0.25 መቀነስ"},
        {"ID": "3.1.8", "Objective": "ኤሌክትሪክ ፍጆታን በ (KWH/ton) ከ 1529 ወደ 1200 መቀነስ"},
        {"ID": "3.2.2", "Objective": "የክሌም ወጪን ከ 0.006% ወደ 0.003% መቀነስ"}
    ]
    
    # Complete Right Live KPI Data List Registry
    right_kpis_raw = [
        {"KPI_ID": "1.1.1", "Pillar": "Supply Chain Enhancement", "Title": "Raw Material Stock Inventory Pipeline Coverage", "Target": 0.95, "Direction": "Up", "Dept": "Purchase"},
        {"KPI_ID": "1.1.2", "Pillar": "Supply Chain Enhancement", "Title": "Spare Parts Inbound Lead Time Index", "Target": 21.0, "Direction": "Down", "Dept": "Plant Engineering"},
        {"KPI_ID": "2.1.1", "Pillar": "Capacity Building", "Title": "Workforce Operational Performance Efficiency", "Target": 0.95, "Direction": "Up", "Dept": "HR"},
        {"KPI_ID": "3.1.7", "Pillar": "Overall Cost Reduction", "Title": "Furnace Fuel Consumption Ratio (Tons/Ton)", "Target": 0.25, "Direction": "Down", "Dept": "Production"},
        {"KPI_ID": "3.1.8", "Pillar": "Overall Cost Reduction", "Title": "Electrical Energy Utility Index (KWH/Ton)", "Target": 1200.0, "Direction": "Down", "Dept": "Plant Engineering"},
        {"KPI_ID": "3.2.2", "Pillar": "Sales & Marketing", "Title": "Commercial Product Warranty Claim Defect Cost Ratio", "Target": 0.003, "Direction": "Down", "Dept": "PIQA"}
    ]
    
    # Complete Top Priorities Deployment Data List
    top_priorities_raw = [
        {"Dept": "Purchase & PIQA", "Priority": "አምራች አቅራቢዎችን ለይቶ ማወቅ፣ የተሻሉትን መምረጥና በአካል ሄዶ ማነጋገር"},
        {"Dept": "Top Mgt & Finance", "Priority": "ከፍተኛ ክትትል በማድረግና አዋጭነትን በማመዛዘን የውጭ ምንዛሪ ግኝትን ማመቻቸት"},
        {"Dept": "Plant Engineering", "Priority": "ለማምረቻ መሣሪዎች፣ መገልገያዎችና መለዋወጫዎች ትክለኛውን ስፔሲፊኬሽን በወቅቱ ማቅረብ"},
        {"Dept": "Production", "Priority": "የሃይል አጠቃቀምን በየዕለቱ መከታተልና አላስፈላጊ ብክነትን ሙሉ በሙሉ ማስወገድ"},
        {"Dept": "Commercial Operations", "Priority": "የገበያ ስለላ (market intelligence) ስራን ማጠናከርና የሽያጭ ኔትወርክን ማስፋፋት"}
    ]
    
    return pd.DataFrame(bottom_5yr_raw), pd.DataFrame(left_annual_raw), pd.DataFrame(right_kpis_raw), pd.DataFrame(top_priorities_raw)

df_5yr, df_annual, df_kpis, df_priorities = load_complete_unlinked_inventories()

# --- INITIALIZE MULTI-MONTH PERSISTENT MEMORY ARRAYS ---
if "monthly_feed" not in st.session_state:
    st.session_state.monthly_feed = {
        "1.1.1": 0.55, "1.1.2": 72.0, "2.1.1": 0.84, "3.1.7": 0.42, "3.1.8": 1410.0, "3.2.2": 0.005
    }

# =========================================================
#   APPLICATION INTERFACE HEADS
# =========================================================
st.markdown("<h1 style='text-align:center;'>🎯 HORIZON ADDIS TYRE MASTER HOSHIN REPOSITORY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666666;'>Corporate Strategic Alignment System & Dynamic Activity Ledger</p>", unsafe_allow_html=True)
st.markdown("---")

# --- 1. OVERARCHING VISUAL REPRESENTATION (ALL-IN-ONE VISUAL MATRIX) ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #00FF66; padding-left:10px;'>📊 GLOBAL CORPORATE HOSHIN PROFILE DIAGRAM</h3>", unsafe_allow_html=True)

st.markdown('<div class="one-page-matrix">', unsafe_allow_html=True)
st.markdown("""
    <div class="matrix-card" style="border-top: 3px solid #FFFFFF;"><div class="glow-white">SUPPLY CHAIN</div><p style='color:#666; font-size:12px; margin-top:5px;'>Pillar Master Ledger</p></div>
    <div class="matrix-card" style="border-top: 3px solid #FFFF00;"><div class="glow-yellow">CAPACITY BUILDING</div><p style='color:#666; font-size:12px; margin-top:5px;'>Operational Master Ledger</p></div>
    <div class="matrix-card" style="border-top: 3px solid #00D2FF;"><div class="glow-blue">COST REDUCTION</div><p style='color:#666; font-size:12px; margin-top:5px;'>Financial Master Ledger</p></div>
    <div class="matrix-card" style="border-top: 3px solid #FF3333;"><div class="glow-red">SALES & MARKETING</div><p style='color:#666; font-size:12px; margin-top:5px;'>Commercial Master Ledger</p></div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 2. ISOLATED DROP-DOWN MASTER LISTS REGISTER ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #FFFFFF; padding-left:10px;'>📁 STRATEGIC MASTER MATRIX DROPDOWNS</h3>", unsafe_allow_html=True)

# Dropdown A: Bottom 5-Year Plan
with st.expander("⬇️ [BOTTOM PANEL DROPDOWN] — 5 YEAR STRATEGIC LAUNCH LIST"):
    st.table(df_5yr)

# Dropdown B: Left Annual Objectives
with st.expander("⬅️ [LEFT PANEL DROPDOWN] — ANNUAL STRATEGIC OBJECTIVE CATALOG"):
    for idx, row in df_annual.iterrows():
        st.markdown(f"**Item ID {row['ID']}**: {row['Objective']}")

# Dropdown C: Right KPI Parameters
with st.expander("➡️ [RIGHT PANEL DROPDOWN] — MASTER KEY PERFORMANCE INDICATORS):"):
    st.dataframe(df_kpis, use_container_width=True, hide_index=True)

# Dropdown D: Top Priority Items
with st.expander("⬆️ [TOP PANEL DROPDOWN] — DEPLOYED ACTIONABLE PRIORITIES"):
    for idx, row in df_priorities.iterrows():
        st.markdown(f"⚡ **{row['Dept']} Focus Group**: {row['Priority']}")

st.markdown("---")

# --- 3. SEPARATE MONTHLY KPI ACTUAL FEEDING GATE & VISUAL DIAGRAM ---
st.markdown("<h3 style='color:#FFFFFF; border-left: 4px solid #FFFF00; padding-left:10px;'>📆 MONTHLY PERFORMANCE DISPATCH & GRAPH DATA FEEDING</h3>", unsafe_allow_html=True)

f_col1, f_col2 = st.columns([1, 2])

with f_col1:
    selected_month = st.selectbox("Select Target Operations Month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    st.markdown("<p style='color:#888888; font-size:13px;'>Modify values below to update month-by-month results:</p>", unsafe_allow_html=True)
    
    current_inputs = {}
    for idx, row in df_kpis.iterrows():
        kid = row["KPI_ID"]
        saved_val = st.session_state.monthly_feed[kid]
        if row["Target"] < 1.0:
            val = st.number_input(f"KPI {kid} ({row['Dept']})", value=float(saved_val), format="%.4f", step=0.001)
        else:
            val = st.number_input(f"KPI {kid} ({row['Dept']})", value=float(saved_val), step=1.0)
        current_inputs[kid] = val
        
    # Commit variables back to cache tracking system
    st.session_state.monthly_feed = current_inputs

# Core evaluation calculations block
def compute_isolated_kpi_progress(row):
    actual_val = st.session_state.monthly_feed[row["KPI_ID"]]
    target_val = row["Target"]
    if row["Direction"] == "Up":
        return min(max((actual_val / target_val) * 100, 0.0), 120.0) if target_val != 0 else 0
    else:
        return min(max((target_val / actual_val) * 100, 0.0), 120.0) if actual_val != 0 else 0

df_kpis["Month_Actual"] = df_kpis["KPI_ID"].map(st.session_state.monthly_feed)
df_kpis["Performance Achievement %"] = df_kpis.apply(compute_isolated_kpi_progress, axis=1)

with f_col2:
    st.markdown(f"<p style='color:#00FF66; font-weight:bold;'>Performance Graph: {selected_month.upper()} Target Status</p>", unsafe_allow_html=True)
    
    # Render progress indicators dynamically per structural KPI entry point
    for idx, row in df_kpis.iterrows():
        pct = row["Performance Achievement %"]
        st.markdown(f"**[{row['KPI_ID']}]** {row['Title']} — Status: `Actual: {row['Month_Actual']}` vs `Target: {row['Target']}`")
        st.progress(pct / 120.0)
        st.caption(f"Calculated Performance Achievement Rate: **{pct:.1f}%**")
        st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)
