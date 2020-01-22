from rest_framework import serializers
from authentication.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegistrationSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = serializers.ChoiceField(
        choices=[('AP', 'APPLICANT'),
                 ('ST', 'STAFF'),
                 ('SP', 'SPONSOR'), ]
    )
    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )
    confirmed_password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name",
                  "password", "confirmed_password", "role"]

    def validate(self, data):
        """validate data before we save """
        confirmed_password = data.get("confirmed_password")

        try:
            validate_password(data["password"])

        except ValidationError as e:
            raise serializers.ValidationError({
                "password": str(e).replace(
                    "["", "").replace(""]", "")})

        if not self.do_passwords_match(data["password"], confirmed_password):
            raise serializers.ValidationError({
                "passwords": ("Passwords do not match")
            })

        return data

    def create(self, validated_data):
        """Create a user."""
        del validated_data["confirmed_password"]
        return User.objects.create_user(**validated_data)

    def do_passwords_match(self, password1, password2):
        """Check if passwords match."""
        return password1 == password2


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True,)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError({
                "invalid": "invalid email and password combination"
            })
        # if not user.is_verified:
        #     raise serializers.ValidationError({
        #         "user": "Your email is not verified,please vist your mail box"
        #     })
        user = {
            "email": user.email,
            "token": user.token
        }
        return user
