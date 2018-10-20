from django.contrib import admin
from django.urls import path
from apps.web.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
]