"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(openapi.Info(
    title = "UDEMY clone",
    default_version="version 1.0",
    description="Hi, you are in swagger now.",
),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/accounts/', include('application.accounts.urls')),
    path('api/v1/profiles/', include('application.profiles.urls')),
    path('api/v1/courses/', include('application.course.urls')),
    path('api/v1/feedback/', include('application.feedback.urls')),
    path('api/v1/order/', include('application.order.urls')),
]
