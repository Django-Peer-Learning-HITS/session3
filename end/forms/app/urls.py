from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path('task/', views.index, name="index"),
    path('task/add', views.add, name="add")
]
