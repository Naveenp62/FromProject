from django.urls import path
from app1 import views
urlpatterns=[
    path('form',views.func,name="formpage"),
    path('home',views.func1,name="homepage"),
    path('page',views.func2,name="page"),
    path('n',views.func3,name="greaterpage")
]