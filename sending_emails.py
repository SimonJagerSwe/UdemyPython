########## SENDING EMAILS WITH PYTHON ##########
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Simon Jäger'
email['to'] = 'simonjager@hotmail.com'
email['subject'] = 'You\'ve won a bajillion dollarz'

email.set_content('I am a Python n00b...')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('simonjagerswe@gmail.com', 'GreatestPasswordEv3r!')
    smtp.send_message(email)
    print('It worked!')