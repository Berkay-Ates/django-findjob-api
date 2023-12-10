"""
URL configuration for findJobApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    create_user,
    login_user,
    activate_user_account,
    create_user_post,
    get_user_posts,
    get_all_user_posts,
    create_company,
    create_company_post,
    get_company_posts,
    get_all_companies_posts,
    create_job,
    get_all_jobs,
    get_all_companies,
    get_all_users,
    get_company_jobs,
    create_job_application,
    get_all_job_applications,
    get_user_job_applications,
    get_company_job_applications,
    get_one_user_information,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("createUserPost/", create_user_post),
    path("loginUser/", login_user),
    path("createUser/", create_user),
    path("activateUserAccount/<str:mail>/", activate_user_account),
    path("getUserPosts/<str:userId>/", get_user_posts),
    path("getAllUserPosts/", get_all_user_posts),
    path("createCompany/", create_company),
    path("createCompanyPost/", create_company_post),
    path("getCompanyPosts/<str:companyId>/", get_company_posts),
    path("getAllCompaniesPost/", get_all_companies_posts),
    path("createJob/", create_job),
    path("getAllJobs/", get_all_jobs),
    path("getAllCompanies/", get_all_companies),
    path("getAllUsers/", get_all_users),
    path("getCompanyJobs/<str:companyId>/", get_company_jobs),
    path("createJobApplication/", create_job_application),
    path("getAllJobApplications/", get_all_job_applications),
    path("getUserJobApplications/<str:userId>/", get_user_job_applications),
    path("getCompanyJobApplications/<str:companyId>/", get_company_job_applications),
    path("getOneUserInformation/<str:mail>/", get_one_user_information),
]
