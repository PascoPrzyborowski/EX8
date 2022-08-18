

# Task 1  Diary_Entry

import os                               #os system
import time
import datetime
import smtplib                          #opt and advanced
from email.mime.multipart import *      #opt and advanced
from email.mime.text      import *      #opt and advanced
from email.message        import *
from xmlrpc.client import NOT_WELLFORMED_ERROR      #opt and advanced
from   colorama import *                #some color    
from   art      import *                #asci art

#init the colorama
init()


def gmail_send(subject, message, from_mail, to_mail, password):
    global link
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    msg            = EmailMessage()
    message        = f'{message}'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = from_mail
    msg['To']      = to_mail
    server.send_message(msg)


new_entry = input("Enter your Diary Entry: >>> ")
log = "Log Entry: "
now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")
print(now)

with open("copy.txt", "a") as file:
    file.write(now + " " + log +" " + new_entry + "\n")









