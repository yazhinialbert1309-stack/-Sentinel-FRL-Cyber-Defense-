import streamlit as st
import pandas as pd
import numpy as np
import time

# Page setup for Dark Theme look
st.set_page_config(page_title="Sentinel-FRL Dashboard", layout="wide")

# Custom CSS for Dark Cards (Image-la irukura maari style)
st.markdown("""
    <style>
    .metric-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E86C1;
        color: white;
    }
    .stMetric {
        background-color: #121212;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title
st.title("🛡️ Sentinel-FRL: Autonomous Self-Healing Dashboard")
st.markdown("##### Robust Federated Learning | Blockchain-Verified | Adaptive Deception")

# --- Top Metric Cards (Image-la irukura maari 4 columns) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Active Mimicry Agents", value="2", delta="↑ Collaborating")
with col2:
    st.metric(label="Total Honey-pot Redirects", value="0", delta="↑ 0")
with col3:
    st.metric(label="Global Model Integrity", value="SECURE", delta="⌛ Scanning...")
with col4:
    st.metric(label="Self-Healing Status", value="ACTIVE ✅", delta="System Patched")

st.divider()

# --- Live Battle Arena (Graph) ---
st.markdown("### ⚔️ Hacker vs Defender: Live Battle Arena")

# Real-time simulation graph
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Attack Surface', 'Defense Response']
)
st.area_chart(chart_data)

# Status message like the image
st.info("Searching for adversarial patterns in the network... 📡")

# --- Logs Table (Optional but professional) ---
st.markdown("### 📂 Security Activity Logs")
logs = pd.DataFrame({
    "Time": ["09:14:01", "09:14:30"],
    "Event": ["Node-1 Sync", "Pattern Detected"],
    "Status": ["SUCCESS", "MITIGATED"]
})
st.table(logs)
