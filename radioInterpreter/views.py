from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import tasks
from .models import Theme


def index(request):
    theme = Theme()
    all_themes = theme.get_all_themes_available()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        uploaded_content_file_str = tasks.read_log("." + uploaded_file_url)
        request.session['uploaded_content_file_str'] = uploaded_content_file_str
        request.session['all_themes'] = all_themes
        request.session['uploaded_file_url'] = uploaded_file_url
        request.session['filename'] = filename

        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url, 'all_themes': all_themes, 'filename': filename
        })

    return render(request, 'index.html')


def parse_log_theme(request):
    if request.method == 'POST':
        theme_selected = request.POST['theme_selected']
        all_themes = request.session['all_themes']
        uploaded_content_file_str = request.session['uploaded_content_file_str']
        filename = request.session['filename']
        uploaded_content_file = tasks.parse_log_with_key_words(uploaded_content_file_str.replace("\n", "<br />"),
                                                               theme_selected)
        uploaded_file_url = request.session['uploaded_file_url']

        return render(request, 'index.html', {'uploaded_file_url': uploaded_file_url,
                                              'uploaded_content_file': uploaded_content_file,
                                              'theme_selected': theme_selected,
                                              'all_themes': all_themes, 'filename': filename
        })


