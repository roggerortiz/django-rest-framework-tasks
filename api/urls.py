from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/api/v1/tasks/")),
    path("admin/", admin.site.urls),
    path("api/v1/docs/", include("docs.urls")),
    path("api/v1/auth/", include("auth.urls")),
    path("api/v1/tasks/", include("tasks.urls")),
]
