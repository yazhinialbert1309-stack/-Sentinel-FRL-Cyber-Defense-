import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="Sentinel AI Pro", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    div[data-testid="stMetricValue"] > div { color: #00CC96; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIN & SETUP LOGIC ---
if 'setup_done' not in st.session_state:
    st.session_state['setup_done'] = False
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def login_system():
    if not st.session_state['setup_done']:
        st.title("🛡️ Sentinel AI - Initial Setup")
        st.subheader("Create your Admin Credentials")
        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password", type="password")
        confirm_pass = st.text_input("Confirm Password", type="password")
        if st.button("Save & Continue"):
            if new_user and new_pass == confirm_pass:
                st.session_state['saved_user'] = new_user
                st.session_state['saved_pass'] = new_pass
                st.session_state['setup_done'] = True
                st.rerun()
            else: st.error("Check passwords again!")
    else:
        st.title("🔐 Sentinel AI - Secure Login")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Unlock Dashboard"):
            if u == st.session_state['saved_user'] and p == st.session_state['saved_pass']:
                st.session_state['logged_in'] = True
                st.rerun()
            else: st.error("Access Denied!")

# --- 3. MAIN APP ---
if not st.session_state['logged_in']:
    login_system()
else:
    # SIDEBAR
    with st.sidebar:
        st.title("🛡️ Sentinel AI Pro")
        st.write(f"Logged in as: **{st.session_state['saved_user']}**")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()
        st.markdown("---")
        menu = st.radio("Navigation", ["🌐 Dashboard", "🤖 AI Security Assistant", "📝 Logs", "⚙️ Settings"])
        st.success("System: Active")

    # --- 4. DASHBOARD PAGE (With New Global Map) ---
    if menu == "🌐 Dashboard":
        st.title("🌐 Global Cyber Defense Dashboard")
        
        # மெட்ரிக்ஸ்
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Attacks Neutralized", "1,524", "+14%")
        m2.metric("System Integrity", "99.9%", "0.1%")
        m3.metric("AI Confidence", "97.2%", "1.2%")
        m4.metric("Live Threats", "0", "-100%")
        
        st.markdown("---")
        
        # --- NEW GLOBAL ATTACK MAP ---
        st.subheader("🌍 Real-time Global Threat Map")
        map_df = pd.DataFrame({
            'Country': ['USA', 'China', 'Russia', 'India', 'Germany', 'Brazil', 'Canada', 'Australia'],
            'Threat Count': np.random.randint(10, 100, 8),
            'lat': [37.09, 35.86, 61.52, 20.59, 51.16, -14.23, 56.13, -25.27],
            'lon': [-95.71, 104.19, 105.31, 78.96, 10.45, -51.92, -106.34, 133.77]
        })
        fig_map = px.scatter_geo(map_df, lat='lat', lon='lon', hover_name='Country', 
                                 size='Threat Count', color='Threat Count',
                                 projection="natural earth", template="plotly_dark",
                                 color_continuous_scale=px.colors.sequential.Reds)
        st.plotly_chart(fig_map, use_container_width=True)

        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("📊 Defense Analytics")
            df = pd.DataFrame({'Time': list(range(21)), 'Intensity': np.random.randint(20, 80, 21)})
            st.plotly_chart(px.line(df, x='Time', y='Intensity', template="plotly_dark"), use_container_width=True)
        with c2:
            st.subheader("📝 Recent Security Events")
            st.table(pd.DataFrame([{"Time": time.strftime("%H:%M:%S"), "IP": fake.ipv4(), "Action": "Blocked"} for _ in range(5)]))

    # --- 5. AI SECURITY ASSISTANT PAGE ---
    elif menu == "🤖 AI Security Assistant":
        st.title("🤖 Sentinel AI - Advanced Assistant")
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]): st.markdown(message["content"])

        if prompt := st.chat_input("Ask a security question..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                response = "Sentinel AI is analyzing your request... Based on our current network metrics, we suggest monitoring for any suspicious patterns related to your query."
                st.markdown(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})

    # --- இதர பக்கங்கள் ---
    elif menu == "📝 Logs":
        st.title("📝 System Event Logs")
        st.dataframe(pd.DataFrame([{"Timestamp": time.strftime("%H:%M:%S"), "Source": fake.ipv4(), "Event": "Network Scan Detected"} for _ in range(20)]), use_container_width=True)
    else:
        st.title("⚙️ Admin Settings")
        st.toggle("Autonomous AI Defense Mode", value=True)
        st.slider("AI Sensitivity Level", 0, 100, 85)
