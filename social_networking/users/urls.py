from django.urls import path

from users.views import (
    AuthSignUpView,
    AuthLogInView
)

urlpatterns = [
    path("signup/", AuthSignUpView.as_view(), name="signup"),
    path("login/", AuthLogInView.as_view(), name="login"),
]
