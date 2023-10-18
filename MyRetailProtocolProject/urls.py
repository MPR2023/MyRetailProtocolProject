"""
URL configuration for MyRetailProtocolProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from protocol_app.views import my_view, home, chat_with_gpt3
from protocol_app import views

basic_patterns = [
    path('admin/', admin.site.urls),
    path('protocol_app/', include('protocol_app.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/chat/', views.chat_with_gpt3, name='chat_with_gpt3'),
    path('api/unified_chat/', views.unified_chat_endpoint, name='unified_chat_endpoint'),
    path('api/', include('protocol_app.urls')),
    path('api/users/', include('users.urls')),
    path('my_view/', my_view, name='my_view'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
        path('', home, name='home'),
    ] + basic_patterns
else:
    urlpatterns = basic_patterns
