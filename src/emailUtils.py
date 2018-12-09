"""
Email utilility classes.

@author: Javier Gracia Carpio (jagracar)
"""

import smtplib
from email.message import EmailMessage


class EmailSender:
    """A simple class that connects to a SMTP server to send emails.

    """

    def __init__(self, smtp_server, port=587):
        """Class constructor.

        Intializes the connection with the SMTP server.
        """
        self.server = smtplib.SMTP(host=smtp_server, port=port)

    def login(self, username, password):
        """Login with the provided username and password.

        """
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(username, password)
 
    def close(self):
        """Closes the server conection.

        """
        self.server.close()
    
    def send_email(self, from_address, to_address, subject, text):
        """Sends an email with the provided addresses and text.

        """
        # Create the email message
        message = EmailMessage()
        message["From"] = from_address
        message["To"] = to_address
        message["Subject"] = subject
        message.set_content(text)
        
        # Send the email
        self.server.send_message(message)
