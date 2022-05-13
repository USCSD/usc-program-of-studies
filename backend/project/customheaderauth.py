from django.contrib.auth.middleware import RemoteUserMiddleware, RemoteUserBackend
import os

class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = os.environ["AUTH_HEADER"]

class CustomHeaderBackend(RemoteUserBackend):
    def configure_user(self, request, user):
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
