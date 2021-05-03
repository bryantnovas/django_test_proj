from django.shortcuts import render
from test_proj.models import User


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def listings(request):
    data = {
        "users": User.objects.all(),
    }
    return render(request, "listings.html", data)