import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Settings & Visual Styling
st.set_page_config(page_title="HATMPLC Ultimate X-Matrix Hub", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Ethiopic', sans-serif;
        background-color: #f8fafc;
    }
    
    /* X-Matrix Circular/Diamond Core Layout */
    .matrix-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e293b;
        margin-bottom: 25px;
        letter-spacing: 2px;
    }
    
    .quadrant-top {
        background: linear-gradient(135deg, #fca5a5 0%, #ef4444 100%);
        color: white;
        padding: 20px;
        border-radius: 12px 12px 0 0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .quadrant-left {
        background: linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%);
        color: #14532d;
        padding: 20px;
        border-radius: 12px 0 0 12px;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .quadrant-right {
        background: linear-gradient(135deg, #bfdbfe 0%, #3b82f6 100%);
        color: white;
        padding: 20px;
        border-radius: 0 12px 12px 0;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .quadrant-bottom {
        background: linear-gradient(135deg, #fed7aa 0%, #f97316 100%);
        color: white;
        padding: 20px;
        border-radius: 0 0 12px 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-top: 15px;
    }
    
    .list-item {
        background: rgba(255, 255, 255, 0.25);
        margin: 6px 0;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 0.9rem;
        text-align: left;
    }
    .list-item-dark {
        background: rgba(0, 0, 0, 0.06);
        margin: 6px 0;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 0.9rem;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Extract verified live structures from the files
@st.cache_data
def get_verified_matrix_data():
    b_df = pd.read_excel("5 YEAR STARTEGY BOTTOM.xlsx").dropna(subset=['Unnamed: 2'])
    bottom_list = b_df['Unnamed: 2'].iloc[3:7].tolist()
    
    l_df = pd.read_excel("lEFT ANNUAL OBJECTIVE.xlsx").dropna(subset=['Unnamed: 3'])
    left_list = [x for x in l_df['Unnamed: 3'].tolist() if "OBJECTIVES" not in str(x)][0:4]
    
    r_df = pd.read_excel("KPI Annaul Right side.xlsx").dropna(subset=['Unnamed: 3'])
    right_list = [x for x in r_df['Unnamed: 3'].tolist() if "OBJECTIVES" not in str(x)][0:4]
    
    t_df = pd.read_excel("Prioritizezed activities Top.xlsx").dropna(subset=['Unnamed: 3'])
    top_list = [x for x in t_df['Unnamed: 3'].tolist() if "ACTIVITIES" not in str(x)][0:4]
    
    return bottom_list, left_list, right_list, top_list

bottom_v, left_v, right_v, top_v = get_verified_matrix_data()

st.markdown("<div class='matrix-title'>🔺 INTERACTIVE HOSHIN KANRI X-MATRIX 🔺</div>", unsafe_allow_html=True)

# --- 3. Geometric X-Matrix Visual Rendering (As requested in image format) ---

# TOP ROW: HOW (Action Items)
st.markdown("<div class='quadrant-top'><h2>🔼 HOW</h2><b>Action Items (ቅድሚያ የሚሰጣቸው ተግባራት)</b></div>", unsafe_allow_html=True)
col_top1, col_top2 = st.columns(2)
with col_top1:
    st.markdown(f"<div class='list-item'>{top_v[0][:150]}...</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='list-item'>{top_v[1][:150]}...</div>", unsafe_allow_html=True)
with col_top2:
    st.markdown(f"<div class='list-item'>{top_v[2][:150]}...</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='list-item'>{top_v[3][:150]}...</div>", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

# MIDDLE ROW: LEFT (HOW FAR) & RIGHT (HOW MUCH)
col_left_side, col_right_side = st.columns(2)

with col_left_side:
    st.markdown("<div class='quadrant-left'><h2>◀️ HOW FAR</h2><b>Objectives (ዓመታዊ ዓላማዎች)</b>", unsafe_allow_html=True)
    for idx, item in enumerate(left_v):
        st.markdown(f"<div class='list-item-dark'><b>{idx+1}.</b> {item}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_right_side:
    st.markdown("<div class='quadrant-right'><h2>▶️ HOW MUCH</h2><b>Action Programs (የቁልፍ አፈጻጸም አመልካቾች)</b>", unsafe_allow_html=True)
    for idx, item in enumerate(right_v):
        st.markdown(f"<div class='list-item'><b>{idx+1}.</b> {item}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# BOTTOM ROW: WHAT (Measures & Targets)
st.markdown("<div class='quadrant-bottom'><h2>🔽 WHAT</h2><b>Measures & Targets (የ5 ዓመት ስትራቴጂካዊ ግቦች)</b></div>", unsafe_allow_html=True)
col_bot1, col_bot2 = st.columns(2)
with col_bot1:
    st.markdown(f"<div class='list-item-dark'>🎯 {bottom_v[0]}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='list-item-dark'>🎯 {bottom_v[1]}</div>", unsafe_allow_html=True)
with col_bot2:
    st.markdown(f"<div class='list-item-dark'>🎯 {bottom_v[2]}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='list-item-dark'>🎯 {bottom_v[3]}</div>", unsafe_allow_html=True)

st.markdown("---")

# 4. Interactive Data Correlation Grid (Lower section)
st.markdown("### 🔄 Cross-Functional Dynamic Linkage Grid")
corr_matrix = pd.DataFrame([
    ["● Strong", "○ Medium", "❌ None", "● Strong"],
    ["❌ None", "● Strong", "○ Medium", "❌ None"],
    ["○ Medium", "❌ None", "● Strong", "● Strong"],
    ["● Strong", "○ Medium", "❌ None", "○ Medium"]
], columns=["HOW (Action Items)", "HOW FAR (Objectives)", "HOW MUCH (KPIs)", "WHAT (Strategy)"],
   index=[f"Project Grid Alpha {i+1}" for i in range(4)])

st.table(corr_matrix)
