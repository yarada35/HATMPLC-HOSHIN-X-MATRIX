import streamlit as st
import pandas as pd

st.set_page_config(page_title="HATMPLC Live X-Matrix Dashboard", layout="wide")

# --- CUSTOM CSS FOR THE TRIANGULAR / CROSS DIAMOND X-MATRIX LAYOUT ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Ethiopic', sans-serif;
        background-color: #f1f5f9;
    }
    .matrix-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e293b;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Grid container for the X-Matrix Layout matching the image structure */
    .x-matrix-container {
        display: grid;
        grid-template-columns: 1fr 1.2fr 1fr;
        grid-template-rows: auto auto auto;
        gap: 15px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .matrix-box {
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        color: white;
        min-height: 200px;
    }
    
    /* Individual quadrant styling matching the attached image colors */
    .top-box {
        grid-column: 2;
        grid-row: 1;
        background: linear-gradient(135deg, #f87171, #ef4444);
        border: 3px solid #dc2626;
        text-align: center;
    }
    .left-box {
        grid-column: 1;
        grid-row: 2;
        background: linear-gradient(135deg, #4ade80, #22c55e);
        border: 3px solid #16a34a;
    }
    .right-box {
        grid-column: 3;
        grid-row: 2;
        background: linear-gradient(135deg, #60a5fa, #3b82f6);
        border: 3px solid #2563eb;
    }
    .bottom-box {
        grid-column: 2;
        grid-row: 3;
        background: linear-gradient(135deg, #fb923c, #f97316);
        border: 3px solid #ea580c;
        text-align: center;
    }
    
    .box-header {
        font-size: 1.6rem;
        font-weight: bold;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .box-subheader {
        font-size: 1rem;
        font-style: italic;
        margin-bottom: 12px;
        opacity: 0.9;
    }
    .item-text {
        font-size: 0.9rem;
        text-align: left;
        background: rgba(25px, 25px, 25px, 0.15);
        padding: 8px;
        margin-bottom: 6px;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='matrix-title'>❌ Hoshin Kanri X-Matrix Visualizer</div>", unsafe_allow_html=True)

# --- LIVE DATA EXTRACTION ---
@st.cache_data
def get_verified_data():
    b_df = pd.read_excel("5 YEAR STARTEGY BOTTOM.xlsx").dropna(subset=['Unnamed: 2'])
    b_list = [str(x).strip() for x in b_df['Unnamed: 2'].tolist() if "STARTEGIC" not in str(x)][:4]
    
    l_df = pd.read_excel("lEFT ANNUAL OBJECTIVE.xlsx").dropna(subset=['Unnamed: 3'])
    l_list = [str(x).strip() for x in l_df['Unnamed: 3'].tolist() if "OBJECTIVES" not in str(x)][:4]
    
    r_df = pd.read_excel("KPI Annaul Right side.xlsx").dropna(subset=['Unnamed: 3'])
    r_list = [str(x).strip() for x in r_df['Unnamed: 3'].tolist() if "OBJECTIVES" not in str(x)][:4]
    
    t_df = pd.read_excel("Prioritizezed activities Top.xlsx").dropna(subset=['Unnamed: 3'])
    t_list = [str(x).replace('\n', ' ').strip() for x in t_df['Unnamed: 3'].tolist() if "ACTIVITIES" not in str(x)][:3]
    
    return b_list, l_list, r_list, t_list

bottom_items, left_items, right_items, top_items = get_verified_data()

# --- GENERATING THE EXACT DIAMOND GRIDS VISUALLY ---
top_html = "".join([f"<div class='item-text'>🔹 {item[:120]}...</div>" for item in top_items])
left_html = "".join([f"<div class='item-text'>🎯 {item}</div>" for item in left_items])
right_html = "".join([f"<div class='item-text'>📊 {item}</div>" for item in right_items])
bottom_html = "".join([f"<div class='item-text'>🔹 {item}</div>" for item in bottom_items])

st.markdown(f"""
    <div class="x-matrix-container">
        <!-- TOP: HOW / ACTION ITEMS -->
        <div class="matrix-box top-box">
            <div class="box-header">HOW</div>
            <div class="box-subheader">Action Items (Priorities)</div>
            {top_html}
        </div>
        
        <!-- LEFT: HOW FAR / OBJECTIVES -->
        <div class="matrix-box left-box">
            <div class="box-header">HOW FAR</div>
            <div class="box-subheader">Annual Objectives</div>
            {left_html}
        </div>
        
        <!-- RIGHT: HOW MUCH / ACTION PROGRAMS -->
        <div class="matrix-box right-box">
            <div class="box-header">HOW MUCH</div>
            <div class="box-subheader">Action Programs (KPIs)</div>
            {right_html}
        </div>
        
        <!-- BOTTOM: WHAT / MEASURES & TARGETS -->
        <div class="matrix-box bottom-box">
            <div class="box-header">WHAT</div>
            <div class="box-subheader">Measures & Targets (5-Yr Strategy)</div>
            {bottom_html}
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("💡 ይህ የተሟላ የሆሺን ማትሪክስ እቅድ በምስሉ ላይ በተቀመጠው የአቅጣጫ መለኪያ መሰረት በቀጥታ ከኤክሴል ፋይሎችዎ ላይ የለቀመ ነው።")
