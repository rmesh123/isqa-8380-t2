from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect

now = timezone.now()


def homepage(request):
    package = Package.objects.filter(start_date__lte=timezone.now())
    return render(request, 'homepage.html',
                  {'packages': package})


def product(request):
    return render(request, 'product.html',
                  {'shop': product})


class PackageDetailView(DetailView):
    model = Package
    template_name = "product.html"


class PackageListView(ListView):
    model = Package
    template_name = "homepage.html"
