import smtplib
import os
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes


def sendEmail(subject,content,attach=False):
    email_address = os.environ.get('EMAIL_ADD')
    email_password = os.environ.get('EMAIL_PASS')
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = email_address
    if attach:
        msg.set_content('Please find requested below:')
        image_cid = make_msgid()
        msg.add_alternative("""\
        <html>
            <body>
                <p>Here is your requested content:<br>
                </p>
                <img src="cid:{image_cid}">
            </body>
        </html>
        """.format(image_cid=image_cid[1:-1]), subtype='html')
        
        with open(content, 'rb') as img:
            # know the Content-Type of the image
            maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
            # attach it
            msg.get_payload()[1].add_related(img.read(), 
                                            maintype=maintype, 
                                            subtype=subtype, 
                                            cid=image_cid)
 
    else:
        #if not image, hoping this fails and then we just add normal content
        msg.set_content(content)

    with smtplib.SMTP('smtp-mail.outlook.com', port=587) as smtp:
        smtp.ehlo('mylowercasehost')
        smtp.starttls()
        smtp.ehlo('mylowercasehost')
        smtp.login(email_address,email_password)
        smtp.send_message(msg)