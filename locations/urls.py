from django.urls import path

from . import views

urlpatterns = [
    path("", views.Locations.as_view(), name="index"),
]