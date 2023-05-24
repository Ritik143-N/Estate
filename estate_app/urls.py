from django.contrib import admin
from django.urls import include, path,re_path
from estate_app import views

urlpatterns = [
    #patient URLS paths
    path('', views.Homepage.as_view()),
    path('about/', views.About.as_view()),
    path('service/', views.Service.as_view()),
    path('properties/', views.Properties.as_view()),
    path('gallery/', views.Gallery.as_view()),
    path('contact/', views.Contacts.as_view(),name='contact'),

    ]