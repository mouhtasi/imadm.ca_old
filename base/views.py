from django.shortcuts import render


def index(request):
    return render(request, 'base/index.html')


def contact(request):
    return render(request, 'base/contact.html')
