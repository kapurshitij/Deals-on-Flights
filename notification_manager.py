import smtplib
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


class NotificationManager:

    def send_sms(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Hi\n\n{message.encode('utf-8')}")

        # Prints if successfully sent.
        print(message.sid)
