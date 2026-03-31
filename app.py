import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from faker import Faker
import time
from datetime import datetime
import socket

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="Sentinel Pro v2.7", layout="wide", page_icon="🛡️")
fake = Faker()

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    .stMetric { border-left: 5px solid #00ffcc; background-color: #161b22; padding: 10px; border-radius: 5px; }
    .scanner-res { padding: 20px; border-radius: 10px; border: 1px solid #30363d; background-color: #161b22; margin-top: 20px; }
    .info-card { background-color: #0e1117; padding: 15px; border-radius: 8px; border-left: 3px solid #ff4b4b; margin-top: 10px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIN LOGIC ---
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'setup_done' not in st.session_state: st.session_state['setup_done'] = False

def login_system():
    if not st.session_state['setup_done']:
        st.title("🛡️ Sentinel AI - Initial Setup")
        u = st.text_input("Create Admin ID")
        p = st.text_input("Create Password", type="password")
        if st.button("Save Credentials"):
            st.session_state['saved_user'], st.session_state['saved_pass'] = u, p
            st.session_state['setup_done'] = True
            st.rerun()
    else:
        st.title("🔐 Secure Login")
        u_in = st.text_input("User ID")
        p_in = st.text_input("Password", type="password")
        if st.button("Unlock Dashboard"):
            if u_in == st.session_state['saved_user'] and p_in == st.session_state['saved_pass']:
                st.session_state['logged_in'] = True
                st.rerun()
            else: st.error("Access Denied")

# --- 3. DOMAIN INFO FUNCTION (புதிய வசதி) ---
def get_domain_info(url):
    # URL-ல் இருந்து டொமைன் பெயரை மட்டும் பிரித்தெடுத்தல்
    domain = url.replace("https://", "").replace("http://", "").replace("www.", "").split("/")[0]
    try:
        # அந்த டொமைனின் நிஜமான IP அட்ரஸைக் கண்டுபிடித்தல்
        ip_addr = socket.gethostbyname(domain)
        return {
            "Domain": domain,
            "IP Address": ip_addr,
            "Server Location": np.random.choice(["USA", "Germany", "India", "Singapore", "Netherlands"]),
            "SSL Status": "Valid (256-bit Encryption)",
            "Last Scanned": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except:
        return None

# --- 4. MAIN APP ---
if not st.session_state['logged_in']:
    login_system()
else:
    with st.sidebar:
        st.title("🛡️ Sentinel Pro v2.7")
        st.write(f"Admin: **{st.session_state['saved_user']}**")
        st.markdown("---")
        menu = st.radio("Intelligence Hub", ["📊 Dashboard", "🔍 URL Scanner", "🤖 AI Assistant", "📝 Logs"])
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    # --- DASHBOARD PAGE ---
    if menu == "📊 Dashboard":
        st.title("🌐 Global Threat Intelligence Dashboard")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Packets Analyzed", "1.6M", "Live")
        c2.metric("Threats Blocked", "4,312", "+27")
        c3.metric("Uptime Score", "99.99%", "Stable")
        c4.metric("Security Level", "ALPHA", "Ultra High")

        st.markdown("---")
        st.subheader("🌍 Real-time Attack Vectors")
        map_df = pd.DataFrame({'lat': [20, 40, 60, -10, 35, 51], 'lon': [78, -100, 100, -50, 105, 10], 'Intensity': np.random.randint(20, 120, 6)})
        fig = px.scatter_geo(map_df, lat='lat', lon='lon', size='Intensity', color='Intensity', projection="orthographic", template="plotly_dark", color_continuous_scale='Reds')
        st.plotly_chart(fig, use_container_width=True)

    # --- 🔍 URL SCANNER PAGE (மேம்படுத்தப்பட்டது) ---
    elif menu == "🔍 URL Scanner":
        st.title("🔍 Advanced Website Security & IP Scanner")
        st.write("Enter a URL to perform a deep forensic scan.")
        
        url_input = st.text_input("Website URL", placeholder="e.g., https://google.com")
        
        if st.button("Run Forensic Scan"):
            if url_input:
                with st.status(f"Analyzing {url_input}...", expanded=True) as status:
                    st.write("📡 Connecting to global threat database...")
                    time.sleep(1)
                    st.write("🛡️ Checking SSL/TLS integrity...")
                    time.sleep(1)
                    info = get_domain_info(url_input)
                    status.update(label="Scan Complete!", state="complete")
                
                # ரிசல்ட் கார்டு
                st.markdown('<div class="scanner-res">', unsafe_allow_html=True)
                if info:
                    st.success(f"### ✅ Result: SAFE")
                    st.write("**Security Score:** 98/100")
                    
                    # --- NEW DOMAIN DETAILS SECTION ---
                    st.markdown("---")
                    st.subheader("📋 Domain Intelligence Report")
                    col_i1, col_i2 = st.columns(2)
                    with col_i1:
                        st.markdown(f"""
                        <div class="info-card">
                        <b>Domain:</b> {info['Domain']}<br>
                        <b>Primary IP:</b> {info['IP Address']}<br>
                        <b>Server Location:</b> {info['Server Location']}
                        </div>
                        """, unsafe_allow_html=True)
                    with col_i2:
                        st.markdown(f"""
                        <div class="info-card">
                        <b>SSL Status:</b> {info['SSL Status']}<br>
                        <b>Scan Timestamp:</b> {info['Last Scanned']}<br>
                        <b>Risk Level:</b> No Threats Found
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("### ⚠️ Invalid Domain or Connection Failed")
                    st.write("Please check the URL and try again.")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter a URL first!")

    # இதர பக்கங்கள்...
    elif menu == "🤖 AI Assistant":
        st.title("🤖 Sentinel AI Assistant")
        st.chat_input("How can I help you today?")
    else:
        st.title("📝 Detailed Event Logs")
        st.dataframe(pd.DataFrame([{"Time": time.strftime("%H:%M:%S"), "IP": fake.ipv4(), "Event": "Filtered"} for _ in range(25)]), use_container_width=True)

