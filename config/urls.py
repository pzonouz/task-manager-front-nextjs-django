from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("api/v1/auth/", include("users.urls")),
]
