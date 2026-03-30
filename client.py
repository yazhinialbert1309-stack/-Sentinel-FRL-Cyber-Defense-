import flwr as fl
import numpy as np
import pandas as pd
import hashlib
import random
from datetime import datetime
import os
import time

# --- 1. Blockchain Hashing Logic (Immutable Evidence) ---
def generate_block_hash(data, prev_hash="0"):
    block_content = f"{data}{prev_hash}".encode()
    return hashlib.sha256(block_content).hexdigest()

# --- 2. Advanced Secure Logging (Blockchain + Self-Healing Logs) ---
def log_to_blockchain_csv(status, action, reason):
    file_path = 'live_stats.csv'
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    prev_hash = "0"
    if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
        try:
            last_line = pd.read_csv(file_path).iloc[-1]
            prev_hash = last_line['HashID']
        except:
            prev_hash = "0"
    
    current_hash = generate_block_hash(f"{timestamp}{status}{action}", prev_hash)
    
    new_data = {
        'Timestamp': [timestamp],
        'Status': [status],
        'Action': [action],
        'Reason': [reason],
        'HashID': [current_hash[:10]]
    }
    
    df = pd.DataFrame(new_data)
    header_needed = not os.path.exists(file_path) or os.stat(file_path).st_size == 0
    df.to_csv(file_path, mode='a', index=False, header=header_needed)
    print(f"[BLOCKCHAIN] Evidence Secured! Hash: {current_hash[:10]}")

# --- 3. Hacker AI Simulation & Self-Healing Logic ---
def hacker_ai_move():
    # Simulation: Hacker pudhu pudhu vithama attack panna try pannuvaan
    moves = ["Port Scan", "SQL Injection", "DDoS Attempt", "Ransomware Script"]
    return random.choice(moves)

def trigger_self_healing(attack_type):
    # System thaanavae patch panni 'Heal' pannikira logic
    patches = {
        "Port Scan": "Firewall Rule Updated",
        "SQL Injection": "Input Validation Patched",
        "DDoS Attempt": "Rate Limiting Activated",
        "Ransomware Script": "File System Isolated"
    }
    return patches.get(attack_type, "General Security Patch Applied")

# --- 4. Sentinel-FRL Agent (The Guardian) ---
class SentinelAgent(fl.client.NumPyClient):
    def get_parameters(self, config):
        return [np.array([1.0])]

    def fit(self, parameters, config):
        print("\n[AGENT] Scanning Infrastructure... Adversarial Activity Detected!")
        
        # Hacker Move Simulation
        hacker_move = hacker_ai_move()
        print(f"[THREAT] Hacker is trying: {hacker_move}")
        
        # Self-Healing Response
        patch_applied = trigger_self_healing(hacker_move)
        
        # Digital Twin Mimicry
        target_service = "Industrial Controller (PLC)"
        print(f"[MIMICRY] Mimicking {target_service} to trap attacker...")
        time.sleep(1.5)
        
        # Logging everything
        status = "ATTACK_BLOCKED"
        action = f"MIMIC & PATCH (Vulnerability: {hacker_move})"
        reason = f"Hacker used {hacker_move}. Auto-Response: {patch_applied}."
        
        log_to_blockchain_csv(status, action, reason)
        
        print(f"[SUCCESS] Threat Mitigated. System Self-Healed: {patch_applied}")
        return [np.array([1.1])], 1, {}

    def evaluate(self, parameters, config):
        return 0.5, 1, {"accuracy": 0.99}

# --- 5. Main Execution ---
if __name__ == "__main__":
    print("--- 🛡️ Sentinel-FRL: Advanced Autonomous Defense Agent Starting ---")
    try:
        fl.client.start_numpy_client(server_address="127.0.0.1:8081", client=SentinelAgent())
    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")
