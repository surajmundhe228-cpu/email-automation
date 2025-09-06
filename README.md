# 📧 Email Automation with Python & Gmail API

This project demonstrates how to **send automated emails** using Python and the Gmail API.  
It supports **personalized messages, scheduling, and attachments**, making it useful for bulk emails, reminders, or productivity automation.

---

## 🚀 Features
- Send emails automatically with Gmail API  
- Schedule emails (daily, weekly, or custom time)  
- Support for multiple recipients via CSV file  
- Personalized subject and body for each recipient  
- Attach files (PDF, CSV, images, etc.)  
- Logs message IDs after sending  

---

## 📂 Project Structure

📁 Email-Automation/
├── email_automation.py # main script
├── requirements.txt # dependencies
├── contacts.csv # (sample contact list)
├── screenshots/ # execution screenshots
└── README.md # documentation


---

## 🛠️ Tools & Technologies
- **Python**  
- **Gmail API** (Google Cloud OAuth 2.0)  
- **schedule** (Python library for task scheduling)  

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/email-automation.git
cd email-automation

2. Install dependencies
pip install -r requirements.txt

3. Enable Gmail API

Go to Google Cloud Console

Create a project and enable Gmail API

Create OAuth Client ID (Desktop app) credentials

Download the credentials.json file and place it in this folder

4. Run the script
python email_automation.py

📊 Example Workflow

Start the script → it connects to Gmail API

Waits for scheduled time (schedule handles timing)

Automatically sends emails with personalized details

Terminal output:

Email automation started. Waiting for schedule...
✅ Email sent successfully! Message Id: XXXXXXXXX

🧑‍💻 Author

Suraj Mundhe

GitHub: @surajmundhe228-cpu
