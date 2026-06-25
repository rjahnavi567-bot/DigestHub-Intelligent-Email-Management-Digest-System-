from datetime import datetime
import schedule
import time
import os

def run_bot():
    with open("logs.txt", "a") as log:
     log.write(
        f"{datetime.now()} - Bot Executed\n"
    )
    try:

        print("Running Email Digest Bot...")

        os.system("python reads_email.py")
        os.system("python digest.py")
        os.system("python send_digest.py")

        print("Digest sent successfully!")

    except Exception as e:

        with open("logs.txt", "a") as log:

            log.write(
                f"ERROR: {e}\n"
            )
schedule.every().day.at("08:00").do(run_bot)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)