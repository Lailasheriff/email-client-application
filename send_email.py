import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_pass, recipient_email, subject, body):
    try:
        SMTPserver = "smtp.gmail.com"
        SMTPport = 587 #for TLS encryption

        print("connecting to SMTP server")
        server = smtplib.SMTP(SMTPserver, SMTPport) #connection with SMTP server
        server.starttls() # start TLS encryption for security
        print("connected successfully")

        print("logging in")
        server.login(sender_email, sender_pass)
        print("Logged in successfully")

        message = MIMEMultipart() #create email object
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain')) #attach email body as plain text

        print("Sending the email")
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit() # close connection with SMTP server
        print("Email sent succesfully!")

    except Exception as e:
        print(f"Error: {e}") # print error message if an exception occurs