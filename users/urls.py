from django.urls import path

from .views import GetUser, Signin, Signup, Social

urlpatterns = [
    path("signin/", Signin.as_view()),
    path("signup/", Signup.as_view()),
    path("social/", Social.as_view()),
    path("get_user/", GetUser.as_view()),
]
