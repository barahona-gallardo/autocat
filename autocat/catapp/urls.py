from django.urls import path

from . import views

app_name = 'autocat'
urlpatterns = [
    path("", views.home, name="home"),
]
