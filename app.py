import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time
import requests

# 1. பக்க வடிவமைப்பு (Page Layout)
st.set_page_config(page_title="Sentinel AI - Cyber Defense Pro", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Cyberpunk Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    div[data-testid="stMetricValue"] > div { color: #00CC96; }
    .stAlert { border-radius: 10px; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE DATA GENERATOR (நிஜமான அச்சுறுத்தல் தரவுகளைப் போல உருவாக்குதல்) ---
def get_live_threats():
    threats = ["Brute Force", "SQL Injection", "DDoS", "Malware Delivery", "Port Scan", "Phishing"]
    countries = ["USA", "China", "Russia", "India", "Germany", "Brazil", "UK", "Canada"]
    data = []
    for _ in range(6):
        data.append({
            "Time": time.strftime("%H:%M:%S"),
            "Attacker IP": fake.ipv4(),
            "Origin": np.random.choice(countries),
            "Method": np.random.choice(threats),
            "Risk Score": np.random.randint(40, 100)
        })
    return pd.DataFrame(data)

# --- 3. SIDEBAR (மெனு மற்றும் சிஸ்டம் ஸ்டேட்டஸ்) ---
with st.sidebar:
    st.title("🛡️ Sentinel AI Pro")
    st.markdown("---")
    menu = st.radio("Navigation", ["🌐 Dashboard", "🧠 AI Threat Analysis", "📝 System Logs", "⚙️ Settings"])
    st.markdown("---")
    st.success("System: Operational")
    st.info(f"Last Update: {time.strftime('%H:%M:%S')}")
    
    # Auto-refresh வசதிக்கான பட்டன்
    if st.button("Manual Force Scan"):
        with st.spinner("Analyzing Network Packets..."):
            time.sleep(2)
            st.rerun()

# --- 4. DASHBOARD PAGE ---
if "Dashboard" in menu:
    st.title("🌐 Cyber Defense Real-time Dashboard")
    st.write("AI-Powered Network Monitoring & Global Threat Intelligence")

    # மெட்ரிக்ஸ் (Metrics)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Attacks Blocked", f"{np.random.randint(1400, 1600)}", "+14%")
    m2.metric("Network Health", "99.8%", "0.2%")
    m3.metric("AI Accuracy", "96.4%", "-0.1%")
    m4.metric("Active Sessions", f"{np.random.randint(20, 45)}", "4")

    st.markdown("---")

    # கிராஃப்கள் மற்றும் லைவ் ஃபீட் (Charts & Live Feed)
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📊 Live Traffic & AI Mitigation Power")
        intervals = list(range(21))
        chart_data = pd.DataFrame({
            'Intervals': intervals,
            'Threat Intensity': np.random.randint(10, 70, 21),
            'AI Defense Power': np.random.randint(50, 100, 21)
        })
        fig = px.area(chart_data, x='Intervals', y=['Threat Intensity', 'AI Defense Power'],
                      color_discrete_map={"Threat Intensity": "#FF4B4B", "AI Defense Power": "#00CC96"},
                      template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("🌍 Threat Origin Map")
        map_data = pd.DataFrame({
            'Country': ['USA', 'China', 'Russia', 'India', 'Germany'],
            'Threats': np.random.randint(10, 100, 5)
        })
        fig_pie = px.pie(map_data, values='Threats', names='Country', hole=0.4, 
                         color_discrete_sequence=px.colors.sequential.Reds_r)
        st.plotly_chart(fig_pie, use_container_width=True)

    # LIVE THREAT FEED (இதுதான் புதிய அம்சம்)
    st.markdown("---")
    st.subheader("🎯 Live Global Threat Intelligence Feed")
    live_df = get_live_threats()
    
    # கலர் கோடிங் (90-க்கு மேல் இருந்தால் சிகப்பு)
    def highlight_risk(val):
        color = '#931a1a' if val > 85 else '#161b22'
        return f'background-color: {color}'

    st.table(live_df.style.applymap(highlight_risk, subset=['Risk Score']))
    
    st.warning(f"🤖 **AI Notice:** Blocked a {live_df['Method'][0]} attempt from {live_df['Attacker IP'][0]} ({live_df['Origin'][0]}) just now.")

# --- 5. AI THREAT ANALYSIS PAGE ---
elif "AI Threat Analysis" in menu:
    st.title("🧠 Advanced AI Anomaly Detection")
    st.write("Upload server logs to identify patterns using Machine Learning.")
    
    uploaded_file = st.file_uploader("Upload Log File (CSV/TXT)", type=['csv', 'txt'])
    if uploaded_file:
        with st.status("AI is analyzing patterns...", expanded=True) as status:
            st.write("Decompressing Logs...")
            time.sleep(1)
            st.write("Searching for Signature Matches...")
            time.sleep(1.5)
            st.write("Heuristic Pattern Matching...")
            time.sleep(1)
            status.update(label="Analysis Complete: Suspicious IP patterns identified.", state="complete")
            st.error("Warning: High-risk anomaly detected in User Agent String.")

# --- 6. SYSTEM LOGS PAGE ---
elif "System Logs" in menu:
    st.title("📝 Detailed System Events")
    
    log_list = []
    for _ in range(12):
        log_list.append({
            "Timestamp": time.strftime("%H:%M:%S"),
            "Event": np.random.choice(["SSH Login Attempt", "Packet Rejection", "DNS Query Blocked", "SSL Handshake Success"]),
            "Severity": np.random.choice(["Low", "Medium", "High", "Critical"]),
            "IP Address": fake.ipv4()
        })
    st.dataframe(pd.DataFrame(log_list), use_container_width=True)

# --- 7. SETTINGS ---
else:
    st.title("⚙️ System Configuration")
    st.toggle("Enable Autonomous Mitigation", value=True)
    st.toggle("Auto-Refresh (15s)", value=True)
    st.slider("AI Threat Threshold", 0, 100, 85)
    st.text_input("Incident Response Email", "admin@sentinel-ai.com")

# --- CHATBOT ASSISTANT ---
st.markdown("---")
with st.expander("💬 Chat with Sentinel AI Assistant"):
    query = st.text_input("Ask a security question:")
    if query:
        st.write(f"**Sentinel AI:** Investigating '{query}'... Our neural network confirms that all defense layers (WAF, IDS, IPS) are currently active and secure.")

