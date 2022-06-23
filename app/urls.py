from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from django.urls import path, include

from app.models import Profile
from . import views
from .views import RegisterView, CustomLoginView, ReservationDeleteView, CreateReservationtView, UpdateReservationView
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
    path('profile/', views.user_profile, name='profile'),
    path('edit/profile/', views.edit_profile, name='edit-profile'),
    path('<int:pk>/delete', ReservationDeleteView.as_view(),name='delete-reservation'),
    path('reservation/', CreateReservationtView.as_view(), name='reservation'),
    path('reservation/<int:id>/',UpdateReservationView.as_view(), name='update-reservation')
    # path('reservation/', views.reservation, name='reservation'),
    # path('', ProfileListView.as_view(), name='article-list'),
    # path('daraja/stk-push/', views.stk_push_callback,name='mpesa_stk_push_callback'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)