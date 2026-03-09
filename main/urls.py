from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_resource/", views.add_resource, name="add_resource")
]
