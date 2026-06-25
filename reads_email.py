from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import sqlite3
import base64
from bs4 import BeautifulSoup

def get_email_body(payload):

    body = ""

    if 'parts' in payload:

        for part in payload['parts']:

            if part['mimeType'] == 'text/plain':

                data = part['body'].get('data')

                if data:

                    body = base64.urlsafe_b64decode(
                        data
                    ).decode('utf-8')

                    return body

    else:

        data = payload['body'].get('data')

        if data:

            body = base64.urlsafe_b64decode(
                data
            ).decode('utf-8')

    return body

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = Credentials.from_authorized_user_file(
    'token.json',
    SCOPES
)

service = build('gmail', 'v1', credentials=creds)
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()
results = service.users().messages().list(
    userId='me',
    labelIds=['UNREAD']
).execute()



messages = results.get('messages', [])

if not messages:
    print("No unread emails found.")
    conn.close()
    exit()

for msg in messages:
    message = service.users().messages().get(
        userId='me',
        id=msg['id']
    ).execute()
    body = get_email_body(message['payload'])
    
    headers = message['payload']['headers']

    sender = ""
    subject = ""
    date = ""

    for header in headers:
        if header['name'] == 'From':
            sender = header['value']
        elif header['name'] == 'Subject':
            subject = header['value']
        elif header['name'] == 'Date':
            date = header['value']

    cursor.execute("""
    INSERT OR REPLACE INTO emails
    VALUES (?, ?, ?, ?, ?)
    """, (
    msg['id'],
    sender,
    subject,
    body,
    date
    ))
conn.commit()
conn.close()

print("Emails saved successfully!")