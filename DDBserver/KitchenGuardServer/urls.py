from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("index", views.index, name="index"),
    path("KitchGuardServer", views.index, name="index"),
    path("dbupdater", views.dbupdater, name="dbupdater")
]