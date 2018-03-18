from django.shortcuts import render


def home(request):
    render(request, 'accounts/home.html')
