# ids.py
from scapy.all import sniff, IP, TCP
import time
from collections import defaultdict
import threading

# Shared data
alerts = {
    "total": 0,
    "syn_flood": 0,
    "port_scan": 0,
    "suspicious_ips": defaultdict(int)
}

last_refresh = time.time()

def process_packet(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        ip_src = packet[IP].src
        tcp_flags = packet[TCP].flags

        # SYN flood detection
        if tcp_flags == "S":
            alerts["total"] += 1
            alerts["syn_flood"] += 1
            alerts["suspicious_ips"][ip_src] += 1
            print(f"[ALERT] 🚨 SYN packet detected from {ip_src}")

        # Port scan detection
        elif tcp_flags == "SA":
            alerts["total"] += 1
            alerts["port_scan"] += 1
            alerts["suspicious_ips"][ip_src] += 1
            print(f"[ALERT] 🔎 Possible Port Scan from {ip_src}")

def start_sniffing():
    print("🚀 IDS Started... Monitoring traffic...")
    sniff(prn=process_packet, store=False)

# Run sniffing in background when imported
def run_ids():
    t = threading.Thread(target=start_sniffing, daemon=True)
    t.start()
