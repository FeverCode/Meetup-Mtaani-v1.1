from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from django.urls import path, include
from . import views
from .views import RegisterView, CustomLoginView, profile
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('deals', views.DealsViewSet,  basename="deals")

urlpatterns = [
    path('',views.index ),
    path('api/', include(router.urls)),
    path('aboutus/',views.about, name='about'),
    path('deals/',views.deals, name='deals'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', profile, name='profile'),
    path('edit/profile/', views.edit_profile, name='edit-profile'),
    path('reservation/', views.new_reservation, name='reservation'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)