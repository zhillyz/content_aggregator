import smtplib
import os
from email.message import EmailMessage

email_address = os.environ.get('EMAIL_ADD')
email_password = os.environ.get('EMAIL_PASS')

def sendEmail(subject,content):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = email_address
    msg.set_content(content)

    with smtplib.SMTP('smtp-mail.outlook.com', port=587) as smtp:
        smtp.ehlo('mylowercasehost')
        smtp.starttls()
        smtp.ehlo('mylowercasehost')
        smtp.login(email_address,email_password)
        smtp.send_message(msg)