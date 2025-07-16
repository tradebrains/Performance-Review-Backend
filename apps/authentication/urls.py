from django.urls import path
from .views import RegisterView,LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework import routers
from django.conf.urls import include
router=routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    ]