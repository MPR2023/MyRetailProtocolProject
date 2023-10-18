from django.contrib.auth.models import User
from django.db import models
from django.conf import settings  # Import settings

class Protocol(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,  # Make it nullable
        on_delete=models.CASCADE,
        related_name='protocols_as_user'
    )
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,  # new
        blank=True,  # new
        on_delete=models.CASCADE,
        related_name='protocols_as_uploader'  # added related_name
    )

    ACCESS_LEVEL_CHOICES = [
        ('worker', 'worker'),
        ('manager', 'manager'),
        ('admin', 'admin'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='protocols/')
    last_updated = models.DateTimeField(auto_now=True)
    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES, default='worker')

    def __str__(self):
        return self.title
    
class ProtocolReview(models.Model):
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=3)  # Ratings from 1 to 5
    comments = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.protocol.title} - {self.rating}"