import smtplib
from email.message import EmailMessage
import pyttsx3

msg = EmailMessage()
numb = int(input("Enter the number of mails you want to send = "))
receivers = []
for i in range(numb):
    receiver = input(f"Enter Receiver {i+1} mail'id = ")
    receivers.append(receiver)
subject = input("Enter subject of the mail :  ")
message = input("Enter text/message of the mail :  ")
msg.set_content(message)
msg['Subject'] = subject
msg['From'] = "nimmaravikiran000@gmail.com"
msg['To'] = receivers

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("nimmaravikiran000@gmail.com", "kxmo qqle nymq stex")
server.send_message(msg)
print("Mail sent Successfully...")
voice = pyttsx3.init()
voice.say("Mail sent successfully")
voice.runAndWait()
server.quit()
