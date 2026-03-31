import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Configuration
st.set_page_config(page_title="Sentinel-FRL: Autonomous Defense", layout="wide")

# Dashboard Title
st.title("🛡️ Sentinel-FRL: Autonomous Cloud Dashboard")
st.subheader("Real-Time Privacy-Preserved Cyber Defense (PhD Prototype)")

# --- Phase 1: Real-Time Metrics ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Active Mimicry Agents", value="2", delta="Stable", delta_color="normal")
with col2:
    st.metric(label="Total Cloud Redirects", value="142", delta="↑ 12%", delta_color="inverse")
with col3:
    st.metric(label="System Integrity", value="98.4%", delta="SECURE", delta_color="normal")

st.divider()

# --- Phase 2: Live Battle Arena (Graph) ---
st.markdown("### 📈 Hacker vs Defender: Live Mitigation Graph")
# Creating simulated attack vs defense data
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Inbound Attacks', 'AI Mitigation']
)
st.area_chart(chart_data)

# --- Phase 3: Blockchain-Secured Logs Table ---
st.markdown("### 📂 Global Blockchain-Secured Logs")

# Simulated Logs for Demo
logs_data = {
    "Timestamp": ["09:05:12", "09:05:45", "09:06:10", "09:06:55"],
    "Status": ["⚠️ ALERT", "🛡️ PATCHED", "✅ SECURE", "⚠️ ALERT"],
    "Action": ["Inbound DDoS", "IP 192.168.1.5 Blacklisted", "Normal Traffic", "Brute Force Detected"],
    "Reason": ["Traffic Spike", "Malicious Pattern", "User Auth", "Multiple Login Failure"],
    "HashID": ["0x7f2a1...", "0xa31b4...", "0xb98c2...", "0xd44e9..."]
}
df_logs = pd.DataFrame(logs_data)
st.table(df_logs)

# --- Phase 4: AI Defense Insight ---
with st.expander("🧠 View Autonomous Defense Insight"):
    st.write("""
    **Current Strategy:** Moving Target Defense (MTD)
    - AI Agent has identified a recurring DDoS pattern from Region-X.
    - Federated Global Model updated with new weights.
    - False-Positive rate reduced to 0.02%.
    """)

st.info("System is monitoring network traffic in Federated Nodes... 📡")
