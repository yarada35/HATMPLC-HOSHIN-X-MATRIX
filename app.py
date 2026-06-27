import streamlit as st
import pandas as pd
import io

# --- INITIAL APP ENVIRONMENT SETUP ---
st.set_page_config(
    page_title="Horizon Addis Tyre - Complete Hoshin Matrix Suite",
    page_icon="🎯",
    layout="wide"
)

# --- MATTE BLACK APP SKIN AND HIGH-READABILITY EMISSIVE HIGHLIGHT GLOWS ---
st.markdown("""
    <style>
    /* Global App Canvas & Core Elements */
    .stApp, [data-testid="stHeader"], header {
        background-color: #000000 !important;
    }
    
    /* Global Text Visibility & Font Scaling Enforcements */
    p, span, label, th, td, .stMarkdown, li {
        color: #FFFFFF !important;
        font-size: 16px !important; /* Increased base body font size */
    }
    
    /* Standardized Streamlit DataFrame Interactive Readability Override */
    div[data-testid="stDataFrame"] td, div[data-testid="stDataFrame"] th {
        font-size: 15px !important;
    }

    /* Interactive Dropdown Expander Readability Wrapper */
    .stAccordion {
        background-color: #0B0B0B !important;
        border: 2px solid #222222 !important;
        margin-bottom: 12px !important;
    }
    .stAccordion button p {
        font-size: 19px !important; /* Larger text headers on dropdown registers */
        font-weight: bold !important;
    }
    
    /* Corporate Core Pillar Matrix Highlights & Color Scheming */
    .glow-yellow {
        color: #FFFF00 !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 24px !important;
        font-weight: 900;
        text-shadow: 0 0 10px #FFFF00, 0 0 15px #BBBB00;
    }
    .glow-red {
        color: #FF3333 !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 24px !important;
        font-weight: 900;
        text-shadow: 0 0 10px #FF3333, 0 0 15px #990000;
    }
    .glow-blue {
        color: #00D2FF !important;
        font-family: 'Arial Black', sans-serif;
        font-size: 24px !important;
        font-weight: 900;
        text-shadow: 0 0 10px #00D2FF, 0 0 15px #006699;
    }
    /* Readable High-Contrast Warm Gold Brown Tone */
    .glow-brown {
        color: #E6A15C !important; 
        font-family: 'Arial Black', sans-serif;
        font-size: 24px !important;
        font-weight: 900;
        text-shadow: 0 0 10px #E6A15C, 0 0 15px #A66F33;
    }
    
    /* Section Custom Identity Labeling Class Callouts */
    .section-title-yellow { color: #FFFF00 !important; font-size: 22px !important; font-weight: bold !important; }
    .section-title-red    { color: #FF3333 !important; font-size: 22px !important; font-weight: bold !important; }
    .section-title-blue   { color: #00D2FF !important; font-size: 22px !important; font-weight: bold !important; }
    .section-title-brown  { color: #E6A15C !important; font-size: 22px !important; font-weight: bold !important; }
    
    /* Layout Organization Grid Components */
    .one-page-matrix {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .matrix-card {
        background-color: #0D0D0D;
        border: 2px solid #333333;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- COMPLETE UNABRIDGED ARRAYS LOADING ENGINE ---
@st.cache_data
def load_all_four_panels_completely():
    # File 1: Bottom Panel - Complete 5 Year Strategy List
    csv_5yr = """ID,Pillar,Strategic Issue / Objective
1.1,Supply Chain Enhancement,የግብዓት አቅርቦትን አስተማማኝ ማድረግ (Reliable Raw Material Supply Pipeline)
1.1.1,Supply Chain Enhancement,ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በክምችትና ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በግዢ ሂደት እንዲኖር ማድረግን ከ27.7% ወደ 95% ማሳደግ
1.1.2,Supply Chain Enhancement,የመለዋወጫ አቅርቦት ጊዜ ከ115 ቀን ወደ 21 ቀናት ዝቅ ማድረግ
1.1.3,Supply Chain Enhancement,ለማሻሻያ ፕሮጀክት የሚሆኑ የማምረቻ መሳሪያዎች 100% በወቅቱ ማቅረብ
1.1.4,Supply Chain Enhancement,ከአምራቾች የሚገዛውን ጥሬ ዕቃ (በአቅራቢዎች ቁጥር) ከ 63% ወደ 80% ማሳደግ
1.1.5,Supply Chain Enhancement,የፈርነስ ዘይት አቅርቦት 100% እንዲሆን ማድረግ
2.1,Capacity Building,የሰው ሀብት አቅም ማሳደግ (Human Resource Capacity & Plant Equipment Utilization)
2.1.1,Capacity Building,የሠራተኛውን አፈጻጸም ከ82 በመቶ ወደ 95 በመቶ ማሳደግ
2.1.2,Capacity Building,የሠራተኛው ዕርካታ (employee sateisfaction) ከ75% ወደ 95% ማሳደግ
2.1.3,Capacity Building,የሠራተኛው የሥራ ተነሳሽነትና የባለቤትነት ስሜት (employee engagement) ከ60% ወደ 85% ማሳደግ
2.1.4,Capacity Building,የሠራተኛ ፍልሰትን ከ7.6% ወደ 3.5% ዝቅ ማድረግ
3.1,Overall Cost Reduction,የምርት ወጪን በከፍተኛ ሁኔታ መቀነስ (Rigorous Production Cost Reduction Framework)
3.1.1,Overall Cost Reduction,የማምረቻ ማሽኖች ብቃት (OEE) ከ74% ወደ 85% ማሳደግ
3.1.2,Overall Cost Reduction,የምርት ብክነትን ከ5.8% ወደ 3.5% መቀነስ
3.1.3,Overall Cost Reduction,የማሽን ብልሽት ጊዜን (Downtime) በ40% መቀነስ
3.1.4,Overall Cost Reduction,የእቅድ አፈፃፀም (Plan Compliance) ከ88% ወደ 96% ማሳደግ
3.1.5,Overall Cost Reduction,የቀጥታ ሰራተኞች ምርታማነትን በ15% ማሳደግ
3.1.6,Overall Cost Reduction,የማምረቻ መሳሪያዎች ጥገና ወጪን በ10% መቀነስ
3.1.7,Overall Cost Reduction,የፈርነስ ፍጆታን (ቶን/ቶን) ከ 0.56 ወደ 0.25 መቀነስ
3.1.8,Overall Cost Reduction,ኤሌክትሪክ ፍጆታን በ (KWH/ton) ከ 1529 ወደ 1200 መቀነስ
3.1.9,Overall Cost Reduction,የዋና ዋና ጥሬ ዕቃ አቅራቢዎችን ቁጥር ከ1.33 ወደ 3 ከፍ ማድረግ
3.1.10,Overall Cost Reduction,በውጪ ህክምና ተቋማት የሚሰጠውን የህመም ፈቃድ ቀናት ከ 2329 የሰው ቀናት ወደ 1164 የሰው ቀናት መቀነስ
3.1.11,Overall Cost Reduction,የግባት ወጪን እስከ 5% መቀነስ
3.1.12,Overall Cost Reduction,የሽያጭ ኮሚሽን ከጠቅላላ ሽያጭ ከ 7% ወደ 5% መቀነስ
3.2.1,Overall Cost Reduction,የአዳዲስ ምረተ የጥራት ወጪን ከ 6 ዙር ወደ 4 ዙር መቀነስ
3.2.2,Overall Cost Reduction,የክሌም ወጪን ከ 0.006% ወደ 0.003% መቀነስ
3.2.4,Overall Cost Reduction,የጥሬ ዕቃ ማሸጊያ እና ጥራትን ከ 95% ወደ 100% ማሳደግ
3.3.1,Overall Cost Reduction,የባንከ ወለድ ወጢን ከ 5% እንዳይበልጥ ማድረግ
4.1.1,Sales & Market Enhancement,የሀገር ውስጥ የገበያ ድርሻን ከ 45% ወደ 60% ማሳደግ
4.1.2,Sales & Market Enhancement,የውጭ ሀገር ወጪ ንግድ (Export Sales) በ 25% ማሳደግ
4.1.3,Sales & Market Enhancement,አዳዲስ ስትራቴጂካዊ የሽያጭ መረቦችንና የጎማ ማከፋፈያ መንገዶችን በየክልሉ መዘርጋት
4.1.4,Sales & Market Enhancement,የብራንድ ተወዳዳሪነትንና የማስተዋወቅ ስራዎችን በሚዲያ ማሳደግ"""

    # File 2: Left Panel - Complete Annual Objectives List
    csv_annual = """ID,Objective,Weight
1.1.1,ለሶስት ወር ምርት የሚበቃ ጥሬ ዕቃ በክምችትና በግዢ ሂደት እንዲኖር ማድረግን ከ27.7% ወደ 95% ማሳደግ,4
1.1.2,የመለዋወጫ አቅርቦት ጊዜ ከ115 ቀን ወደ 21 ቀናት ዝቅ ማድረግ,2
1.1.3,ለማሻሻያ ፕሮጀክት የሚሆኑ የማምረቻ መሳሪያዎች 100% በወቅቱ ማቅረብ,6
1.1.4,ከአምራቾች የሚገዛውን ጥሬ ዕቃ (በአቅራቢዎች ቁጥር) ከ 63% ወደ 80% ማሳደግ,6
1.1.5,የፈርነስ ዘይት አቅርቦት 100% እንዲሆን ማድረግ,2
2.1.1,የሠራተኛውን አፈጻጸም ከ82 በመቶ ወደ 95 በመቶ ማሳደግ,4
2.1.2,የሠራተኛው ዕርካታ (employee sateisfaction) ከ75% ወደ 95% ማሳደግ,4
2.1.3,የሠራተኛው የሥራ ተነሳሽነትና የባለቤትነት ስሜት (employee engagement) ከ60% ወደ 85% ማሳደግ,3
2.1.4,የሠራተኛ ፍልሰትን ከ7.6% ወደ 3.5% ዝቅ ማድረግ,2
3.1.1,የማምረቻ ማሽኖች ብቃት (OEE) ከ74% ወደ 85% ማሳደግ,5
3.1.2,የምርት ብክነትን ከ5.8% ወደ 3.5% መቀነስ,5
3.1.3,የማሽን ብልሽት ጊዜን (Downtime) በ40% መቀነስ,4
3.1.4,የእቅድ አፈፃፀም (Plan Compliance) ከ88% ወደ 96% ማሳደግ,3
3.1.5,የቀጥታ ሰራተኞች ምርታማነትን በ15% ማሳደግ,2
3.1.6,የጥገና ወጪ ላይ የመለዋወጫ ወጪን በ8 በመቶ መቀነስ,3
3.1.7,የፈርነስ ፍጆታን (ቶን/ቶን) ከ 0.56 ወደ .25 መቀነስ,4
3.1.8,ኤሌክትሪክ ፍጆታን በ (KWH/ton) ከ 1529 ወደ 1200 መቀነስ,2
3.1.9,የዋና ዋና ጥሬ ዕቃ አቅራቢዎችን ቁጥር ከ1.33 ወደ 3 ከፍ ማድረግ,2
3.1.10,በውጪ ህክምና ተቋማት የሚሰጠውን የህመም ፈቃድ ቀናት ከ 2329 የሰው ቀናት ወደ 1164 የሰው ቀናት መቀነስ,2
3.1.11,የግባት ወጪን እስከ 5% መቀነስ,2
3.1.12,የሽያጭ ኮሚሽን ከጠቅላላ ሽያጭ ከ 7% ወደ 5% መቀነስ,2
3.2.1,የአዳዲስ ምረተ የጥራት ወጪን ከ 6 ዙር ወደ 4 ዙር መቀነስ,1
3.2.2,የክሌም ወጪን ከ 0.006% ወደ 0.003% መቀነስ,1
3.2.4,የጥሬ ዕቃ ማሸጊያ እና ጥራትን ከ 95% ወደ 100% ማሳደግ,1
4.1.1,የሀገር ውስጥ የገበያ ድርሻን ከ 45% ወደ 60% ማሳደግ,5
4.1.2,የውጭ ሀገር ወጪ ንግድ (Export Sales) በ 25% ማሳደግ,4
4.1.3,የደንበኞችን እርካታ ማሳደግና ወቅታዊ የገበያ ጥናቶችን ማጠናከር,3"""

    # File 3: Right Panel - Complete Annual KPI List with Target & Department Responsibilities
    csv_kpis = """KPI_ID,Title,Target,Direction,Dept
1.1.1,Raw Material Stock Inventory Pipeline Coverage,0.95,Up,Purchase
1.1.2,Spare Parts Inbound Lead Time Index (Days),21.0,Down,PE
1.1.3,Project Modification Equipment Delivery Completeness Rate,1.0,Up,PE
1.1.4,Direct Manufacturer Sourcing Supplier Ratio,0.8,Up,PURCHASE
1.1.5,Furnace Oil Continuous Supply Availability Rate,1.0,Up,PE
2.1.1,Workforce Operational Performance Efficiency,0.95,Up,HR
2.1.2,Employee Overall Factory Satisfaction Survey Score,0.95,Up,HR
2.1.3,Employee Workplace Engagement Index Rating,0.85,Up,HR
2.1.4,Workforce Turnover and Attrition Rate Control,0.035,Down,HR
3.1.1,Overall Equipment Effectiveness (OEE) Master Target,0.85,Up,PRODUCTION
3.1.2,Production Material Scrap Rate Waste Reduction,0.035,Down,PRODUCTION
3.1.3,Unscheduled Machine Breakdown Downtime Index,0.40,Down,PE
3.1.4,Manufacturing Plan Compliance Achievement Index,0.96,Up,PRODUCTION
3.1.5,Direct Labour Operational Productivity Coefficient,0.15,Up,PRODUCTION
3.1.6,Plant Maintenance Spare Parts Budget Optimization,0.08,Down,PE
3.1.7,Furnace Fuel Consumption Ratio (Tons/Ton),0.25,Down,PRODUCTION
3.1.8,Electrical Energy Utility Index (KWH/Ton),1200.0,Down,PE
3.1.9,Primary Raw Material Strategic Sourcing Options,3.0,Up,PURCHASE
3.1.10,External Sickness Absenteeism Human-Days Mitigation,1164.0,Down,HR
3.1.11,Inbound Material Supply Cost Mitigation Index,0.05,Down,ALL Departments
3.1.12,Commercial Sales Commission Outlay Efficiency Ratio,0.05,Down,SALES AND MARKETING
3.2.1,New Product Iteration Defect Quality Loop Cycles,4.0,Down,SALES AND MARKETING
3.2.2,Commercial Product Warranty Claim Defect Cost Ratio,0.003,Down,PIQA
3.2.4,Raw Material Packaging Integrity & Quality Acceptability,1.0,Up,PURCHASE
3.3.1,Bank Interest Outlay Financial Threshold Ceiling,0.05,Down,FINANCE
3.3.2,Customs Storage and Demurrage Operational Waste Outlay,0.0,Down,PURCHASE
3.3.3,Obsolete Spare Parts Dead Stock Liquidation Index,0.20,Down,SALES AND MARKETING
3.3.4,First-In First-Out (FIFO) Inventory Control Implementation,1.0,Up,PMITS
3.3.5,Tire Rotation and Inventory Lifespan Optimization Index,1.0,Up,PRODUCTION
4.1.1,Domestic Market Share Penetration Index,0.60,Up,SALES AND MARKETING
4.1.2,Export Sales Volume Expansion Rate,0.25,Up,SALES AND MARKETING
4.1.3,Strategic Customer Survey Satisfaction Rating Index,0.95,Up,SALES AND MARKETING
4.1.4,Brand Awareness Promotion Campaign Reach Matrix,1.0,Up,SALES AND MARKETING"""

    # File 4: Top Panel - Complete Prioritized Activities List
    csv_priorities = """ID,Priority,Dept
1.1.3,"• ከፍተኛ ክትትል በማድረግና አዋጭነትን በማመዛዘን የውጭ ምንዛሪ ግኝትን ማመቻቸት\n• ለማምረቻ መሣሪዎች ትክለኛውን ስፔሲፊኬሽን በወቅቱ ማቅረብ",Top Mgt & Finance
1.1.4,"• አምራች አቅራቢዎችን ለይቶ ማወቅ፣ የተሻሉትን መምረጥና በአካል ሄዶ ማነጋገር\n• ጥሬ ዕቃዎች ሲመጡ ፍተሻ በማድረግ ጥራታቸውን ማረጋገጥ",Purchase & PIQA
1.1.1,"• የምርት ዕቅድ፣ የክምችት መጠንና የዕለት ተዕለት የጥሬ ዕቃ ሁኔታን በቅርብ መከታተል",Purchase
2.1.1,"• የሠራተኛውን አቅም ለመገንባት የሚያስችሉ ስልጠናዎችን በጥናት ላይ ተመስርቶ ማዘጋጀትና መስጠት",HR
3.1.1,"• የማሽነሪዎችን ዕለታዊና ሳምንታዊ የመከላከያ ጥገና (Preventive Maintenance) ማረጋገጥ",PRODUCTION
3.1.7,"• የኃይል አጠቃቀምንና ፍጆታን በየዕለቱ በጥብቅ መከታተልና አላስፈላጊ የሃይል ብክነቶችን ሙሉ በሙሉ ማስወገድ",PRODUCTION
4.1.1,"• ወቅታዊ የገበያ ጥናት በማካሄድ ማከፋፈያ መንገዶችን በየክልሉ መዘርጋትና ዘላቂ ግንኙነት መፍጠር\n• ተገቢውን ሚዲያ በመጠቀም ምርት እና አገልግሎቶችን በአግባቡ ማስተዋወቅ\n• የገበያ ስለላ (market intelligence) ስራን ማጠናከር",SALES AND MARKETING"""

    df_5yr = pd.read_csv(io.StringIO(csv_5yr))
    df_annual = pd.read_csv(io.StringIO(csv_annual))
    df_kpis = pd.read_csv(io.StringIO(csv_kpis))
    df_priorities = pd.read_csv(io.StringIO(csv_priorities))
    
    return df_5yr, df_annual, df_kpis, df_priorities

df_5yr, df_annual, df_kpis, df_priorities = load_all_four_panels_completely()

# --- INSTANTIATE PERSISTENT TRACKING MEMORY FOR EVERY LOADED METRIC ---
if "monthly_feed" not in st.session_state:
    st.session_state.monthly_feed = {row["KPI_ID"]: float(row["Target"]) for idx, row in df_kpis.iterrows()}

# =========================================================
#   APPLICATION INTERFACE HEADS
# =========================================================
st.markdown("<h1 style='text-align:center; font-size:36px; color:#FFFF00;'>🎯 HORIZON ADDIS TYRE MASTER HOSHIN MANAGEMENT SUITE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#E6A15C; font-size:18px;'>Corporate Strategic Alignment System — Unabridged Executive Blueprint View</p>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #333;'>", unsafe_allow_html=True)

# --- 1. OVERARCHING VISUAL REPRESENTATION PANEL ---
st.markdown("<h3 class='section-title-yellow'>📊 GLOBAL CORPORATE HOSHIN PROFILE DIAGRAM</h3>", unsafe_allow_html=True)
st.markdown('<div class="one-page-matrix">', unsafe_allow_html=True)
st.markdown("""
    <div class="matrix-card" style="border-top: 4px solid #FFFF00;"><div class="glow-yellow">SUPPLY CHAIN</div><p style='color:#AAAAAA; font-size:14px !important; margin-top:5px;'>Pillar Master Ledger</p></div>
    <div class="matrix-card" style="border-top: 4px solid #FF3333;"><div class="glow-red">CAPACITY BUILDING</div><p style='color:#AAAAAA; font-size:14px !important; margin-top:5px;'>Operational Master Ledger</p></div>
    <div class="matrix-card" style="border-top: 4px solid #00D2FF;"><div class="glow-blue">COST REDUCTION</div><p style='color:#AAAAAA; font-size:14px !important; margin-top:5px;'>Financial Master Ledger</p></div>
    <div class="matrix-card" style="border-top: 4px solid #E6A15C;"><div class="glow-brown">SALES & MARKETING</div><p style='color:#AAAAAA; font-size:14px !important; margin-top:5px;'>Commercial Master Ledger</p></div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 2. THE FOUR SEPARATED STRATEGIC DROPDOWN REGISTER EXPANDERS ---
st.markdown("<h3 class='section-title-blue'>📁 COMPLETE STRATEGIC MASTER MATRIX DROPDOWNS</h3>", unsafe_allow_html=True)

with st.expander("⬇️ [BOTTOM PANEL DROPDOWN] — 5 YEAR STRATEGIC LAUNCH LIST (COMPLETE - ALL ROWS)"):
    st.dataframe(df_5yr, use_container_width=True, hide_index=True)

with st.expander("⬅️ [LEFT PANEL DROPDOWN] — ANNUAL STRATEGIC OBJECTIVE CATALOG (COMPLETE - ALL ROWS)"):
    st.dataframe(df_annual, use_container_width=True, hide_index=True)

with st.expander("➡️ [RIGHT PANEL DROPDOWN] — MASTER KEY PERFORMANCE INDICATORS & RESPONSIBILITIES (COMPLETE - ALL ROWS)"):
    st.dataframe(df_kpis, use_container_width=True, hide_index=True)

with st.expander("⬆️ [TOP PANEL DROPDOWN] — DEPLOYED ACTIONABLE PRIORITIES (COMPLETE - ALL ROWS)"):
    st.dataframe(df_priorities, use_container_width=True, hide_index=True)

st.markdown("<hr style='border:1px solid #333;'>", unsafe_allow_html=True)

# --- 3. DYNAMIC DATA INPUT FEED & ENGINE TARGET STATUS PERFORMANCE GRAPH ---
st.markdown("<h3 class='section-title-brown'>📆 MONTHLY PERFORMANCE DISPATCH & GRAPH DATA FEEDING</h3>", unsafe_allow_html=True)

f_col1, f_col2 = st.columns([1, 2])

with f_col1:
    selected_month = st.selectbox("Select Target Operations Month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    st.markdown("<p style='color:#E6A15C; font-size:15px; font-weight:bold;'>Input current operational metrics directly below:</p>", unsafe_allow_html=True)
    
    current_inputs = {}
    for idx, row in df_kpis.iterrows():
        kid = row["KPI_ID"]
        saved_val = st.session_state.monthly_feed.get(kid, float(row["Target"]))
        if row["Target"] <= 1.0:
            val = st.number_input(f"KPI {kid} ({row['Dept']})", value=float(saved_val), format="%.4f", step=0.001, key=f"feed_{kid}")
        else:
            val = st.number_input(f"KPI {kid} ({row['Dept']})", value=float(saved_val), step=1.0, key=f"feed_{kid}")
        current_inputs[kid] = val
        
    st.session_state.monthly_feed = current_inputs

# Execution progress calculation block
def compute_isolated_kpi_progress(row):
    actual_val = st.session_state.monthly_feed.get(row["KPI_ID"], float(row["Target"]))
    target_val = float(row["Target"])
    if row["Direction"] == "Up":
        return min(max((actual_val / target_val) * 100, 0.0), 120.0) if target_val != 0 else 0
    else:
        return min(max((target_val / actual_val) * 100, 0.0), 120.0) if actual_val != 0 else 0

df_kpis["Month_Actual"] = df_kpis["KPI_ID"].map(st.session_state.monthly_feed)
df_kpis["Performance Achievement %"] = df_kpis.apply(compute_isolated_kpi_progress, axis=1)

with f_col2:
    st.markdown(f"<p style='color:#00FF66; font-weight:bold; font-size:20px;'>Performance Graphs for {selected_month.upper()}</p>", unsafe_allow_html=True)
    
    for idx, row in df_kpis.iterrows():
        pct = row["Performance Achievement %"]
        st.markdown(f"<span style='font-size:18px !important; font-weight:bold; color:#FFFF00;'>[{row['KPI_ID']}] {row['Title']}</span><br><span style='color:#00D2FF; font-size:14px !important;'>Owner Accountability: <b>{row['Dept']} Department</b></span>", unsafe_allow_html=True)
        st.markdown(f"Status: `Actual: {row['Month_Actual']}` vs `Target: {row['Target']}`")
        st.progress(pct / 120.0)
        st.markdown(f"<span style='font-size:14px !important; color:#E6A15C;'>Calculated Performance Achievement Rate: <b>{pct:.1f}%</b></span>", unsafe_allow_html=True)
        st.markdown("<div style='border-bottom: 1px dashed #333; margin-bottom:14px;'></div>", unsafe_allow_html=True)

# --- 4. OVERALL COMPANY ACHIEVEMENT PRESENTATION HUB ---
st.markdown("<hr style='border:1px solid #333;'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:#FFFF00; border-bottom: 2px solid #222; padding-bottom:10px; font-size:28px;'>🏆 GLOBAL COMPANY PERFORMANCE REALIZATION</h2>", unsafe_allow_html=True)

total_kpis = len(df_kpis)
average_achievement = df_kpis["Performance Achievement %"].mean() if total_kpis > 0 else 0.0
targets_achieved = len(df_kpis[df_kpis["Performance Achievement %"] >= 100.0])

col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    st.markdown("""
        <div style='background-color:#0A0A0A; border:2px solid #FF3333; padding:20px; border-radius:8px; text-align:center;'>
            <h4 style='color:#FF3333; margin:0; font-size:18px !important; font-weight:bold;'>STRATEGIC BOUNDARY TARGET</h4>
            <h1 style='font-size:52px !important; color:#FFFFFF; margin:10px 0; font-weight:bold;'>100.0%</h1>
            <p style='color:#AAAAAA; font-size:14px !important; margin:0;'>Horizon Addis Milestone Base</p>
        </div>
    """, unsafe_allow_html=True)

with col_m2:
    glow_color = "#00FF66" if average_achievement >= 90.0 else "#FFFF00"
    st.markdown(f"""
        <div style='background-color:#0A0A0A; border:2px solid {glow_color}; padding:20px; border-radius:8px; text-align:center;'>
            <h4 style='color:{glow_color}; margin:0; font-size:18px !important; font-weight:bold;'>COMPANY ACTUAL REALIZATION</h4>
            <h1 style='font-size:52px !important; color:{glow_color}; margin:10px 0; font-weight:bold;'>{average_achievement:.2f}%</h1>
            <p style='color:#AAAAAA; font-size:14px !important; margin:0;'>Combined Operational Velocity</p>
        </div>
    """, unsafe_allow_html=True)

with col_m3:
    st.markdown(f"""
        <div style='background-color:#0A0A0A; border:2px solid #00D2FF; padding:20px; border-radius:8px; text-align:center;'>
            <h4 style='color:#00D2FF; margin:0; font-size:18px !important; font-weight:bold;'>KPI TARGET CLOSURE RATE</h4>
            <h1 style='font-size:52px !important; color:#FFFFFF; margin:10px 0; font-weight:bold;'>{targets_achieved} / {total_kpis}</h1>
            <p style='color:#AAAAAA; font-size:14px !important; margin:0;'>Uncompromised Complete Line Items</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px !important; font-weight:bold; color:#E6A15C;'>Visual Representation: Actual Realization Overlapping Corporate Target Boundary</p>", unsafe_allow_html=True)

st.progress(min(average_achievement / 120.0, 1.0))
st.markdown("<p style='text-align:right; color:#AAAAAA; font-size:13px !important; margin-top:2px;'>Realization Matrix Level Cap: 120% Variance Window</p>", unsafe_allow_html=True)
