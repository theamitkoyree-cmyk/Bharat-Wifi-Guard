print("Bharat WiFi Guard Started")

import subprocess

def scan_networks():
    print("[*] WiFi Scanning... Ye aapke apne network ke liye hai")
    # Ye sirf list dikhayega
    try:
        result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True, shell=True)
        print(result.stdout)
    except Exception as e:
        print(e)

scan_networks()
print("Scan Complete - Jai Hind")