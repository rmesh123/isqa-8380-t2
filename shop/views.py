from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from .models import *
from .forms import *
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import CreateView, ListView
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View





now = timezone.now()


def homepage(request):
    package = Package.objects.filter(start_date__lte=timezone.now())
    return render(request, 'homepage.html',
                  {'packages': package})


def product(request):
    return render(request, 'product.html',
                  {'shop': product})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        return render(request, 'shop/templates/registration/password_reset_complete.html')
    else:
        return render(request, 'shop/templates/registration/password_reset_complete.html')




class PackageDetailView(DetailView):
    model = Package
    template_name = "product.html"


class PackageListView(ListView):
    model = Package
    template_name = "homepage.html"
