import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time

# 1. பக்க வடிவமைப்பு (Page Layout)
st.set_page_config(page_title="Sentinel AI - Cyber Defense Pro", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Cyberpunk Look - இங்கே 'unsafe_allow_html=True' என்று சரியாக மாற்றப்பட்டுள்ளது
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    div[data-testid="stMetricValue"] > div { color: #00CC96; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (மெனு மற்றும் சிஸ்டம் ஸ்டேட்டஸ்) ---
with st.sidebar:
    st.title("🛡️ Sentinel AI Pro")
    st.markdown("---")
    menu = st.sidebar.radio("Navigation", ["🌐 Dashboard", "🧠 AI Threat Analysis", "📝 System Logs", "⚙️ Settings"])
    st.markdown("---")
    st.success("System: Operational")
    st.info(f"Last Scan: {time.strftime('%H:%M:%S')}")
    if st.button("Reboot Firewall"):
        with st.spinner("Restarting Security Layers..."):
            time.sleep(2)
            st.rerun()

# --- 3. DASHBOARD PAGE ---
if "Dashboard" in menu:
    st.title("🌐 Cyber Defense Real-time Dashboard")
    st.write("AI-Powered Network Monitoring & Threat Mitigation")

    # மெட்ரிக்ஸ் (Metrics)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Attacks Blocked", "1,482", "+14%")
    m2.metric("Network Integrity", "99.8%", "0.2%")
    m3.metric("AI Confidence", "96.4%", "-0.1%")
    m4.metric("Active Sessions", "24", "4")

    st.markdown("---")

    # கிராஃப்கள் (Charts)
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📊 Live Traffic & Threat Mitigation")
        # 21 இண்டர்வல்ஸ் கணக்குப்படி சமமான டேட்டா
        intervals = list(range(21))
        chart_data = pd.DataFrame({
            'Intervals': intervals,
            'Threat Intensity': np.random.randint(10, 60, 21),
            'AI Defense Power': np.random.randint(40, 100, 21)
        })
        fig = px.area(chart_data, x='Intervals', y=['Threat Intensity', 'AI Defense Power'],
                      color_discrete_map={"Threat Intensity": "#FF4B4B", "AI Defense Power": "#00CC96"},
                      template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("🌍 Top Attack Sources")
        map_data = pd.DataFrame({
            'Country': ['USA', 'China', 'Russia', 'Germany', 'India'],
            'Attacks': [450, 310, 280, 120, 95]
        })
        fig_pie = px.pie(map_data, values='Attacks', names='Country', hole=0.4, 
                         color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_pie, use_container_width=True)

    # AI Prediction Alert
    st.warning("🤖 **AI Prediction:** High probability of SQL Injection attempt detected in Port 8080. Automating Patch...")

# --- 4. AI THREAT ANALYSIS PAGE ---
elif "AI Threat Analysis" in menu:
    st.title("🧠 Advanced AI Anomaly Detection")
    st.write("Upload server logs to identify patterns using Machine Learning.")
    
    uploaded_file = st.file_uploader("Upload Log File (CSV/TXT)", type=['csv', 'txt'])
    if uploaded_file:
        with st.status("AI is analyzing patterns...", expanded=True) as status:
            st.write("Extracting IP Metadata...")
            time.sleep(1)
            st.write("Running Neural Network Scan...")
            time.sleep(2)
            status.update(label="Analysis Complete: 2 Suspicious IP patterns identified.", state="complete")
            st.error("Warning: Unusual traffic from 192.168.1.45 detected.")
    
    st.info("💡 **Tip:** Use our pre-trained 'Mimicry Agent' to bait hackers into a Honeypot.")

# --- 5. SYSTEM LOGS PAGE (LIVE FEED) ---
elif "System Logs" in menu:
    st.title("📝 Real-time Security Logs")
    
    if st.button("Refresh Live Logs"):
        st.rerun()

    log_list = []
    for _ in range(15):
        log_list.append({
            "Timestamp": time.strftime("%H:%M:%S"),
            "Source IP": fake.ipv4(),
            "Event": np.random.choice(["Brute Force Attempt", "Port Scan", "Unauthorized Access", "File Integrity Check"]),
            "Severity": np.random.choice(["Low", "Medium", "High", "Critical"]),
            "Action": "Blocked by AI"
        })
    
    df_logs = pd.DataFrame(log_list)
    
    # Severity கலர் கோடிங்
    def color_severity(val):
        if val == 'Critical': color = 'red'
        elif val == 'High': color = 'orange'
        elif val == 'Medium': color = 'yellow'
        else: color = 'white'
        return f'color: {color}'

    st.dataframe(df_logs.style.applymap(color_severity, subset=['Severity']), use_container_width=True)

# --- 6. SETTINGS ---
else:
    st.title("⚙️ System Settings")
    st.toggle("Enable Autonomous Defense", value=True)
    st.toggle("Dark Mode (Force)", value=True)
    st.slider("AI Sensitivity Level", 0, 100, 85)
    st.text_input("Admin Notification Email", "admin@sentinel-ai.com")

# --- CHATBOT FLOATING ASSISTANT ---
st.markdown("---")
with st.expander("💬 Chat with Sentinel Assistant"):
    query = st.text_input("Ask a security question:")
    if query:
        st.write(f"**Sentinel AI:** Analyzing your request regarding '{query}'... Currently, all firewall layers are secure and no active breaches are found.")

