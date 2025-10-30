"""Monitor a log file for failed login attempts and detect potential brute-force attacks.

Check for failed login attempts by a user.
Keep track of amount of failed attempts
Make alert if failed attempts meet threshold
Export alerts to a csv file"""

import csv
from datetime import datetime


def monitor_logs(log_file, watch_ip=None, threshold=3):
    failed_attempts = {}
    alerts = []

    with open(log_file, "r") as file:
        for line in file:
            if "Failed" in line:
                split_line = line.strip().split(" - ")
                timestamp = datetime.strptime(split_line[0], "%Y-%m-%d %H:%M:%S")
                user = split_line[1].split(": ")[1]
                ip = split_line[3].split(": ")[1]

                if watch_ip and ip != watch_ip:
                    continue

                key = (user, ip)
                if key not in failed_attempts:
                    failed_attempts[key] = []
                failed_attempts[key].append(timestamp)

                if len(failed_attempts[key]) >= threshold:
                    alert_message = f"{timestamp} - \033[31mALERT\033[0m: Possible brute-force attack on user {user} from IP {ip}!"
                    print(alert_message)
                    new_timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
                    alerts.append([new_timestamp, user, ip, "Brute-force attack detected"])

                    failed_attempts[key] = []

    if alerts:
        export_alerts(alerts)



def export_alerts(alerts):
    with open("security_alerts.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "User", "IP", "Alert Type"])
        writer.writerows(alerts)
    print("Alerts has been saved to CSV file 'security_alerts.csv'.")


# log_file = "logs.txt"
# monitor_logs(log_file)

print()




