from rest_framework import serializers
from .models import User, Company, Job, JobApplication, CompanyPost, UserPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
            "surname",
            "mail",
            "person_id",
            "created_date",
            "gender",
            "is_active",
            "user_password",
            "profile_img_url",
        ]


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "company_id",
            "created_date",
            "field",
            "company_img_url",
        ]


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "title",
            "description",
            "application_count",
            "salary",
            "created_date",
            "job_id",
            "company",
        ]


class JobApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            "job_application_id",
            "job",
            "user",
            "company",
            "application_date",
        ]


class CompanyPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = [
            "title",
            "description",
            "company_post_id",
            "company",
            "company_post_date",
        ]


class UserPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = [
            "title",
            "description",
            "user_post_id",
            "user",
            "user_post_date",
        ]
