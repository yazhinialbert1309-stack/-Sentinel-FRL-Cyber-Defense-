import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sentinel-FRL", layout="wide")
st.title("🛡️ Sentinel-FRL: Cyber Defense Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Cloud Redirects", "142", "12%")
col2.metric("Integrity", "98.4%", "0.2%")
col3.metric("Stability", "Stable", None)

# Mock logs table
logs_df = pd.DataFrame({
    "Timestamp": ["09:05:12", "09:05:45", "09:06:10"],
    "Status": ["⚠️ ALERT", "🛡️ PATCHED", "✅ SECURE"],
    "Action": ["Inbound DDoS", "IP Blacklisted", "Normal Traffic"],
    "HashID": ["0x7f2a1...", "0xa31b4...", "0xb98c2..."]
})
st.dataframe(logs_df, use_container_width=True)

# 🔄 REFRESH BUTTON HERE 👇
if st.button("🔄 Refresh Logs"):
    st.rerun()

st.caption("🔍 Searching for adversarial patterns... 📡")
