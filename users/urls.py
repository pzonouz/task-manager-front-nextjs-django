from django.urls import path

from .views import signin, signup

urlpatterns = [path("signin/", signin.as_view()), path("signup/", signup.as_view())]
