from django.contrib import admin
from django.urls import path
from canteenapp import views
urlpatterns = [
    path("",views.index),
    path('index', views.index),
path('services', views.services),
path('contact', views.contact),
path('about', views.about),
path('galary', views.galary),
path('database', views.database),
#path('loan_application', views.loanapplication),
#path("admin",views.admin)
]