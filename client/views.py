import requests
from django.conf import settings
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserCodeAPIView(APIView):
    serializer_class = type('CodeSerializer', (serializers.Serializer,), dict(access_token=serializers.UUIDField()))

    def post(self, *args, **kwargs):
        print("we are here")
        print(kwargs)
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data['access_token']
        print(access_token)
        client_secret, client_id = settings.PUSTAKA_OAUTH_SETTING['client_secret'], \
                                   settings.PUSTAKA_OAUTH_SETTING['client_id']
        headers = {
            "x-client-id": client_id,
            "x-client-secret": client_secret,
            "x-access-token": str(access_token)
        }
        response = requests.get(settings.PUSTAKA_OAUTH_SETTING['user_retrieve_url'], headers=headers)

        if response.status_code == 200:
            response = response.json()
            username = response.pop('username')
            user, _ = User.objects.update_or_create(username=username, defaults=response)
            print(user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "username": username,
                "token": token.key
            })
        return Response({
            "message": "something went wrong"
        })


