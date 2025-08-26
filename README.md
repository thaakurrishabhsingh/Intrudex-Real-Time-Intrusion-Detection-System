# 🚀 Intrudex - Real-Time Intrusion Detection System

Intrudex is a **Real-Time Intrusion Detection System (IDS)** built with **Python** and a **Flask-based dashboard**.  
It monitors network traffic, detects suspicious activities, and logs alerts in real time.  

---

## 🔥 Features
- ✅ Real-time packet sniffing and analysis  
- ✅ Detection of suspicious IPs and activities  
- ✅ Alerts logging system (`alerts.log`)  
- ✅ Flask-powered **Web Dashboard** for monitoring  
- ✅ Clean and simple **UI with HTML/CSS**  

---

## 📂 Project Structure
IDS/
│-- app.py # Flask server and dashboard
│-- ids.py # IDS logic for packet monitoring
│-- alerts.log # Log file for detected alerts
│-- static/style.css # Dashboard CSS styling
│-- templates/index.html # Web dashboard template

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/thaakurrishabhsingh/Intrudex-Real-Time-Intrusion-Detection-System.git
cd Intrudex-Real-Time-Intrusion-Detection-System
2️⃣ Install Dependencies
pip install flask

3️⃣ Run the Application
python app.py


Now, open your browser and go to:
👉 http://127.0.0.1:5000/
