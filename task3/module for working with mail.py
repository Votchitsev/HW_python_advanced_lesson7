import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib


class Mail:

    def __init__(self):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = 'login@gmail.com'
        self.password = 'qwerty'
        self.subject = "subject"
        self.header = None

    def send_message(self, message, recipients):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    my_mail = Mail()
    my_message = 'message'
    email_addresses_to_send = ['vasya@email.com', 'petya@email.com']
    my_mail.send_message(my_message, email_addresses_to_send)
    my_mail.receive_message()
