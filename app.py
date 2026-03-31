import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time

# 1. பக்க வடிவமைப்பு (Page Configuration)
st.set_page_config(page_title="Sentinel AI Pro", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS for Cyberpunk Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    div[data-testid="stMetricValue"] > div { color: #00CC96; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PASSWORD SETUP & LOGIN LOGIC ---
if 'setup_done' not in st.session_state:
    st.session_state['setup_done'] = False
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login_system():
    # பாஸ்வேர்டு இன்னும் செட் செய்யப்படவில்லை என்றால்
    if not st.session_state['setup_done']:
        st.title("🛡️ Sentinel AI - Setup Your Security")
        st.subheader("Create your Admin Credentials")
        new_user = st.text_input("Create Username", placeholder="e.g., admin")
        new_pass = st.text_input("Create Password", type="password", placeholder="Choose a strong password")
        confirm_pass = st.text_input("Confirm Password", type="password")
        
        if st.button("Set Credentials"):
            if new_user and new_pass == confirm_pass:
                st.session_state['saved_user'] = new_user
                st.session_state['saved_pass'] = new_pass
                st.session_state['setup_done'] = True
                st.success("Credentials saved! Now please login.")
                st.rerun()
            else:
                st.error("Passwords do not match or fields are empty!")
                
    # பாஸ்வேர்டு செட் செய்த பிறகு லாகின் ஸ்கிரீன்
    else:
        st.title("🔐 Sentinel AI - Secure Login")
        user_input = st.text_input("Username")
        pass_input = st.text_input("Password", type="password")
        
        if st.button("Access Dashboard"):
            if user_input == st.session_state['saved_user'] and pass_input == st.session_state['saved_pass']:
                st.session_state['logged_in'] = True
                st.success(f"Welcome back, {user_input}!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

# --- 3. MAIN APP (LOGIN வெற்றிகரமாக முடிந்தால் மட்டும் இது தெரியும்) ---
if not st.session_state['logged_in']:
    login_system()
else:
    # --- LIVE DATA GENERATOR ---
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

    # --- 4. SIDEBAR ---
    with st.sidebar:
        st.title("🛡️ Sentinel AI Pro")
        st.write(f"Logged in as: **{st.session_state['saved_user']}**")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()
        st.markdown("---")
        menu = st.radio("Navigation", ["🌐 Dashboard", "🧠 AI Threat Analysis", "📝 System Logs", "⚙️ Settings"])
        st.markdown("---")
        st.success("System Status: Active")

    # --- 5. DASHBOARD PAGE ---
    if "Dashboard" in menu:
        st.title("🌐 Cyber Defense Real-time Dashboard")
        
        # மெட்ரிக்ஸ்
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Attacks Blocked", f"{np.random.randint(1400, 1600)}", "+14%")
        m2.metric("Network Integrity", "99.8%", "0.1%")
        m3.metric("AI Confidence", "96.4%", "-0.1%")
        m4.metric("Active Sessions", f"{np.random.randint(10, 50)}", "2")

        st.markdown("---")

        col_left, col_right = st.columns(2)
        with col_left:
            st.subheader("📊 Traffic & Defense Power")
            chart_data = pd.DataFrame({'Intervals': list(range(21)), 'Threats': np.random.randint(10, 70, 21), 'Defense': np.random.randint(50, 100, 21)})
            fig = px.area(chart_data, x='Intervals', y=['Threats', 'Defense'], color_discrete_map={"Threats": "#FF4B4B", "Defense": "#00CC96"}, template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)

        with col_right:
            st.subheader("🌍 Top Threat Origins")
            map_data = pd.DataFrame({'Country': ['USA', 'China', 'Russia', 'India', 'Germany'], 'Value': np.random.randint(10, 100, 5)})
            fig_pie = px.pie(map_data, values='Value', names='Country', hole=0.4, color_discrete_sequence=px.colors.sequential.Reds_r)
            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")
        st.subheader("🎯 Live Threat Intelligence Feed")
        live_df = get_live_threats()
        
        def highlight_risk(val):
            return f'background-color: #931a1a' if val > 85 else ''

        st.table(live_df.style.applymap(highlight_risk, subset=['Risk Score']))

        # --- DOWNLOAD REPORT ---
        st.markdown("---")
        st.subheader("📥 Export Intelligence Report")
        csv = live_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV Report", csv, "sentinel_report.csv", "text/csv")

    # இதர பக்கங்கள் (AI Analysis, Logs, Settings)
    elif "AI Threat Analysis" in menu:
        st.title("🧠 AI Anomaly Analysis")
        st.file_uploader("Upload Log Data for AI Scan")
    elif "System Logs" in menu:
        st.title("📝 Detailed Event Logs")
        st.dataframe(pd.DataFrame([{"Time": time.strftime("%H:%M:%S"), "IP": fake.ipv4(), "Status": "Blocked"} for _ in range(15)]), use_container_width=True)
    else:
        st.title("⚙️ Security Configuration")
        st.toggle("Auto-Mitigation Mode", value=True)
        st.slider("AI Sensitivity", 0, 100, 80)

    st.markdown("---")
    with st.expander("💬 Sentinel Assistant"):
        st.write("Sentinel AI: Everything is under control, Admin.")
