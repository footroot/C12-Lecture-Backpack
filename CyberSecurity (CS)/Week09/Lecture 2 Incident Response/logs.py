logs = [
    "2024-11-26 10:15:00 - Login attempt failed for user admin",
    "2024-11-26 10:16:00 - Successful login for user alice",
    "2024-11-26 10:17:00 - Multiple failed logins for user root"
]

def detect_suspicious_logs(logs):
    failed_attempts = 0
    for log in logs:
        if ("login attempt failed" in log.lower() or 
            "multiple failed" in log.lower()):
            failed_attempts += 1

    if failed_attempts > 3:
        print(f"Suspicious activity detected: {log}")

detect_suspicious_logs(logs)
