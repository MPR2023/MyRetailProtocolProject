from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', views.CustomUserCreateAPIView.as_view(), name='account-create'),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
