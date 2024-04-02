import imaplib
import re
import pandas as pd
import yaml
import getpass
import email
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Define functions to connect to Gmail and retrieve emails
username = input("Enter your GMail username:")
password = input("Enter your password: ")

imap = imaplib.IMAP4_SSL('imap.gmail.com')
imap.login(username,password)
imap.select("Inbox")
status, items = imap.search(None, "ALL")
if status == 'OK':
    mail_id = items[0].split()
    mail_list = []
    for emailid in mail_id:
        status, data = imap.fetch(emailid, '(RFC822)')
        content = data[0][1]
        mail = email.message_from_bytes(content)
        sender = mail["From"]
        subject = mail["Subject"]
        print("From:", sender)
        print("Subject:", subject)
        if mail.is_multipart():
                for part in mail.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" not in content_disposition:
                        payload = part.get_payload(decode=True)
                        if payload:
                            body = payload.decode()
                            print("Body:", body)
                        else:
                            payload = mail.get_payload(decode=True)
                if payload:
                    body = payload.decode()
                    print("Body:", body)

# 关闭与 IMAP 服务器的连接
imap.logout()

    
    













