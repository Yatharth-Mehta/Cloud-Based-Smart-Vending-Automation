# 🛒 Cloud-Based Smart Vending Automation  

## 📌 Overview  
The **Cloud-Based Smart Vending Automation** system is an innovative **IoT solution** designed to enhance vending machine efficiency by leveraging:  
✅ **Sensor-based automation**  
✅ **Real-time cloud integration**  
✅ **Remote monitoring capabilities**  

This project employs **ultrasonic sensors, database logging, and network communication** to enable:  
🔹 **Smart stock monitoring**  
🔹 **Automated product dispensing**  
🔹 **Operational analytics**  

---

## ⚙️ Features  
- 🏪 **Automated Product Detection:** Uses an **ultrasonic sensor** to track product availability and customer interactions.  
- 📡 **Cloud-Based Data Logging:** Captures and stores **real-time transaction data** in a **SQLite database** for analytics and inventory tracking.  
- 🌍 **Remote Monitoring & Control:** Establishes a **TCP/IP server-client communication** between the vending machine and a remote database server.  
- 💡 **Dynamic Feedback System:** Activates an **LED indicator** based on product availability and transaction success.  
- 📏 **Threshold-Based Alerts:** Prevents errors by ensuring vending operations are executed only when predefined conditions are met.  

---

## 🛠️ Technical Implementation  
### **🔧 Hardware Components**  
- 🎯 **Ultrasonic Sensor (HC-SR04):** Measures the distance to detect stock levels.  
- 📟 **Raspberry Pi GPIO Interface:** Handles sensor input and LED output.  
- 💡 **LED Indicator:** Provides real-time feedback on vending operations.  

### **🖥️ Software Architecture**  
#### **Client-Side (Sensor-Client.py) [Raspberry Pi]**  
- 📏 **Measures distance** using the ultrasonic sensor.  
- 📡 **Sends real-time stock data** to the cloud server over a **TCP connection**.  
- 📩 **Receives feedback** from the server to determine LED status.  

#### **Server-Side (Sensor-Server.py) [Cloud Database]**  
- 🔗 **Manages incoming data** from multiple vending units.  
- 📊 **Stores transactions** in a **SQLite database**.  
- 🔄 **Sends success/failure responses** to the client based on stock levels.  

---

## 🚀 Future Enhancements  
📌 **Integration with IoT Cloud Platforms** (AWS IoT, Firebase) for real-time remote access.  
📌 **Automated Inventory Management System** to notify suppliers of stock depletion.  
📌 **Mobile App Integration** for customer purchases and real-time machine status monitoring.  
📌 **AI-Powered Demand Forecasting** to optimize product restocking.  

---

## 🎯 Why This Project?  
This **IoT-powered vending automation system** offers an **intelligent, scalable, and cost-efficient** solution to streamline vending machine operations.  

By demonstrating **sensor integration, cloud communication, and database management**, this project highlights expertise in:  
✔️ **Embedded Systems**  
✔️ **Networking**  
✔️ **IoT Automation**  
