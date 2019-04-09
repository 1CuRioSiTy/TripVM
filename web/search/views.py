
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import UserForm
from .models import Route
from django.views.generic import View


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'search/login.html')
    else:
        return render(request, 'search/index.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'search/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('search:index')

        return render(request, self.template_name, {'form': form})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'search/login.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'search/index.html', {'success_message': 'You successfully login'})
            else:
                return render(request, 'search/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'search/login.html', {'error_message': '您的用户名或密码错误！'})
    return render(request, 'search/login.html')


