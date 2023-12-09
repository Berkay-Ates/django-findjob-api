from django.core.mail import send_mail

subject = "İş Bul İş Sistemi Mail Doğrulama"
message = "http://127.0.0.1:8000/activateUserAccount/"
from_email = "ates80408@gmail.com"


def sendMail(target: list):
    send_mail(subject, message + target[0], from_email, target)
