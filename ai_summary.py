from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(
    api_key=api_key
)

def summarize_email(email_body):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        You are an email assistant.

Summarize the email in 2 short bullet points.

Focus on:
- action items
- deadlines
- important information

Ignore greetings and signatures.

        Email:
        {email_body}
        """
    )

    return response.text