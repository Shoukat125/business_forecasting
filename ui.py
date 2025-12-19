import streamlit as st
import plotly.graph_objects as go

def apply_custom_css():
    MAIN_BG = "#E8F0F1" 
    SIDEBAR_BG = "#022b8b"
    TEXT_LIGHT = "#E9EBF0"
    TEXT_DARK = "#1e293b" 

    st.markdown(f"""
    <style>
    html, body, [data-testid="stApp"] {{ background-color: {MAIN_BG}; }}
    section[data-testid="stSidebar"] {{ background-color: {SIDEBAR_BG}; }}
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] h3 {{ color: {TEXT_LIGHT} !important; }}
    .stAlert p {{ color: white !important; }}
    
    .stButton > button {{
        background: linear-gradient(90deg,#ff6f3c,#ff3d00);
        color: white;
        border-radius: 999px;
        font-weight: 600;
        width: 100%;
        border: none;
    }}
    .result-box {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 10px;
    }}
    header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

def display_header():
    st.markdown("<h1 style='text-align:center; color:#1e293b;'>Business Forecasting using AI</h1>", unsafe_allow_html=True)
    st.write("---")

def display_result_card(profit, revenue):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="result-box"><h3 style="color:#64748b;">Net Profit</h3><h1 style="color:#10b981; font-size: 35px;">£{profit:,.2f}</h1></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="result-box"><h3 style="color:#64748b;">Total Revenue</h3><h1 style="color:#3b82f6; font-size: 35px;">£{revenue:,.2f}</h1></div>', unsafe_allow_html=True)

def display_graphs(profit, revenue):
    st.write("### 📈 Visual Analysis")
    col1, col2 = st.columns(2)

    with col1:
        # Profit Gauge Chart
        fig_profit = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = profit,
            number = {'prefix': "£"},
            title = {'text': "Profit Level", 'font': {'size': 20}},
            gauge = {
                'axis': {'range': [None, profit*1.5 if profit > 0 else 1000]},
                'bar': {'color': "#10b981"},
                'steps': [{'range': [0, profit], 'color': "#f0fff4"}]}
        ))
        fig_profit.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_profit, use_container_width=True)

    with col2:
        # Revenue vs Profit Comparison
        fig_compare = go.Figure(data=[
            go.Bar(name='Revenue', x=['Business Metrics'], y=[revenue], marker_color='#3b82f6'),
            go.Bar(name='Profit', x=['Business Metrics'], y=[profit], marker_color='#10b981')
        ])
        fig_compare.update_layout(barmode='group', height=300, margin=dict(l=20, r=20, t=50, b=20), title="Revenue vs Profit")
        st.plotly_chart(fig_compare, use_container_width=True)