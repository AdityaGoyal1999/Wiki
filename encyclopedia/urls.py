from django.urls import path

from . import views

app_name='ency'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.singlePage, name="singlePage"),
    path('encyclopedia/search/', views.search, name="search"),
    path('encyclopedia/create/', views.createPage, name="createPage"),
    path('encyclopedia/create/save/', views.savePage, name="savePage"),
    path('encyclopedia/editPage/new/<str:title>/', views.editPage, name="editPage"),
    path('encyclopedia/editPage/save/', views.editPageSave, name="editPageSave"),
    path('encyclopedia/randomPage/', views.randomPage, name="randomPage")
]
