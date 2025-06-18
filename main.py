import time
import requests
from datetime import datetime

websites = [
    "https://gs-center.onrender.com",
    "https://khan-global-institute.onrender.com",
    "https://jeet-diku.onrender.com",
    "https://khan-sir-class.onrender.com",
    "https://studymate-app.onrender.com",
    "https://aman-2-lz4v.onrender.com",
    "https://cw-ppj7.onrender.com",
    "https://appx-api-sunny.onrender.com"
]

interval = 600

def ping_websites():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting ping cycle...")
    for site in websites:
        try:
            response = requests.get(site, timeout=10)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Pinged {site} - Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Failed to ping {site} - Error: {e}")

if __name__ == "__main__":
    while True:
        ping_websites()
        print(f"Waiting {interval//60} minutes before next cycle...\n")
        time.sleep(interval)
