import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page layout
st.set_page_config(page_title="HATMPLC Hoshin Dashboard", layout="wide")

# Custom CSS for Noto Sans Ethiopic feel and clean interface
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Ethiopic:wght@300;400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Ethiopic', sans-serif;
    }
    .metric-card {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1e3a8a;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.title("🏭 HATMPLC OPERATIONAL EXCELLENCE STRATEGIC DEPLOYMENT")
st.subheader("የሆሺን ኤክስ-ማትሪክስ የቀን ተቀን አፈጻጸም መከታተያ ሰሌዳ (Live Hoshin X-Matrix Dashboard)")

st.markdown("---")

# Sidebar navigation / filter
st.sidebar.header("🎛️ የአፈጻጸም መቆጣጠሪያ (Control Panel)")
selected_dept = st.sidebar.selectbox("ክፍለ-ሥራ መምረጥ (Filter by Department)", 
    ["ሁሉም ክፍሎች (All)", "Purchase & PIQA", "Plant Engineering (PE)", "Production Dept (PD)", "Finance & Top Mgt", "PMITS"])

# 1. Macro KPIs Scorecard Row
st.markdown("### 🎯 ዋና ዋና የኩባንያው ውጤት አመልካቾች (Top Corporate KPIs)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card"><b>የዕለት ተዕለት ምርታማነት (Daily Output)</b><h2 style="color:#1e3a8a;margin:5px 0;">37.3 / 70 T</h2><small>መነሻ: 22.2 ቶን | ግብ: 70 ቶን</small></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card" style="border-left-color:#10b981;"><b>ዓመታዊ የጎማ ሽያጭ (Annual Sales)</b><h2 style="color:#10b981;margin:5px 0;">5.77 ቢሊዮን ብር</h2><small>መነሻ: 1.1 ቢሊዮን | ግብ: 5.77 ቢ</small></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card" style="border-left-color:#f59e0b;"><b>የማምረቻ መሣሪያዎች ዝግጁነት</b><h2 style="color:#f59e0b;margin:5px 0;">93.28% / 96%</h2><small>መነሻ: 88.5% | የታለመው: 96%</small></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card" style="border-left-color:#ef4444;"><b>የመለዋወጫ አቅርቦት ጊዜ</b><h2 style="color:#ef4444;margin:5px 0;">21 ቀናት</h2><small>መነሻ: 115 ቀናት | የታለመው: 21 ቀን</small></div>', unsafe_allow_html=True)

st.markdown("---")

# 2. Main Row: Strategic Pillars Progress Chart & Department Trackers
left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("### 📊 የዓመታዊ እቅድ ዋና ጉዳዮች አፈጻጸም (Strategic Pillars Progress)")
    pillars_data = pd.DataFrame({
        "Strategic Pillar": ["የገበያ ልማት (Market Dev)", "ጠንካራ አቅርቦት ሰንሰለት (Supply Chain)", "የአቅም ግንባታ (Capacity)", "ወጪን መቀነስ (Cost Reduction)"],
        "Progress (%)": [78, 85, 90, 72]
    })
    fig = px.bar(pillars_data, x="Strategic Pillar", y="Progress (%)", 
                 color="Strategic Pillar", text="Progress (%)",
                 color_discrete_sequence=["#3b82f6", "#10b981", "#f59e0b", "#ef4444"])
    fig.update_layout(showlegend=False, height=350, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.markdown("### 👥 የክፍለ-ሥራ ባለቤቶች ዕለታዊ ክትትል (Resource Owners Tracker)")
    
    owners = [
        {"dept": "Purchase & PIQA", "task": "የጥሬ ዕቃ አቅርቦትን ማረጋጋትና ጥራትን መቆጣጠር (1.1.4)", "status": "በእቅዱ መሠረት (ON TRACK)", "color": "green"},
        {"dept": "Plant Engineering (PE)", "task": "የማምረቻ መሣሪያዎችን ዝግጁነት ከ91.68% ወደ 93.28% ማሳደግ (2.3.2)", "status": "በእቅዱ መሠረት (ON TRACK)", "color": "green"},
        {"dept": "Production Dept (PD)", "task": "የዕለት ምርታማነትን ወደ 37.3 ቶን ማሳደግ (2.3.4)", "status": "ትኩረት ያስፈልገዋል (AT RISK)", "color": "orange"},
        {"dept": "Finance & Top Mgt", "task": "የውጭ ምንዛሪ ግኝትን ማመቻቸትና ወጪ መቆጣጠር (1.1.3)", "status": "በእቅዱ መሠረት (ON TRACK)", "color": "green"},
        {"dept": "PMITS", "task": "የአሰራር ስርዓቶችን ቀጣይነት ማረጋገጥና አፈጻጸም ማሳደግ (2.1.1)", "status": "በእቅዱ መሠረት (ON TRACK)", "color": "green"},
    ]
    
    for owner in owners:
        if selected_dept == "ሁሉም ክፍሎች (All)" or selected_dept == owner["dept"]:
            color_hex = "#10b981" if owner["color"] == "green" else "#f59e0b"
            st.markdown(f"""
            <div style="background-color: white; padding: 12px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <b>{owner['dept']}</b><br>
                    <span style="font-size: 0.85rem; color: #64748b;">{owner['task']}</span>
                </div>
                <span style="background-color: {color_hex}22; color: {color_hex}; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold;">
                    {owner['status']}
                </span>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# 3. Interlocking Hoshin Matrix (Correlation View)
st.markdown("### 🔄 የስትራቴጂካዊ ፕሮጀክቶች እና የKPIs ትስስር ማትሪክስ (Correlation Matrix Grid)")
matrix_df = pd.DataFrame([
    ["የጥሬ ዕቃ ግዢ ፍላጎትን ማሳደግ", "Strong (3)", "None (0)", "None (0)", "Medium (1)", "Strong (3)"],
    ["የመለዋወጫ ግዢ ሥርዓትን ማዘመን", "None (0)", "Strong (3)", "Strong (3)", "None (0)", "Medium (1)"],
    ["የማምረቻ መሣሪያዎች አጠቃላይ ጥገና", "None (0)", "Medium (1)", "Strong (3)", "Strong (3)", "Medium (1)"],
    ["አዳዲስ የፒሲአር እና ኤልቲአር ምርቶች", "Medium (1)", "None (0)", "Medium (1)", "Strong (3)", "None (0)"],
    ["የስክራፕ እና የብክነት መጠንን መቀነስ", "None (0)", "None (0)", "Medium (1)", "Medium (1)", "Strong (3)"]
], columns=["ስትራቴጂካዊ ፕሮጀክቶች (Projects)", "የጥሬ ዕቃ አቅርቦት", "የአቅርቦት ጊዜ ቅነሳ", "መሣሪያዎች ዝግጁነት", "የዕለት ምርታማነት", "የዋጋ ቆጣቢነት"])

st.dataframe(matrix_df.set_index("ስትራቴጂካዊ ፕሮጀክቶች (Projects)"), use_container_width=True)
st.caption("* ማስታወሻ: Strong (3) = ጠንካራ ትስስር | Medium (1) = መካከለኛ ትስስር | None (0) = ትስስር የሌለው")

app.py
app.py
Loading app.py.
Displaying app.py.
