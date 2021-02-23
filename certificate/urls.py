from django.urls import path
from .views import *

urlpatterns = [
    path('certificates', CertificateView.as_view()),
]