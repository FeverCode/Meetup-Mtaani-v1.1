from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import RegisterView, CustomLoginView
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.conf.urls import url

urlpatterns = [
    path('',views.index ),
    path('aboutus/',views.about, name='about'),
    path('deals/',views.deals, name='deals'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)