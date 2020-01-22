from rest_framework import generics, status
from authentication.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        response = {
            "data": {
                "user": dict(user_data),
                "message": "you have been successfully registered, check your mail to activate your account"
            }
        }
        return Response(response, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data

        response = {
            "data": {
                "user": dict(user),
                "message": "login was very successful",

            }
        }
        return Response(response, status=status.HTTP_200_OK)
