from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/schema/", include("docs.urls")),
    path("api/v1/auth/", include("auth.urls")),
    path("api/v1/tasks/", include("tasks.urls")),
]
