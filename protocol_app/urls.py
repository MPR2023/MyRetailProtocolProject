from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'protocols', views.ProtocolViewSet)

urlpatterns = [
    path('chat/', views.chat_with_gpt3, name='chat_with_gpt3'),  # Keeping only this
    path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('fetch_protocol_based_on_location/', views.fetch_protocol_based_on_location, name='fetch_protocol_based_on_location'),
]