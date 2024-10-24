# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from . import views   # Import views from the account app
from django.conf import settings   # Application settings
from .views import document_report

# Define URL patterns
urlpatterns = [
    path('base/', views.base, name="base"),      # Home page
    path('login/', views.login_page, name='login_page'),    # Login page
    path('register/', views.register_page, name='register'),  # Registration page
    path('report/', document_report, name='document_report'),
]


