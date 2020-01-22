from django.urls import path, include
from authentication.views import RegistrationAPIView, LoginAPIView

app_name = "authentication"

urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),

]
