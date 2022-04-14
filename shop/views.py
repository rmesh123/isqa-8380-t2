from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

now = timezone.now()


def homepage(request):
    return render(request, 'homepage.html',
                  {'shop': homepage})


def product(request):
    return render(request, 'product.html',
                  {'shop': product})
