import os

print("Fetching emails...")
os.system("python reads_email.py")

print("\nGenerating digest...")
os.system("python digest.py")

print("\nSending digest...")
os.system("python send_digest.py")

print("\nEmail Digest Bot completed successfully!")