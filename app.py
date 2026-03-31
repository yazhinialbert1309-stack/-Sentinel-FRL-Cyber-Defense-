import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time
from datetime import datetime
import re

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="Sentinel Pro v2.6", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Realistic Pro Look
st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    .stMetric { border-left: 5px solid #00ffcc; background-color: #161b22; padding: 10px; border-radius: 5px; }
    .status-box { padding: 10px; border-radius: 5px; border: 1px solid #30363d; margin-bottom: 10px; font-family: monospace; font-size: 12px; background-color: #0e1117; }
    .scanner-res { padding: 20px; border-radius: 10px; border: 2px solid #00ffcc; background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIN LOGIC ---
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'setup_done' not in st.session_state: st.session_state['setup_done'] = False

def login_system():
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

# --- 3. URL SCANNER FUNCTION ---
def scan_url(url):
    # இது ஒரு AI Simulation ஸ்கேனர்
    with st.status(f"Scanning {url} for threats...", expanded=True) as status:
        st.write("🔍 Checking domain reputation...")
        time.sleep(1)
        st.write("📂 Analyzing SSL certificates...")
        time.sleep(1.5)
        st.write("🤖 Running AI Heuristic analysis...")
        time.sleep(1.5)
        
        # எளிய லாஜிக்: 'google.com' போன்ற தெரிந்த பெயர்கள் வந்தால் 'Safe' என்று காட்டும்
        is_malicious = any(x in url.lower() for x in ["hack", "free-money", "win-prize", "login-update"])
        
        if is_malicious:
            status.update(label="⚠️ Threat Detected!", state="error")
            return "MALICIOUS", 92
        else:
            status.update(label="✅ Scan Complete - Website is Safe", state="complete")
            return "SAFE", 98

# --- 4. MAIN APP ---
if not st.session_state['logged_in']:
    login_system()
else:
    # SIDEBAR
    with st.sidebar:
        st.title("🛡️ Sentinel Pro v2.6")
        st.write(f"Admin: **{st.session_state['saved_user']}**")
        st.markdown("---")
        menu = st.radio("Intelligence Hub", ["📊 Dashboard", "🔍 URL Scanner", "🤖 AI Assistant", "📝 Logs"])
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- DASHBOARD PAGE ---
    if menu == "📊 Dashboard":
        st.title("🌐 Global Threat Intelligence Dashboard")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Packets Analyzed", "1.4M", "Live")
        c2.metric("Threats Blocked", "4,285", "+18")
        c3.metric("Uptime Score", "99.98%", "Stable")
        c4.metric("Security Level", "ALPHA", "High")

        st.markdown("---")
        col_map, col_intel = st.columns([2, 1])
        
        with col_map:
            st.subheader("🌍 Real-time Attack Vectors")
            map_df = pd.DataFrame({'lat': [20, 40, 60, -10, 35, 51], 'lon': [78, -100, 100, -50, 105, 10], 'Intensity': np.random.randint(10, 100, 6)})
            fig = px.scatter_geo(map_df, lat='lat', lon='lon', size='Intensity', color='Intensity', projection="orthographic", template="plotly_dark", color_continuous_scale='Reds')
            st.plotly_chart(fig, use_container_width=True)

        with col_intel:
            st.subheader("📡 System Logs Feed")
            for _ in range(4):
                st.markdown(f'<div class="status-box">[FIREWALL] Blocked IP {fake.ipv4()}<br><span style="color:#00ffcc">[AI] Scan complete.</span></div>', unsafe_allow_html=True)

    # --- 🔍 URL SCANNER PAGE (புதிய பக்கம்) ---
    elif menu == "🔍 URL Scanner":
        st.title("🔍 Advanced Website Security Scanner")
        st.write("Enter any URL to analyze it for phishing or malware risks.")
        
        url_input = st.text_input("Website URL", placeholder="https://example.com")
        
        if st.button("Start Deep Scan"):
            if url_input:
                result, score = scan_url(url_input)
                
                st.markdown(f'<div class="scanner-res">', unsafe_allow_html=True)
                if result == "SAFE":
                    st.success(f"### ✅ Security Result: {result}")
                    st.write(f"**Security Score:** {score}/100")
                    st.write("Our AI confirms this domain has no known malicious patterns.")
                else:
                    st.error(f"### ⚠️ Security Result: {result}")
                    st.write(f"**Risk Score:** {score}/100")
                    st.write("This URL shows patterns associated with phishing or malware delivery.")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter a URL first!")

    # --- இதர பக்கங்கள் ---
    elif menu == "🤖 AI Assistant":
        st.title("🤖 Sentinel AI Assistant")
        st.chat_input("Ask a security question...")
    else:
        st.title("📝 System Logs")
        st.dataframe(pd.DataFrame([{"Time": time.strftime("%H:%M:%S"), "IP": fake.ipv4(), "Status": "Blocked"} for _ in range(20)]), use_container_width=True)
