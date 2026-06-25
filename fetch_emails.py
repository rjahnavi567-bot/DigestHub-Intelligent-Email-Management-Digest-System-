from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = Credentials.from_authorized_user_file(
    'token.json',
    SCOPES
)

service = build('gmail', 'v1', credentials=creds)

results = service.users().messages().list(
    userId='me',
    labelIds=['UNREAD']
).execute()

messages = results.get('messages', [])

print("Unread emails:", len(messages))