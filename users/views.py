from django.core.cache import cache
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from protocol_app.serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.core.exceptions import ValidationError  # Import ValidationError
from django.core.validators import validate_email


def obtain_jwt_token(request):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    if not callable(jwt_payload_handler) or not callable(jwt_encode_handler):
        return Response({'error': 'Handler functions are not set or not callable'})

    try:
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username is None or password is None:
            raise KeyError

        # Validate email
        if '@' in username:
            validate_email(username)
    except ValidationError:
        return Response({'error': 'Invalid email format'})
    except KeyError:
        return Response({'error': 'Username or password key is missing'})

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})
    else:
        return Response({'error': 'Authentication failed'})



def get_user_count():
    user_count = cache.get('user_count')

    if user_count is None:
        # If cache is empty, execute the query
        user_count = CustomUser.objects.count()
        # Cache the result for 15 minutes
        cache.set('user_count', user_count, 60 * 15)

    return user_count

# In your view
def my_view(request):
    user_count = get_user_count()

class CustomUserCreateAPIView(CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        try:
            email = request.data['email']
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email format'})
        except KeyError:
            return Response({'error': 'Email key is missing'})

        return super().create(request, *args, **kwargs)