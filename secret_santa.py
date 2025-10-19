from dotenv import load_dotenv
import os
import random
import smtplib
import ssl

load_dotenv()
email = os.getenv("email")

from email.message import EmailMessage

def send_email(sender, receiver, recipient):
    password = os.environ['password']

    body_msg = f"""\
Hi! Your secret santa is: {recipient}! 
Remember to spend 10-100 bucks on your gift, but don't stress about it being the perfect gift!
"""

    msg = EmailMessage()
    msg['Subject'] = "Your Secret Santa Present"
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body_msg)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)


names_list = ['Sheila', 'Sandra','Sandy']
names_and_emails = [
    ['Sandra', 'sandrafiona11@gmail.com'],
    ['Sandy', 'sf2410@srmist.edu.in'],
    ['Sheila', 'dgesf2951@gmail.com'],
]

if len(names_list) <= 1:
    print("Not enough people to start secret santa!")
    quit()

assignments = names_and_emails.copy()
random.shuffle(assignments)

sender = email
for i in range(len(assignments)):
    santa = assignments[i]
    recipient = assignments[(i + 1) % len(assignments)]  # wraps around at the end
    send_email(sender, santa[1], recipient[0])
