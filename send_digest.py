from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send'
]

creds = Credentials.from_authorized_user_file(
    'token.json',
    SCOPES
)

service = build('gmail', 'v1', credentials=creds)

with open(
    'daily_digest.html',
    'r',
    encoding='utf-8'
) as file:
    digest_content = file.read()

message = MIMEText(digest_content,"html")

message['from'] = 'jahnavi4717@gmail.com'
message['to'] = 'jahnavir765@gmail.com'
message['subject'] = 'Daily Email Digest'

raw = base64.urlsafe_b64encode(
    message.as_bytes()
).decode()

service.users().messages().send(
    userId='me',
    body={'raw': raw}
).execute()

print("Digest email sent successfully!")