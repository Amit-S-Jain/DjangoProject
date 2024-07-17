from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app1.urls')),
    path('PGOwner/',include('PGOwner.URLs')),
    path('PGStaff/',include('PGStaff.URLs')),
    path('PGTenant/',include('PGTenant.URLs')),
]
