from django.shortcuts import render

# Create your views here.

from core.erp.models import *


def myfirstview(request):
    data = {
        'name': 'William',
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)
