from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import check_password, make_password
from .models import Dsuser
from .forms import RegisterForm, LoginForm

# Create your views here.


def timeline(request):
    return render(request, 'timeline.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        new_dsuser = Dsuser(
            user_id=form.data.get('user_id'),
            email=form.data.get('email'),
            password=make_password(form.data.get('password'))
        )
        new_dsuser.save()

        return super().form_valid(form)

    def form_invalid(self, form):        
        return super().form_invalid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        print(form.pk)
        self.request.session['user'] = form.pk

        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del request.session['user']

    return redirect('/')