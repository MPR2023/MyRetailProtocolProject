from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Protocol
from .serializers import ProtocolSerializer
from django_filters import rest_framework as filters
from django.db.models import Q
from silk.profiling.profiler import silk_profile
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from chatgpt_api import chat_with_gpt3_function  # Corrected the import to match your function name
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from users.models import CustomUser
from typing import Union
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
import logging
import os

# Initialize logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'template_name.html')

@silk_profile(name='My View Profile')
def my_view(request):
    return render(request, 'template_name.html')

@api_view(['GET', 'POST'])
def chat_with_gpt3(request):

    if request.method == 'POST':
        user_input = request.data.get("user_input", "")
        logger.debug(f"Received user input: {user_input}")
        try:
            gpt_response = chat_with_gpt3_function(request)  # Notice the name change
            if isinstance(gpt_response, JsonResponse):
                return gpt_response
            else:
                return Response({"gpt_response": gpt_response})
        except Exception as e:
            logger.error(f"An error occurred: {e}")  # Logging the exception
            return JsonResponse({"error": f"Something went wrong: {str(e)}"})

@api_view(['POST', 'GET'])
def unified_chat_endpoint(request):

    user_input = None
    if request.method == 'POST':
        user_input = request.data.get("user_input", "")
        logger.debug(f"Received POST data: {request.data}")
    elif request.method == 'GET':
        user_input = request.GET.get("query", "")
        logger.debug(f"Received GET query: {request.GET}")

    if not user_input:
        return JsonResponse({"error": "No user input provided"})

    try:
        # Pass only the user_input and api_key to chatgpt_api.chat_with_gpt3
        api_key = os.environ.get("GPT3_API_KEY")
        gpt_response = chat_with_gpt3(user_input, api_key)
        return JsonResponse({"response": gpt_response})
    except Exception as e:
        logger.error(f"An error occurred: {e}")  # Logging the exception
        return JsonResponse({"error": f"An error occurred: {e}"})

# Rest of your code for ProtocolViewSet etc. stays the same

class ProtocolViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Protocol.objects.all().order_by('-last_updated')
    serializer_class = ProtocolSerializer
    ordering_fields = ['title', 'last_updated']
    ordering = ['title']
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('title', 'access_level', 'uploader')

    def create_protocol(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Log the data type before saving
            logger.debug(f"Type of serializer.validated_data: {type(serializer.validated_data)}")
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user: Union[AbstractBaseUser, AnonymousUser] = self.request.user  # Type annotation

        if isinstance(user, CustomUser):
            role = user.role
        else:
            role = 'anonymous'

        cache_key = f'protocols_for_role_{role}'
        cached_queryset = cache.get(cache_key)

        if cached_queryset is not None:
            return cached_queryset

        if role == 'admin':
            logger.debug("Returning all protocols for admin")
            queryset = Protocol.objects.select_related('uploader', 'user').all()
        elif role == 'manager':
            logger.debug("Returning protocols for manager")
            queryset = Protocol.objects.select_related('uploader', 'user').filter(Q(access_level='manager') | Q(access_level='worker'))
        else:  # role is 'worker'
            logger.debug("Returning protocols for worker")
            queryset = Protocol.objects.select_related('uploader', 'user').filter(access_level='worker')

        # Cache the queryset for 15 minutes
        cache.set(cache_key, queryset, 60 * 15)

        if not queryset:
        # Handle edge case where no protocols are available for this role
            return []  # or some error response

        return queryset
        
    @silk_profile(name='List Protocols')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @silk_profile(name='Create Protocol')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)