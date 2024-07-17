from django.urls import path
from PGTenant import views

urlpatterns = [
    path('home/',views.home)
]