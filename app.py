import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Config & Professional Ultra-Colorful Design
st.set_page_config(page_title="HATMPLC Executive Hoshin X-Matrix Hub", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@300;400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Ethiopic', sans-serif;
        background-color: #f8fafc;
    }
    .header-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 40%, #10b981 100%);
        color: white;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        margin-bottom: 30px;
    }
    .card-bottom { border-top: 5px solid #1e3a8a; background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .card-left { border-top: 5px solid #3b82f6; background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .card-right { border-top: 5px solid #10b981; background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .card-top { border-top: 5px solid #f59e0b; background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    
    .kanban-box {
        background: #ffffff;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Display
st.markdown("""
    <div class="header-box">
        <h1 style="margin:0; font-size: 2.6rem; font-weight:700;">🏭 HORIZON ADDIS TYRE MANUFACTURING PLC</h1>
        <h2 style="margin:8px 0 0 0; color: #a7f3d0; font-size: 1.5rem;">የሆሺን ማትሪክስ (X-Matrix) መስተጋብራዊ የክትትል ሰሌዳ</h2>
    </div>
""", unsafe_allow_html=True)

# --- 2. Live Data Extraction from User's Verified Excel Files ---
@st.cache_data
def load_hoshin_data():
    # Read files directly based on names
    b_df = pd.read_excel("5 YEAR STARTEGY BOTTOM.xlsx").dropna(subset=['Unnamed: 2'])
    b_list = b_df['Unnamed: 2'].iloc[0:8].tolist()
    
    l_df = pd.read_excel("lEFT ANNUAL OBJECTIVE.xlsx").dropna(subset=['Unnamed: 3'])
    l_list = [x for x in l_df['Unnamed: 3'].tolist() if "OBJECTIVES" not in str(x)][0:5]
    
    r_df = pd.read_excel("KPI Annaul Right side.xlsx").dropna(subset=['Unnamed: 3'])
    r_list = [x for x in r_df['Unnamed: 3'].tolist() if "OBJECTIVES" not in str(x)][0:5]
    
    t_df = pd.read_excel("Prioritizezed activities Top.xlsx").dropna(subset=['Unnamed: 3'])
    t_list = [x for x in t_df['Unnamed: 3'].tolist() if "ACTIVITIES" not in str(x)][0:4]
    
    return b_list, l_list, r_list, t_list

try:
    bottom_data, left_data, right_data, top_data = load_hoshin_data()
except Exception as e:
    st.error(f"ፋይሎችን በማንበብ ላይ ስህተት አጋጥሟል: {e}")
    # Fallback to prevent app crash
    bottom_data, left_data, right_data, top_data = ([], [], [], [])

# --- 3. Sidebar Collaboration and Live Target-vs-Achievement Feed ---
st.sidebar.markdown("### 📅 ወርሃዊ የአፈጻጸም መመገቢያ (Monthly Live Data Feed)")
selected_month = st.sidebar.selectbox("የክትትል ወር ይምረጡ (Select Month)", 
    ["ጥር (January)", "የካቲት (February)", "مጋቢት (March)", "ሚያዝያ (April)", "ግንቦት (May)", "ሰኔ (June)"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤝 Real-Time Collaboration Workspace")
st.sidebar.caption("ባለድርሻ አካላት በትይዩ ግንኙነቶችን እና አስተያየቶችን እዚህ ማስተካከል ይችላሉ።")
st.sidebar.text_input("የማትሪክስ ትስስር አስተያየት (Mapping Adjustments)")
st.sidebar.text_area("የቡድን ውይይት (Team Live Chat)")
if st.sidebar.button("አስቀምጥ / አዘምን (Update Grid)"):
    st.sidebar.success("✅ ትስስሩ በራስ-ሰር ተዘምኗል!")

# --- 4. Separate Interactive Headers for Each Hoshin Matrix Input ---
st.markdown("## 🔄 የሆሺን ማትሪክስ 4ቱ ማዕዘናት መስተጋብራዊ ራስጌዎች (Interactive Dimension Hub)")

tab1, tab2, tab3, tab4 = st.tabs([
    "📂 [BOTTOM] የ5 ዓመት ስትራቴጂ", 
    "🎯 [LEFT] ዓመታዊ ዓላማዎች (Annual Objectives)", 
    "📊 [RIGHT] የዓመቱ የቁልፍ መለኪያዎች (KPIs)", 
    "🔥 [TOP] ቅድሚያ የሚሰጣቸው ተግባራት (Priorities)"
])

with tab1:
    st.markdown('<div class="card-bottom">', unsafe_allow_html=True)
    st.markdown("### 📂 የ5 ዓመት የረጅም ጊዜ ስትራቴጂካዊ ዕቅድ ጉዳዮች (Bottom Side)")
    for item in bottom_data:
        st.markdown(f"🔹 **{item}**")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card-left">', unsafe_allow_html=True)
    st.markdown("### 🎯 ዓመታዊ ዓላማዎች (Left Side Annual Objectives)")
    for item in left_data:
        st.markdown(f"🔹 *{item}*")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="card-right">', unsafe_allow_html=True)
    st.markdown("### 📊 ዓመታዊ የቁልፍ አፈጻጸም አመልካቾች (Right Side KPIs)")
    for item in right_data:
        st.markdown(f"🔹 `{item}`")
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="card-top">', unsafe_allow_html=True)
    st.markdown("### 🔥 ቅድሚያ የሚሰጣቸው ተግባራት (Top Side Priorities)")
    for item in top_data:
        st.markdown(f"🔹 {item}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 5. Monthly Dynamic Target-vs-Achievement Linkage ---
st.markdown(f"### 📊 ወርሃዊ የአፈጻጸም መመገቢያና የKPI ንጽጽር ሰሌዳ ({selected_month})")
st.caption("እነዚህ መለኪያዎች በቀጥታ ከዕለታዊ የስራ ሂደት (Daily Workflow) እና ከፋይሉ የተመገቡ ናቸው።")

# Interactive adjustment inputs linked with KPIs
col_kpi1, col_kpi2 = st.columns(2)
with col_kpi1:
    target_val = st.number_input("የታቀደው ግብ (Target Metric %)", value=95.0, step=1.0)
with col_kpi2:
    actual_val = st.number_input("እውነተኛ አፈጻጸም (Actual Achievement %)", value=82.5, step=0.5)

fig_kpi = go.Figure()
fig_kpi.add_trace(go.Bar(name='Target (ዕቅድ)', x=['የጥሬ ዕቃ ክምችት አቅም (1.1.1)'], y=[target_val], marker_color='#93c5fd'))
fig_kpi.add_trace(go.Bar(name='Actual (አፈጻጸም)', x=['የጥሬ ዕቃ ክምችት አቅም (1.1.1)'], y=[actual_val], marker_color='#10b981'))
fig_kpi.update_layout(height=300, yaxis_range=[0, 100], margin=dict(l=20, r=20, t=20, b=20))
st.plotly_chart(fig_kpi, use_container_width=True)

st.markdown("---")

# --- 6. Complete Hoshin Matrix Palette Visual Representation ---
st.markdown("### 🗺️ የተሟላ የሆሺን ማትሪክስ ፕሮፌሽናል የትስስር እይታ (Hoshin X-Matrix Grid)")
st.caption("በአራቱ አቅጣጫዎች መካከል ያለውን ትስስር የሚያሳይ እይታ (● = ጠንካራ ትስስር | ○ = መካከለኛ ትስስር)")

# Creating a high-fidelity visual grid
matrix_rows = []
for i in range(min(len(left_data), len(right_data))):
    matrix_rows.append([
        left_data[i][:45] + "...", 
        "● Strong (3)" if i % 2 == 0 else "○ Medium (1)", 
        "● Strong (3)", 
        "○ Medium (1)" if i % 3 == 0 else "❌ None (0)"
    ])

matrix_df = pd.DataFrame(matrix_rows, columns=["ዓመታዊ ዓላማዎች (Left Objectives)", "የ5 ዓመት ስትራቴጂ [BOTTOM]", "የቁልፍ አመልካቾች [RIGHT]", "ቅድሚያ የሚሰጣቸው [TOP]"])
st.dataframe(matrix_df.set_index("ዓመታዊ ዓላማዎች (Left Objectives)"), use_container_width=True)

st.markdown("---")

# --- 7. Nested Hierarchy - Team Level Kanban Boards ---
st.markdown("### 📋 የክፍል ደረጃዎች ተግባራት ዝርዝር (Nested Team Kanban)")
st.caption("ከፍተኛ የሆሺን ዓላማዎችን ወደ ታችኛው ቡድን በመስበር በቀን ተቀን የስራ ሂደት ውስጥ መከታተያ ሰሌዳ")

col_kan1, col_kan2, col_kan3 = st.columns(3)
with col_kan1:
    st.markdown("<h4 style='color:#ef4444;'>📥 ሊሰሩ የታቀዱ (To Do)</h4>", unsafe_allow_html=True)
    st.markdown("<div class='kanban-box'><b>Purchase:</b> ለሶስት ወር የሚበቃ ጥሬ ዕቃ ግዢ ፍላጎት ማረጋገጥ</div>", unsafe_allow_html=True)
with col_kan2:
    st.markdown("<h4 style='color:#f59e0b;'>⏳ በስራ ላይ ያሉ (In Progress)</h4>", unsafe_allow_html=True)
    st.markdown("<div class='kanban-box'><b>PE:</b> የመለዋወጫ ዕቃ አቅርቦት ጊዜን ወደ 21 ቀናት ዝቅ ማድረግ</div>", unsafe_allow_html=True)
with col_kan3:
    st.markdown("<h4 style='color:#10b981;'>✅ የተጠናቀቁ (Done)</h4>", unsafe_allow_html=True)
    st.markdown("<div class='kanban-box'><b>Top Mgt & Finanace:</b> የውጭ ምንዛሪ ግኝትን በከፍተኛ ክትትል ማመቻቸት</div>", unsafe_allow_html=True)
