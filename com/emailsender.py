import yagmail
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

receiver = 'kewakew217@peogi.com'
subject = 'Email Automation Python'
# contents = 'There She Goes Again'

message = MIMEMultipart()
message['From'] = os.getenv('sender')
message['To'] = receiver
message['Subject'] = subject

body = """
<h1>Hi There</h1>
<p>The She Goes Once Again</p>
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)
contents = message.as_string()

yag = yagmail.SMTP(user=os.getenv('sender'), password=os.getenv('passkey'))
yag.send(to=receiver, subject=subject, contents=contents)

print('mail sent successfully')




