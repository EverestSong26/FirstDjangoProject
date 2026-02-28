from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher

def index(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/index.html", {'content': teach})

    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> Opened on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    #return HttpResponse(html_content)

# Create your views here.
