from __future__ import print_function
import base64
import csv
import os.path
import time
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the token.json file
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, message_text, attachment=None):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Add email body
    msg = MIMEText(message_text, 'plain')
    message.attach(msg)

    # Add attachment if provided
    if attachment:
        with open(attachment, 'rb') as f:
            mime = MIMEBase('application', 'octet-stream')
            mime.set_payload(f.read())
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
        message.attach(mime)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_message(service, user_id, message):
    try:
        sent = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"✅ Email sent successfully! Message Id: {sent['id']}")
        return sent
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None

def send_bulk_emails():
    service = gmail_service()
    sender = "okeysurajj@gmail.com"  # Replace with your Gmail

    # Read contacts from CSV
    with open("contacts.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            recipient = row['email']
            subject = f"Hello {name}, here’s your report 📊"
            body = f"""
Hi {name},

This is an automated email with your personalized report.

Regards,  
Suraj Mundhe
"""
            message = create_message(sender, recipient, subject, body, attachment="Amazon_Sales_Dashboard.pdf")
            send_message(service, "me", message)

# Example: Schedule to run daily at 9 AM
schedule.every().day.at("11:27").do(send_bulk_emails)

print("🚀 Email automation started. Waiting for schedule...")

while True:
    schedule.run_pending()
    time.sleep(60)
