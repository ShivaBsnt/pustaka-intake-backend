
from django.contrib import admin
from django.urls import path
from .views.user import UserViewSet
from .views.user import UserExistAPIView
from.views.register import UserRegisterView
from .views.login import CustomAuthToken
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', UserViewSet, basename='user')


urlpatterns = [
    path('check/', UserExistAPIView.as_view(), name="check_user"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', CustomAuthToken.as_view(), name="register"),



]+router.urls
