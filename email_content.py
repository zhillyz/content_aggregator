import smtplib
import os
from email.message import EmailMessage

email_address = os.environ.get('EMAIL_ADD')
email_password = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Test email'
msg['From'] = email_address
msg['To'] = email_address
msg.set_content('this is email')

with smtplib.SMTP_SSL('smtp-mail.outlook.com', port=465) as smtp:
    smtp.login(email_address,email_password)
    smtp.send_message(msg)