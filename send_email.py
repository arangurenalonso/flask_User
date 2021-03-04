import os
from dotenv import load_dotenv
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='aranguren.alonso@gmail.com',
    to_emails='aranguren.alonso@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
apiKey=os.getenv('SENDGRID_API_KEY')
print(apiKey)
response = sg.send(message)
print(response.status_code, response.body, response.headers)