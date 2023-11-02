from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProtocolViewSet, chat_with_gpt3, fetch_protocol_based_on_location

router = DefaultRouter()
router.register(r'protocols', ProtocolViewSet)  # Register ProtocolViewSet with the router

urlpatterns = [
    path('chat/', chat_with_gpt3, name='chat_with_gpt3'),
    path('fetch_protocol_based_on_location/', fetch_protocol_based_on_location, name='fetch_protocol_based_on_location'),
    path('', include(router.urls)),  # Include the router URLs
]