from django.urls import path
from PGStaff import views

urlpatterns = [
    path('home/',views.home, name='home')
]