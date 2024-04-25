from django.urls import path

from . import views

urlpatterns = [
    path("dbupdater", views.dbupdater, name="dbupdater"),
    path("allEvents", views.allEvents, name="allEvents"),
    path("someEvents", views.someEvents, name="someEvents"),
]