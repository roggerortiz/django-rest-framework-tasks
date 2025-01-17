from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("signup/", views.SignUpView.as_view(), name="sigup"),
    # path("profile/", views.ProfileView.as_view(), name="profile"),
]
