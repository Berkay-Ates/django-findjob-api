from uuid import uuid4
import django
from django.db import models
from datetime import *


class User(models.Model):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    ERKEK = "Erkek"
    KADIN = "Kadin"
    DIGER = "DIGER"

    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
        (ERKEK, "Erkek"),
        (KADIN, "Kadin"),
        (DIGER, "Diger"),
    ]

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    mail = models.EmailField(blank=False, unique=True)
    person_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True, db_index=True
    )
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=False)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    user_password = models.CharField(max_length=255)
    profile_img_url = models.CharField(max_length=255)


class Company(models.Model):
    name = models.CharField(max_length=255)
    company_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True, db_index=True
    )
    created_date = models.DateTimeField(auto_now_add=True, blank=True)


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    application_count = models.IntegerField()
    salary = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    job_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True, db_index=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class JobApplication(models.Model):
    job_application_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True, db_index=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True, blank=True)


class CompanyPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    company_post_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True, db_index=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_post_date = models.DateTimeField(auto_now_add=True, blank=True)


class UserPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    user_post_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, unique=True, db_index=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_post_date = models.DateTimeField(auto_now_add=True, blank=True)
