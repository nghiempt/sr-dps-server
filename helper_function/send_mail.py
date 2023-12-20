import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os

load_dotenv()

class SEND_MAIL:
    @staticmethod
    def send_sign_up_mail(receiver_email):
        sender_email = os.getenv("SENDER_MAIL_ADDRESS")
        subject = "[DOUBLE N] Invite Letter"
        body = """<html lang="en">
                        <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Invite letter</title>
                        </head>
                        <body style="font-family: 'Arial', sans-serif;">

                        <p style="line-height: 1.5; font-size: 14px; text-align: justify;">Hello</p>

                        <p style="line-height: 1.5; font-size: 14px; text-align: justify;">
                            We are thrilled to welcome you to our community! It's a pleasure to have you on board, and we're excited for you to explore all the features our platform has to offer.
                        </p>

                        <p style="line-height: 1.5; font-size: 14px; text-align: justify;">
                            Once again, welcome to our community! We're looking forward to seeing you actively participate and contribute.
                        </p>

                        <p style="line-height: 1.5; font-size: 14px;">Best regards,</p>
                        <p style="line-height: 1.5; font-size: 14px;">DOUBLE N</p>

                        </body>
                        </html>"""

        html_part = MIMEText(body, "html", "utf-8")

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(html_part)

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = os.getenv("SENDER_MAIL_ADDRESS")
        smtp_password = os.getenv("SENDER_MAIL_PASSWORD")

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()

            server.login(smtp_username, smtp_password)

            server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent successfully.")

