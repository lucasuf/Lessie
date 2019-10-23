from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from . import tasks


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        uploaded_content_file_str = tasks.read_log("." + uploaded_file_url)

        uploaded_content_file = uploaded_content_file_str.replace("\n", "<br />")
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url, 'uploaded_content_file': uploaded_content_file
        })
    return render(request, 'index.html')

