import smtplib, ssl
import pandas as pd

port = 587  
smtp_server = "smtp.gmail.com"
sender_email = "pandatxyz@gmail.com"
receiver_email_list = []
password = "wudd kcew uivu zesh"
message = """\
Subject: Hi there

This message is sent from Satyam's Attendace system project for being absent ."""
server = smtplib.SMTP(smtp_server,port)
server.starttls()
server.login(sender_email,password)

def sendMail(receiver_mail):
    try:
        server.sendmail(sender_email,receiver_mail,"Hello dummy mail is sent to u..")
    except Exception as e:
        print("Something went wrong and that issue is ..,",e)
    server.close()

# for receiver_mail in receiver_email_list:
#     sendMail(receiver_mail)

# print("Mail sent successfully to all absent student")
