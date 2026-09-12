# 🇮🇳 Bharat WiFi Guard

Bharat WiFi Guard ek simple Python tool hai jo aas-paas ke Fake / Suspicious WiFi networks ko detect karne me help karta hai. Ye tool `nmcli` ka use karke WiFi scan karta hai aur open / bina security wale networks ko alert karta hai.

Made with ❤️ by [theamitkoyree](https://github.com/theamitkoyree-cmyk)

---

### ✨ Features
- Aas-paas ke saare WiFi networks ko scan karta hai
- Open / Free WiFi ko Suspicious ke roop me batata hai
- Signal strength aur Security dikhata hai
- Kali Linux / Ubuntu ke liye perfect

### ⚙️ Requirements
- Kali Linux / Ubuntu / Parrot OS
- Python 3
- NetworkManager (`nmcli`)

### 🚀 Installation & Usage

**1. Kali me Terminal kholo**

**2. Tool download karo:**
```bash
git clone https://github.com/theamitkoyree-cmyk/Bharat-Wifi-Guard.git

cd Bharat-Wifi-Guard
ls
python3 guard.py
nmcli dev wifi list
