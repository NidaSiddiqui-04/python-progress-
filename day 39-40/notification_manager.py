
import os
import smtplib

from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.
account_sid="AC261816a56dcff008b296f64e0db556dd"
auth_token=os.environ.get("AUTH_TOKEN")
print(auth_token)

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)
        self.username=os.environ.get("EMAIL")
        self.password=os.environ.get("EPASSWORD")
    def send_emails(self,email_list,message_body):
        with smtplib.SMTP("smtp.gmail.com",port=587) as mail:
            mail.starttls()
            mail.login(user=self.username,password=self.password)
            for emails in email_list:
                mail.sendmail(from_addr=self.username,to_addrs=emails,msg=message_body)
                print("sent")
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_body,
            to="whatsapp:+918109097063"
        )
        print(message.sid)