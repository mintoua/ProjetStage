from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'main/index.html')

def download_view(request):
    return render(request, 'main/telecharger.html')

def contact_view(request):
    return render(request, 'main/contact.html')
