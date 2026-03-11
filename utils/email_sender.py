import smtplib
from email.mime.text import MIMEText
from config import Config


def send_detection_email(user_email, result):

    sender = Config.MAIL_USERNAME
    password = Config.MAIL_PASSWORD
    receiver = Config.ADMIN_EMAIL

    subject = "Insect Damage Detection Alert"

    body = f"""
    A new detection has been performed.

    User: {user_email}
    Result: {result}

    Please check the admin dashboard for details.
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()