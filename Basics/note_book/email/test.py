#import yagmail
#
#yag = yagmail.SMTP("", "")
#yag.send(
#    to="evikarnold@gmail.com",
#    subject="Test Email",
#    contents="This is a test email sent using yagmail with App Password!"
#)
#print("Email sent successfully!")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Your account and server details
email_sender = 'auroraevik00@gmail.com'
email_password = 'ixfp ygnr noea uwwp' # Use the App Password here!
email_receiver = 'evikarnold@gmail.com'

smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For starttls

# 2. Create the email
subject = 'Test Email from Python!'
body = """
Hello,

This is a test email sent using Python.
It's pretty cool, right?

Cheers,
The Python Script
"""

msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain')) # Attach the body as plain text

# 3. Convert the message to a string
text = msg.as_string()

# 4. Send the email
try:
    print("Connecting to server...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() # Upgrade the connection to secure TLS
    server.login(email_sender, email_password)
    print("Logged in...")
    
    server.sendmail(email_sender, email_receiver, text)
    print("Email has been sent successfully!")
    
except Exception as e:
    print(f"Something went wrong: {e}")
finally:
    server.quit()
