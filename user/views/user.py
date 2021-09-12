from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from PustakaIntake.viewsets import ListRetrieveUpdateModelMixin
from ..serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class UserViewSet(ListRetrieveUpdateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UserExistAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print("request data",  request.data)

        try:
            username = request.data['username']
            obj = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({
                "is_user": False
            })
        return Response({
            "is_user": True
        })
