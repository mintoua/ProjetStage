from django.http import HttpResponse
from django.shortcuts import render
from mainapp.models import FilesAdmin
from django.conf import settings
import os
from django.http import Http404


def home_view(request):
    return render(request,'main/index.html')

def download_view(request):
    context = {'file':FilesAdmin.objects.all}
    return render(request, 'main/telecharger.html', context)

def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;file_name='+os.path.basename(file_path)
            return response

    raise Http404

def contact_view(request):
    return render(request, 'main/contact.html')
