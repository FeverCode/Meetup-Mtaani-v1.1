from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

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
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

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

def deals(request):
    return render(request, 'viewDeals.html')



@login_required
def profile(request):
    return render(request, 'users/profile.html')