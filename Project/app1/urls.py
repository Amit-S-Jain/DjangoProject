from django.urls import path
from . import views

urlpatterns = [
    path('home/<str:bandName>',views.home),
    path('httpRequestParam/',views.httpRequestParam)
]