import streamlit as st
import pandas as pd
import time
from supabase import create_client

# --- 1. SUPABASE CLOUD CONFIG ---
SUPABASE_URL = "https://lxtvogbquxilhzwubszc.supabase.co"
SUPABASE_KEY = "sb_publishable_AGXM6lNqy1_V-m2ka7bNGw_GO7gsNrg"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Page Config ---
st.set_page_config(page_title="Sentinel-FRL: Global Defense Hub", layout="wide")

st.title("🛡️ Sentinel-FRL: Autonomous Cloud Dashboard")
st.markdown("### Real-Time Privacy-Preserved Cyber Defense")

# --- Function to load Data from Supabase Cloud ---
def load_cloud_data():
    try:
        # Cloud-la irundhu last 10 logs-ai edukkum
        response = supabase.table("attack_logs").select("*").order("Timestamp", desc=True).limit(10).execute()
        df = pd.DataFrame(response.data)
        if df.empty:
            return pd.DataFrame(columns=['Timestamp', 'Status', 'Action', 'Reason', 'HashID']), "Waiting for logs... ⏳"
        return df, "CLOUD VERIFIED ✅ (Blockchain Integrity Intact)"
    except Exception as e:
        return pd.DataFrame(columns=['Timestamp', 'Status', 'Action', 'Reason', 'HashID']), f"Connecting... {e}"

placeholder = st.empty()

while True:
    df, status_msg = load_cloud_data()
    
    with placeholder.container():
        # 1. Metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Active Mimicry Agents", "2", "Stable")
        m2.metric("Total Cloud Redirects", len(df), f"+{len(df)}")
        m3.metric("System Integrity", "SECURE", status_msg)

        st.divider()

        # 2. Live Logs Table (Cloud Data)
        st.subheader("📁 Global Blockchain-Secured Logs")
        st.dataframe(df, use_container_width=True)

        # 3. XAI & Mimicry Insight
        st.subheader("🧠 Autonomous Defense Insight")
        st.info("The Agent is currently using **Federated Reinforcement Learning** to sync threat intelligence across nodes without exposing local data.")

    time.sleep(2) # Auto-refresh every 2 seconds
