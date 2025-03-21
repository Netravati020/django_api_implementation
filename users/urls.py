from django.urls import path
from .views import RegisterAPI, VerifyOTPAPI, LoginAPI, UserDetailsAPI, LogoutAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("register/verify/", VerifyOTPAPI.as_view(), name="verify-otp"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("me/", UserDetailsAPI.as_view(), name="user-details"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
]
