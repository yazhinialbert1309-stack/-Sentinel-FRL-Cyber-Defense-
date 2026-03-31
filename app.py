import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time
from datetime import datetime

# 1. பக்க வடிவமைப்பு (Page Config)
st.set_page_config(page_title="Sentinel AI Pro v2.0", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Neon Cyberpunk Look
st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    [data-testid="stMetricValue"] { color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #ff4b4b , #00ffcc); }
    .sidebar-text { font-size: 14px; color: #808080; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIN & SETUP LOGIC ---
if 'setup_done' not in st.session_state: st.session_state['setup_done'] = False
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'chat_history' not in st.session_state: st.session_state['chat_history'] = []

def login_system():
    if not st.session_state['setup_done']:
        st.title("🛡️ Sentinel AI - Initial Setup")
        u = st.text_input("Create Admin Username")
        p = st.text_input("Create Password", type="password")
        cp = st.text_input("Confirm Password", type="password")
        if st.button("Set Credentials"):
            if u and p == cp:
                st.session_state['saved_user'], st.session_state['saved_pass'] = u, p
                st.session_state['setup_done'] = True
                st.rerun()
    else:
        st.title("🔐 Sentinel AI - Secure Login")
        u_in = st.text_input("Username")
        p_in = st.text_input("Password", type="password")
        if st.button("Access Command Center"):
            if u_in == st.session_state['saved_user'] and p_in == st.session_state['saved_pass']:
                st.session_state['logged_in'] = True
                st.rerun()
            else: st.error("Access Denied!")

# --- 3. MAIN APP ---
if not st.session_state['logged_in']:
    login_system()
else:
    # --- SIDEBAR (Updated) ---
    with st.sidebar:
        st.title("🛡️ Sentinel Pro v2.0")
        st.markdown(f"**Admin:** {st.session_state['saved_user']}")
        st.markdown(f"📅 **Date:** {datetime.now().strftime('%d-%m-%Y')}")
        st.markdown(f"⏰ **Time:** {datetime.now().strftime('%H:%M:%S')}")
        
        st.markdown("---")
        # System Health Progress Bar
        st.write("System Integrity")
        st.progress(98)
        st.write("Firewall Strength")
        st.progress(85)
        
        st.markdown("---")
        menu = st.radio("Navigation", ["🌐 Global Dashboard", "🤖 AI Assistant", "📝 Live Logs", "⚙️ Admin Settings"])
        
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- 4. DASHBOARD PAGE ---
    if menu == "🌐 Global Dashboard":
        st.title("🌐 Global Cyber Defense Dashboard")
        
        # New Metrics Style
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Attacks Neutralized", "2,845", "+18%")
        m2.metric("Network Uptime", "99.99%", "0.01%")
        m3.metric("Security Score", "94/100", "Gold")
        m4.metric("Active Encryptions", "128-bit", "Secure")

        st.markdown("---")

        # --- UPDATED GLOBAL MAP ---
        st.subheader("🌍 Real-time Threat Trajectories")
        map_df = pd.DataFrame({
            'Country': ['USA', 'China', 'Russia', 'India', 'Germany', 'Brazil', 'Canada', 'Australia', 'Japan', 'France'],
            'Threat Count': np.random.randint(20, 150, 10),
            'lat': [37.09, 35.86, 61.52, 20.59, 51.16, -14.23, 56.13, -25.27, 36.20, 46.22],
            'lon': [-95.71, 104.19, 105.31, 78.96, 10.45, -51.92, -106.34, 133.77, 138.25, 2.21]
        })
        fig_map = px.scatter_geo(map_df, lat='lat', lon='lon', hover_name='Country', 
                                 size='Threat Count', color='Threat Count',
                                 projection="orthographic", # உலக உருண்டை (Globe) தோற்றம்
                                 template="plotly_dark",
                                 color_continuous_scale='Turbo') # இன்னும் வண்ணமயமாக
        st.plotly_chart(fig_map, use_container_width=True)

        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("📊 Neural Defense Analytics")
            chart_df = pd.DataFrame({'Time': list(range(21)), 'Threats': np.random.randint(10, 60, 21), 'Mitigation': np.random.randint(40, 100, 21)})
            fig_line = px.area(chart_df, x='Time', y=['Threats', 'Mitigation'], template="plotly_dark", color_discrete_map={"Threats": "#ff4b4b", "Mitigation": "#00ffcc"})
            st.plotly_chart(fig_line, use_container_width=True)
        with c2:
            st.subheader("📝 Immediate Response Logs")
            log_data = [{"Time": time.strftime("%H:%M:%S"), "Source": fake.ipv4(), "Action": "Auto-Blocked"} for _ in range(6)]
            st.table(pd.DataFrame(log_data))

    # --- 5. AI ASSISTANT ---
    elif menu == "🤖 AI Assistant":
        st.title("🤖 Sentinel AI Intelligence")
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
        if p := st.chat_input("Ask Sentinel..."):
            st.session_state.chat_history.append({"role": "user", "content": p})
            with st.chat_message("user"): st.markdown(p)
            with st.chat_message("assistant"):
                res = "Accessing Neural Database... No active breaches related to your query. System remains secure."
                st.markdown(res)
                st.session_state.chat_history.append({"role": "assistant", "content": res})

    # Other pages remain updated with same logic...
    elif menu == "📝 Live Logs":
        st.title("📝 Live System Telemetry")
        st.dataframe(pd.DataFrame([{"ID": i, "IP": fake.ipv4(), "Status": "Filtered"} for i in range(50)]), use_container_width=True)
    else:
        st.title("⚙️ Admin Settings")
        st.toggle("Deep Packet Inspection", value=True)
        st.slider("AI Mitigation Speed (ms)", 10, 500, 100)

