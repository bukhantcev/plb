from lib2to3.fixes.fix_input import context
from lib2to3.pgen2.tokenize import group

from django.shortcuts import render
from .models import Uslugi, Uslugi_groups
# Create your views here.


def welcome(request):
    print(request.path)

    return render(request, 'main/welcome.html')

def home(request):
    print('')

    context = {
        'uslugi': Uslugi.objects.order_by('id'),
        'groups': Uslugi_groups.objects.order_by('id'),
        'media': 'static/media'
               }


    return render(request, 'main/home.html', context=context)