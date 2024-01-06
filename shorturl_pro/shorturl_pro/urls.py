# Imports
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    path("", include("urlshorter.urls")),
]
