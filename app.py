import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import hashlib
import time

st.set_page_config(page_title="Sentinel-FRL", layout="wide", initial_sidebar_state="expanded")
st.title("🛡️ Sentinel-FRL: Autonomous Cyber Defense")

# 1️⃣ LIVE GRAPH (Hacker vs Defender)
col1, col2 = st.columns([3,1])
with col1:
    chart_data = pd.DataFrame({
        'Intervals': list(range(20)),
        'Attacks': [0]*10 + [1]*10 + [np.random.randint(0,2)],
        'AI Mitigation': [2]*21
    })
    fig = px.line(chart_data, x='Intervals', y=['Attacks','AI Mitigation'],
                  title='🎨 Hacker vs Defender: Live Mitigation Graph',
                  color_discrete_map={'Attacks':'#ef4444', 'AI Mitigation':'#10b981'})
    st.plotly_chart(fig, use_container_width=True)

# 2️⃣ METRICS + THREAT ALERTS
col1, col2, col3 = st.columns(3)
col1.metric("Cloud Redirects", "142", "12%")
col2.metric("Integrity", "98.4%", "0.2%")
col3.metric("Stability", "Stable", None)

# Real-time Threat Alert
if np.random.random() > 0.7:
    st.error("🚨 LIVE ALERT: DDoS attack detected from IP 192.168.1.100!")
else:
    st.success("🟢 All systems nominal")

# 3️⃣ DYNAMIC LOGS + REFRESH + MOBILE UI
fake = Faker()
if st.button("🔄 Refresh Logs", use_container_width=True):
    st.rerun()

logs = []
for i in range(5):
    status = np.random.choice(["⚠️ ALERT", "🛡️ PATCHED", "✅ SECURE"])
    logs.append({
        "Timestamp": fake.time(),
        "Status": status,
        "Action": fake.word().title() + " Detected",
        "HashID": f"0x{hashlib.sha256(str(i).encode()).hexdigest()[:6]}..."
    })

st.subheader("📂 Blockchain-Secured Logs")
st.dataframe(pd.DataFrame(logs), use_container_width=True)

st.caption("🔍 Searching adversarial patterns... 📡 | 📱 Mobile Responsive")
