from django.urls import path

from . import views

app_name='ency'

urlpatterns = [
    path("", views.index, name="index"),
    path("Page/<str:title>/", views.singlePage, name="singlePage"),
    path('search/', views.search, name="search"),
    path('create/', views.createPage, name="createPage")
]
