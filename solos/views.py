from django.shortcuts import render
from django.http import HttpResponse
from solos.models import *

# Create your views here.


def index(request):

    context = {'solo': Solo.objects.filter(
    instrument=request.GET.get('instrument', None)
    )}
    return render(request, 'solos/index.html',context)
