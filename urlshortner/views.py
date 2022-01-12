from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import uuid
from .models import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = UrlModel(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = UrlModel.objects.get(uuid=pk)
    return redirect(url_details.link)