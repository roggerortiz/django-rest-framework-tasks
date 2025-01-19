from django.urls import path
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("", RedirectView.as_view(url="swagger-ui")),
    path("file", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc-ui/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc-ui",
    ),
]
