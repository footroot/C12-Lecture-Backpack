suspicious_ips = ["192.168.1.101", "192.168.0.102"]

def block_ips(ips):
    for ip in ips:
        print(f"Blocking IP: {ip}")

block_ips(suspicious_ips)