from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main/home.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


@login_required
def affirmations(request):
    return render(request, 'main/affirmations.html')


@login_required
def tests(request):
    return render(request, 'main/tests.html')
