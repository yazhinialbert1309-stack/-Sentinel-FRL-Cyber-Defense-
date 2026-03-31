import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time

# பக்கம் அமைப்பு (Page Config)
st.set_page_config(page_title="Sentinel AI - Pro", layout="wide")
fake = Faker()

# --- 1. SIDEBAR (மெனு) ---
st.sidebar.title("🛡️ Sentinel AI Pro")
menu = st.sidebar.radio("Menu", ["Dashboard", "AI Threat Analysis", "Live Logs", "Settings"])
st.sidebar.markdown("---")
st.sidebar.success("System Status: Operational")

if menu == "Dashboard":
    st.title("🌐 Cyber Defense Real-time Dashboard")
    
    # --- 2. ADVANCED METRICS (மேம்பட்ட அளவீடுகள்) ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Attacks Blocked", "1,284", "+12%")
    col2.metric("System Integrity", "99.2%", "+0.5%")
    col3.metric("AI Confidence", "94%", "-1%")
    col4.metric("Active Threats", "0", "-100%")

    # --- 3. DYNAMIC CHARTS (கிராஃப்கள்) ---
    st.markdown("### 📊 Attack Vectors vs AI Mitigation")
    chart_data = pd.DataFrame({
        'Time': list(range(25)),
        'Threat Level': np.random.randint(10, 80, 25),
        'AI Defense': np.random.randint(20, 100, 25)
    })
    fig = px.line(chart_data, x='Time', y=['Threat Level', 'AI Defense'], 
                  color_discrete_map={"Threat Level": "red", "AI Defense": "green"},
                  template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    # --- 4. AI PREDICTION & NOTIFICATIONS (அலர்ட் சிஸ்டம்) ---
    st.info("🤖 **AI Prediction:** Low risk of DDoS attack in the next 30 minutes.")
    
    if st.button("Manual System Scan"):
        with st.status("Scanning Network...", expanded=True) as status:
            st.write("Checking Open Ports...")
            time.sleep(1)
            st.write("Analyzing Traffic Patterns...")
            time.sleep(1)
            st.write("Verifying SSL Certificates...")
            status.update(label="Scan Complete! No threats found.", state="complete", expanded=False)
        st.toast("Scan Successful!", icon='✅')

elif menu == "AI Threat Analysis":
    st.title("🧠 AI Anomaly Detection")
    st.write("Upload your log file to detect hidden threats using Machine Learning.")
    uploaded_file = st.file_uploader("Choose a CSV log file")
    if uploaded_file:
        st.success("File uploaded! AI is analyzing patterns...")

elif menu == "Live Logs":
    st.title("📝 Live System Logs")
    log_data = []
    for _ in range(10):
        log_data.append({
            "Timestamp": time.strftime("%H:%M:%S"),
            "Event": fake.sentence(nb_words=4),
            "Level": np.random.choice(["INFO", "WARNING", "CRITICAL"]),
            "IP Address": fake.ipv4()
        })
    df_logs = pd.DataFrame(log_data)
    st.table(df_logs)

# --- CHATBOT (சின்ன சாட்போட்) ---
st.markdown("---")
with st.expander("💬 Sentinel AI Assistant"):
    user_input = st.text_input("Ask me anything about your security:")
    if user_input:
        st.write("Sentinel AI: I am analyzing your request regarding '" + user_input + "'. Currently, all systems are secure.")

