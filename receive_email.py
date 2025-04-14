import imaplib
import email
from plyer import notification

def receive_email(user_email, password):
    try:
        IMAPserver = "imap.gmail.com"
        mail = imaplib.IMAP4_SSL(IMAPserver)
        mail.login(user_email, password)
        mail.select("inbox")

        #Search for all emails in inbox
        result, data = mail.search(None, "ALL")
        if result == "OK" and data[0]:
            latestID = data[0].split()[-1]  #gets the latest email id
            result, data = mail.fetch(latestID, "(RFC822)")
            
            if result == "OK":
                emailB = data[0][1] # extract email data
                message = email.message_from_bytes(emailB) #parse email content
                sender_email = message["From"]
                subject = message["Subject"]
                body = ""

                #Extract the email body if it's in plain text format
                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()    
                mail.logout()
                
                #Send a notification for the new email
                notification.notify(
                    title=f"New Email from {sender_email}",
                    message=subject,
                    timeout=10
                )    
                return f"From: {sender_email}\nSubject: {subject}\n\n{body}"
        return "No emails found." #return message if no emails exist
    except Exception as e:
        return f"Error: {e}"  #return error message in case of an exception
  
