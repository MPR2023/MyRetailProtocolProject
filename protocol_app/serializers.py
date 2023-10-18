from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Protocol
from .models import Protocol, ProtocolReview

class ProtocolSerializer(serializers.ModelSerializer):
    uploader_role = serializers.CharField(source='uploader.role', read_only=True)

    class Meta:
        model = Protocol
        fields = '__all__'

class ProtocolReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtocolReview
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email')

    def validate_title(self, value):
        if 'badword' in value:
            raise serializers.ValidationError("Title contains a prohibited word.")
        return value
