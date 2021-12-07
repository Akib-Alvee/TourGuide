from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name="HomePage"),
    path("placeview/<int:myid>", views.placeview, name="Placeview"),
    path("destinations/<str:name>/", views.destination, name="Destination"),
    path('tourindex/', views.tourindex, name="Tourindex"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="ContactUs"),
   
]
