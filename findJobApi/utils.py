from django.core.mail import send_mail

from datetime import *
from .models import Company

from django.db import connection


subject = "İş Bul İş Sistemi Mail Doğrulama"
message = "https://findjopapi.onrender.com/activateUserAccount/"
from_email = "ates80408@gmail.com"


def sendMail(target: list):
    send_mail(subject, message + target[0], from_email, target)


def getCompanyThroughName(companyName):
    result = Company.objects.get(name=companyName)
    return result
