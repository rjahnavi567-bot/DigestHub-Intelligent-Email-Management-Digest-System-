from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    search = request.args.get("search", "")
    category = request.args.get("category", "")
    cursor.execute("""
SELECT id,sender,subject,date
FROM emails
WHERE sender LIKE ?
OR subject LIKE ?
ORDER BY date DESC
""", (
    f"%{search}%",
    f"%{search}%"
))

    emails = cursor.fetchall()
    if category:

     filtered = []

     for email in emails:

        sender = email[1]
        subject = email[2]

        text = (sender + " " + subject).lower()

        email_category = "Other"

        if "security" in text:
            email_category = "Security"

        elif "internship" in text:
            email_category = "Work"

        elif "kaggle" in text or "workshop" in text:
            email_category = "Learning"

        elif "google play" in text:
            email_category = "Promotions"

        if email_category == category:
            filtered.append(email)

     emails = filtered
    conn.close()

    total_emails = len(emails)

    work_count = 0
    learning_count = 0
    security_count = 0
    promotion_count = 0
    other_count = 0

    for email in emails:

     sender = email[1].lower()
     subject = email[2].lower()
     
     text = sender + " " + subject

     if "security" in text:
        security_count += 1
        

     elif "internship" in text:
        work_count += 1
    

     elif "kaggle" in text or "workshop" in text:
        learning_count += 1
    

     elif "google play" in text:
        promotion_count += 1
     

     else:
        other_count += 1
      
    
    return render_template(
    "index.html",
    emails=emails,
    total_emails=total_emails,
    work_count=work_count,
    learning_count=learning_count,
    security_count=security_count,
    promotion_count=promotion_count,
    other_count=other_count
)

@app.route("/email/<email_id>")
def email_details(email_id):

    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT sender, subject, body, date
    FROM emails
    WHERE id = ?
    """, (email_id,))

    email = cursor.fetchone()

    conn.close()

    return render_template(
        "email_details.html",
        email=email
    )

if __name__ == "__main__":
    app.run(debug=True)