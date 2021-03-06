"""meetup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from app import views
from django.conf.urls import url
from mpesa.urls import mpesa_urls


test_patterns = [
    url(r'^$', views.test, name='django_daraja_index'),
    url(r'^oauth/success', views.oauth_success, name='test_oauth_success'),
    url(r'^stk-push/success', views.stk_push_success,name='test_stk_push_success'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('api-token-auth/', obtain_auth_token),
    url(r'^test/tests/', include(test_patterns)),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('mpesa/', include(mpesa_urls)),
]
