from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'string': 'Hello, World!'})


def get_index_data(request):
    return HttpResponse('Hello, World!')
