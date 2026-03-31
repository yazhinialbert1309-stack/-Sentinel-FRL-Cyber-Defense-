import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="Sentinel AI - Cyber Defense Pro", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    div[data-testid="stMetricValue"] > div { color: #00CC96; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LIVE DATA GENERATOR ---
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

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Sentinel AI Pro")
    st.markdown("---")
    menu = st.radio("Navigation", ["🌐 Dashboard", "🧠 AI Threat Analysis", "📝 System Logs", "⚙️ Settings"])
    st.markdown("---")
    st.success("System: Operational")
    st.info(f"Last Update: {time.strftime('%H:%M:%S')}")
    if st.button("Manual Force Scan"):
        with st.spinner("Analyzing Network..."):
            time.sleep(1.5)
            st.rerun()

# --- 4. DASHBOARD PAGE ---
if "Dashboard" in menu:
    st.title("🌐 Cyber Defense Real-time Dashboard")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Attacks Blocked", f"{np.random.randint(1400, 1600)}", "+14%")
    m2.metric("Network Health", "99.8%", "0.2%")
    m3.metric("AI Accuracy", "96.4%", "-0.1%")
    m4.metric("Active Sessions", f"{np.random.randint(20, 45)}", "4")

    st.markdown("---")

    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("📊 Live Traffic & AI Mitigation")
        chart_data = pd.DataFrame({'Intervals': list(range(21)), 'Threat Intensity': np.random.randint(10, 70, 21), 'AI Defense Power': np.random.randint(50, 100, 21)})
        fig = px.area(chart_data, x='Intervals', y=['Threat Intensity', 'AI Defense Power'], color_discrete_map={"Threat Intensity": "#FF4B4B", "AI Defense Power": "#00CC96"}, template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        st.subheader("🌍 Threat Origin Map")
        map_data = pd.DataFrame({'Country': ['USA', 'China', 'Russia', 'India', 'Germany'], 'Threats': np.random.randint(10, 100, 5)})
        fig_pie = px.pie(map_data, values='Threats', names='Country', hole=0.4, color_discrete_sequence=px.colors.sequential.Reds_r)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    st.subheader("🎯 Live Global Threat Intelligence Feed")
    live_df = get_live_threats()
    
    def highlight_risk(val):
        color = '#931a1a' if val > 85 else '#161b22'
        return f'background-color: {color}'

    st.table(live_df.style.applymap(highlight_risk, subset=['Risk Score']))
    st.warning(f"🤖 **AI Notice:** Blocked a {live_df.iloc[0]['Method']} attempt from {live_df.iloc[0]['Attacker IP']} just now.")

    # --- புதிய டவுன்லோட் பட்டன் ---
    st.markdown("---")
    st.subheader("📥 Export Security Intelligence")
    csv_data = live_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download CSV Report", data=csv_data, file_name=f'sentinel_report_{time.strftime("%H%M")}.csv', mime='text/csv')

# பிற பக்கங்கள் (AI Analysis, Logs, Settings) அப்படியே இருக்கும்...
elif "AI Threat Analysis" in menu:
    st.title("🧠 AI Anomaly Detection")
    uploaded_file = st.file_uploader("Upload Log File")
    if uploaded_file: st.success("Analysis Complete!")
elif "System Logs" in menu:
    st.title("📝 System Events")
    st.dataframe(pd.DataFrame([{"Time": time.strftime("%H:%M:%S"), "IP": fake.ipv4(), "Event": "Blocked"} for _ in range(10)]), use_container_width=True)
else:
    st.title("⚙️ Settings")
    st.toggle("Autonomous Defense", value=True)

st.markdown("---")
with st.expander("💬 Sentinel Assistant"):
    if st.text_input("Ask Me:"): st.write("Sentinel AI: System Secure.")
