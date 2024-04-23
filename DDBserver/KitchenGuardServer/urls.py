from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("index", views.index, name="index"),
    path("KitchGuardServer", views.index, name="index"),
    path("api/dbupdater", views.dbupdater, name="dbupdater"),
    path("api/allEvents", views.allEvents, name="allEvents"),
    path("api/someEvents", views.someEvents, name="someEvents"),
]