from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from app.models import Deals, Profile, Reservation
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, ReservationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from django.views.generic.edit import CreateView

from django_daraja.mpesa import utils
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def dispatch(self, request, *args, **kwargs):
       # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
    return super(RegisterView, self).dispatch(request, *args, **kwargs)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
              
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} with')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})
    
   


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
    
    
    

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutUs.html')
@login_required
def deals(request):
    return render(request, 'viewDeals.html')


@login_required
def user_profile(request):
    profile = Profile.objects.all()
    reservations = Reservation.objects.all().order_by('id').reverse()
    return render(request, 'users/profile.html', {'profile': profile, 'reservations': reservations})

# class ProfileListView(ListView):
#     model = Reservation
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/edit-profile.html', {'user_form': user_form, 'profile_form': profile_form})


class DealsViewSet(viewsets.ModelViewSet):
    queryset = Deals.objects.all()
    serializer_class = DealsSerializer
    permission_classes = [IsAuthenticated]




cl = MpesaClient()
stk_push_callback_url = 'https://darajambili.herokuapp.com/express-payment'
b2c_callback_url = 'https://darajambili.herokuapp.com/b2c/result'


def test(request):

	return HttpResponse('Welcome to the home of daraja APIs')


def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)


def stk_push_success(request):
	phone_number = config('LNM_PHONE_NUMBER')
	amount = 1
	account_reference = config('TILL_NUMBER')
	transaction_desc = 'Test transaction'
	callback_url = stk_push_callback_url
	r = cl.stk_push(phone_number, amount, account_reference,
	                transaction_desc, callback_url)
	return JsonResponse(r.response_description, safe=False)

# @login_required
# def reservation(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST, instance=request.user)
    
#         if form.is_valid():
#             form.save(commit=False)
#             form.user = request.user.profile
#             form.save()
#             messages.success(request, f'Reservation Successfully Created')
#             # prevents post get redirect pattern. sends a get request instead of post request
#             return redirect('profile')
#     else:
#         form = ReservationForm()
#     context = {
#         'form': form,

#     }
#     return render(request, 'users/reservation.html', context)

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    
   
class UpdateReservationView(UpdateView):
      model = Reservation
      form_class = ReservationForm
      template_name = "users/reservation.html"
      form_class = ReservationForm
      
      
class CreateReservationtView(LoginRequiredMixin, CreateView):

    model = Reservation
    form_class = ReservationForm 
    template_name = 'users/reservation.html'
    success_url = reverse_lazy('profile')

    #   ↓        ↓ method of the CreatePostView

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #   ↓              ↓ method of the CreatePostView
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Create new post'
        return data
