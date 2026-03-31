import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time
from datetime import datetime

# 1. Page Config
st.set_page_config(page_title="Sentinel Pro v2.5", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Realistic Pro Look
st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    .stMetric { border-left: 5px solid #00ffcc; background-color: #161b22; }
    .status-box { padding: 10px; border-radius: 5px; border: 1px solid #30363d; margin-bottom: 10px; font-family: monospace; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIN LOGIC (அப்படியே இருக்கும்) ---
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'setup_done' not in st.session_state: st.session_state['setup_done'] = False

# --- 3. REALISTIC DATA GENERATOR ---
def get_threat_intel():
    # நிஜமான சைபர் செக்யூரிட்டி வார்த்தைகள்
    methods = ["SSH Brute Force", "SQLi Attempt", "Cross-Site Scripting (XSS)", "DDoS Flood", "Anomalous Packet Size", "Malicious File Upload"]
    data = []
    for _ in range(6):
        data.append({
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Target Port": np.random.choice([80, 443, 22, 8080, 3306]),
            "Attacker IP": fake.ipv4(),
            "Method": np.random.choice(methods),
            "Confidence": f"{np.random.randint(85, 100)}%",
            "Action": "AUTO_BLOCKED"
        })
    return pd.DataFrame(data)

# --- LOGIN SCREEN ---
if not st.session_state['logged_in']:
    if not st.session_state['setup_done']:
        st.title("🛡️ Sentinel AI - Initial Setup")
        u = st.text_input("Create Admin ID")
        p = st.text_input("Create Password", type="password")
        if st.button("Save Credentials"):
            st.session_state['saved_user'], st.session_state['saved_pass'] = u, p
            st.session_state['setup_done'] = True
            st.rerun()
    else:
        st.title("🔐 Secure Login")
        u_in = st.text_input("User ID")
        p_in = st.text_input("Password", type="password")
        if st.button("Unlock Dashboard"):
            if u_in == st.session_state['saved_user'] and p_in == st.session_state['saved_pass']:
                st.session_state['logged_in'] = True
                st.rerun()
            else: st.error("Access Denied")
else:
    # --- MAIN DASHBOARD ---
    with st.sidebar:
        st.title("🛡️ Sentinel Pro v2.5")
        st.write(f"Admin: **{st.session_state['saved_user']}**")
        st.markdown("---")
        st.write("System Health")
        st.progress(98)
        menu = st.radio("Intelligence Hub", ["Dashboard", "Threat Logs", "AI Chat"])
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    if menu == "Dashboard":
        st.title("🌐 Live Threat Intelligence Dashboard")
        
        # Metrics
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Packets Analyzed", "1.2M", "Live")
        c2.metric("Threats Blocked", "4,102", "+21")
        c3.metric("Uptime Score", "99.98%", "Stable")
        c4.metric("Security Level", "ALPHA", "High")

        st.markdown("---")
        
        # Threat Feed & Map
        col_map, col_intel = st.columns([2, 1])
        
        with col_map:
            st.subheader("🌍 Real-time Attack Vectors")
            map_df = pd.DataFrame({
                'lat': [20, 40, 60, -10, 35, 51], 'lon': [78, -100, 100, -50, 105, 10],
                'Intensity': np.random.randint(10, 100, 6)
            })
            fig = px.scatter_geo(map_df, lat='lat', lon='lon', size='Intensity', color='Intensity', projection="orthographic", template="plotly_dark", color_continuous_scale='Reds')
            st.plotly_chart(fig, use_container_width=True)

        with col_intel:
            st.subheader("📡 Live System Feed")
            for i in range(4):
                st.markdown(f"""
                <div class="status-box">
                [SYSTEM] {datetime.now().strftime('%H:%M:%S')} - Scanning Port {np.random.choice([80, 443])}...<br>
                [FIREWALL] Blocked IP {fake.ipv4()}<br>
                <span style="color:#00ffcc">[AI] No anomalies detected in current stream.</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("🎯 Active Threat Intelligence Feed")
        intel_df = get_threat_intel()
        st.dataframe(intel_df, use_container_width=True)
        
        # Download Report
        csv = intel_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Threat Intel Report", csv, "threat_intel.csv", "text/csv")
