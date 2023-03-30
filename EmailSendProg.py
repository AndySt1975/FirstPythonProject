#If you have 2-Factor Authentication set up on your account, that may prevent you from logging in from an unknown device)
# you have to generate a app password in google to be able to send this now 
# *********
# You now have to go into the section of the Security called App Password. You just give your app a name and click on "generate". 
# You then replace the value for "password" with the auto generated one.
# **************************************************************
# Python email
# **************************************************************
import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")

# ***********************************************************