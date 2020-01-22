import jwt

from django.conf import settings

from rest_framework import authentication, exceptions

from .models import User, BlackList

"lets configure JWT here"


class JWTAuthentication(authentication.BaseAuthentication):
    auth_header_prefix = 'Bearer'.lower()

    def authenticate(self, request):
        """
        we call this method each time an endpoint is accessed
        and it return None when the authentication credentials are not met
        """

        request.user = None

        # we need the auth_header, which should be a list containing two
        # elements: 1) the name of the authentication header ('Bearer' in our
        # case) and 2) the JWT token.

        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')

        token = auth_header[1].decode('utf-8')

        if prefix.lower() != self.auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        we will try authenticate the token and if successful return (user,
        token) otherwise we return an Authentication failed Error
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            print(payload)

        except jwt.ExpiredSignatureError:
            message = "your token has expired, kindly login again"
            raise exceptions.AuthenticationFailed(message)

        try:
            user = User.objects.get(pk=payload['id']
                                    )
        except User.DoesNotExist:
            message = "user matching this token was not found"
            raise exceptions.AuthenticationFailed(message)

        if not user.is_active:
            msg = 'Forbidden! This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        token = BlackList.objects.filter(token=token).first()

        if token:
            msg = 'Session Expired.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
