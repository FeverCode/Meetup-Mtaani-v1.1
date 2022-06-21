from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import RegisterView

urlpatterns = [
    path('',views.index ),
    path('aboutus/',views.about, name='about'),
    path('deals/',views.deals, name='deals'),
    path('register/', RegisterView.as_view(), name='users-register'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)