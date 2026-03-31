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
    .stChatFloatingInputContainer { background-color: #161b22; }
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
        col_s1, col_s2 = st.columns(2)
        with col_s1:
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

# --- AI CHATBOT LOGIC ---
def get_ai_response(user_query):
    query = user_query.lower()
    responses = {
        "hi": "Hello Admin! I am Sentinel AI. How can I assist you with security today?",
        "hello": "Hello Admin! I am Sentinel AI. How can I assist you with security today?",
        "ddos": "A DDoS (Distributed Denial of Service) attack attempts to overwhelm a server with traffic. Our Sentinel AI is currently monitoring traffic spikes to prevent this.",
        "sql injection": "SQL Injection is a vulnerability where attackers inject malicious SQL code. I recommend using prepared statements and parameterized queries.",
        "password": "Always use a combination of symbols, numbers, and uppercase letters. Change your admin password every 90 days.",
        "status": "All defense layers are active. Firewall is filtering 99.8% of malicious packets.",
        "phishing": "Phishing is a deceptive attempt to steal data. Never click on suspicious links in emails.",
        "malware": "Malware includes viruses, worms, and trojans. Our heuristic engine is scanning all file uploads."
    }
    # Default response for unknown queries
    return responses.get(query, "That's an interesting security concern. Based on our current neural network analysis, I suggest monitoring your network logs for any anomalies related to that.")

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

    # --- 4. DASHBOARD PAGE ---
    if menu == "🌐 Dashboard":
        st.title("🌐 Cyber Defense Dashboard")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Attacks Neutralized", "1,524", "+14%")
        m2.metric("System Integrity", "99.9%", "0.1%")
        m3.metric("AI Confidence", "97.2%", "1.2%")
        m4.metric("Live Threats", "0", "-100%")
        
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("📊 Defense Analytics")
            df = pd.DataFrame({'Time': list(range(21)), 'Intensity': np.random.randint(20, 80, 21)})
            st.plotly_chart(px.line(df, x='Time', y='Intensity', template="plotly_dark"), use_container_width=True)
        with c2:
            st.subheader("📝 Recent Security Events")
            st.table(pd.DataFrame([{"Time": time.strftime("%H:%M:%S"), "IP": fake.ipv4(), "Action": "Blocked"} for _ in range(5)]))

    # --- 5. ADVANCED AI SECURITY ASSISTANT (புதிய பக்கம்) ---
    elif menu == "🤖 AI Security Assistant":
        st.title("🤖 Sentinel AI - Advanced Assistant")
        st.write("Ask me about cyber threats, security best practices, or system status.")
        
        # Chat interface
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask a security question..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                response = get_ai_response(prompt)
                st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

    # --- இதர பக்கங்கள் ---
    elif menu == "📝 Logs":
        st.title("📝 System Event Logs")
        st.dataframe(pd.DataFrame([{"Timestamp": time.strftime("%H:%M:%S"), "Source": fake.ipv4(), "Event": "Login Access"} for _ in range(20)]), use_container_width=True)
    else:
        st.title("⚙️ Admin Settings")
        st.toggle("Autonomous AI Mode", value=True)
        st.slider("AI Sensitivity", 0, 100, 85)

