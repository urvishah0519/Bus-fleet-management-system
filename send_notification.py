import smtplib
from email.mime.text import MIMEText

def send_email_notification(to_email, subject, body):
    sender_email = "urvishah0519@gmail.com"
    sender_password = "gtzcmujbpkbnguis"

    # Add live tracking link to the body of the email
    live_tracking_link = "https://app.fleetx.io/live/share/v2/eJwFwYkNACAIBLCJLkF%2BxlFkDWe3XUSm7xZxmA6i06GzBSXeyNlRGm185gPhDgrV?timezone=null" 
    body += f"\n\nYou can track your bus live here: {live_tracking_link}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        msg = MIMEText(body)
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {str(e)}")
