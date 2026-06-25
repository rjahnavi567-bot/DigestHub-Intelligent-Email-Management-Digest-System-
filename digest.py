
import sqlite3
from datetime import datetime

def categorize_email(sender, subject):

    text = (sender + " " + subject).lower()

    if "security" in text:
        return "Security"

    elif "internship" in text:
        return "Work"

    elif "kaggle" in text or "workshop" in text:
        return "Learning"

    elif "google play" in text:
        return "Promotions"

    return "Other"

IGNORE_SUBJECTS = [
    "Security alert",
    "Your new privacy settings",
    "finish setting up your new Google Account"
]


conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("""
SELECT sender, subject, body
FROM emails
ORDER BY date DESC
LIMIT 10
""")

emails = cursor.fetchall()
print("Total emails fetched:", len(emails))
grouped_emails = {
    "Work": [],
    "Learning": [],
    "Security": [],
    "Promotions": [],
    "Other": []
}

total_emails = 0

today = datetime.now().strftime(
    "%d %B %Y"
)

with open("daily_digest.html", "w", encoding="utf-8") as file:

    file.write("""
<html>
<head>
<title>Daily Email Digest</title>
<style>
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}
.email {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 5px;
}
.category {
    color: blue;
    font-weight: bold;
}
</style>
</head>
<body>

""")
    
    file.write(f"""
<h1>Daily Email Digest</h1>

<p>
Generated on: {today}
</p>
""")

    

    for i, email in enumerate(emails, start=1):

        sender = email[0]
        subject = email[1]
        body = email[2][:3000]

        skip = False

        for item in IGNORE_SUBJECTS:
          if item.lower() in subject.lower():
            skip = True
            break

        if skip:
           
           continue
 
        category = categorize_email(
        sender,
        subject
    )
        

        summary = body[:200].replace("\n", " ")

        grouped_emails[category].append(
            (sender, subject, summary))
        
        total_emails += 1

    work_count = len(grouped_emails["Work"])
    learning_count = len(grouped_emails["Learning"])
    security_count = len(grouped_emails["Security"])
    promotions_count = len(grouped_emails["Promotions"])
    other_count = len(grouped_emails["Other"])

    file.write(f"""
<div class="email">

<h2>Digest Statistics</h2>

<p>Total Emails: {total_emails}</p>

<p>Work: {work_count}</p>

<p>Learning: {learning_count}</p>

<p>Security: {security_count}</p>

<p>Promotions: {promotions_count}</p>

<p>Other: {other_count}</p>

</div>
""")
   
    for category, emails_list in grouped_emails.items():

      if not emails_list:
        continue

      file.write(f"<h2>{category}</h2>")

      for sender, subject, summary in emails_list:

        file.write(f"""
        <div class="email">

        <h3>{subject}</h3>

        <p>
        <b>Sender:</b> {sender}
        </p>

        <p>
        <b>Summary:</b><br>
        {summary}
        </p>

        </div>
        """)    

    file.write("""
</body>
</html>
""")
print("Digest generated successfully!")