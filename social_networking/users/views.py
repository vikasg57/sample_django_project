from rest_framework import status
from base.response import APIResponse

from base.views import AbstractAPIView
from users.handlers.user_handler import UserHandler
from rest_framework.permissions import AllowAny


class AuthLogInView(AbstractAPIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = self.get_email(request.data.get("email"))
        password = request.data.get("password")
        data = UserHandler().get_user(email, password)
        return APIResponse(data=data, status=status.HTTP_200_OK)


class AuthSignUpView(AbstractAPIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        mobile = request.data.get("mobile")
        password = request.data.get("password")
        email = self.get_email(request.data.get("email"))
        data = UserHandler().crete_user(
            first_name, last_name, mobile, email, password)
        return APIResponse(data=data, status=status.HTTP_200_OK)
