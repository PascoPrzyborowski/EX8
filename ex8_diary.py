

# Task 1  Diary_Entry

import os                               #os system
import time
import datetime
import smtplib                          #opt and advanced
from email.mime.multipart import *      #opt and advanced
from email.mime.text      import *      #opt and advanced
from email.message        import *
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

print()
print(Fore.LIGHTCYAN_EX+"")
tprint("SECRET DIARY", font="random") #Logo
print(""+Style.RESET_ALL)
print()
time.sleep(1)

print("Loading ....")
time.sleep(1)
print()
new_entry = input("Enter your Diary Entry: >>> ")
print()
time.sleep(1)

#Some Deko stuff
log = "Log Entry: "
timestamp = "Your Local Time an Date is now:"
now = datetime.datetime.today().strftime( "%H:%M:%S %d-%m-%Y")
print(Fore.LIGHTGREEN_EX+"")
print(timestamp + " " + now)
print(""+Style.RESET_ALL)
time.sleep(1)
print()


with open("diary.txt", "a") as file:
     file.write(now + " " + log +" " + new_entry + "\n")

#reading part with Deko
print("Loading your Entries, please wait ...")
time.sleep(1)
print()
with open('diary.txt') as f:
    print(Fore.LIGHTRED_EX+"")
    entry = "You have the following Entries in your Diary: "
    print(entry + "\n")
    contents = f.read()
    print(contents)
    print(""+Style.RESET_ALL)


#if new_entry != " ":  # If not empty print in Diary 
#else:
   # print("Empty Sting. -Not Adding- !")


# print("Want to delete a line ?")
# choice = input("yes for yes or not for not:")

# if choice == "yes":
#     with open("diary.txt", "r") as f:
#         lines = f.readlines()
#         delitem = input("Put the word in to delete:")
#     with open("diary.txt", "w") as f:
#         for line in lines:
#             if line.strip(delitem + "\n"):
#                 f.write(line)






