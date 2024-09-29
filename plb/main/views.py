from lib2to3.fixes.fix_input import context
from lib2to3.pgen2.tokenize import group

from django.db.models import Model
from django.shortcuts import render
from sympy.logic.inference import valid
from sympy.plotting.textplot import is_valid

from .forms import ZapisForm, KlientsForm
from .models import Uslugi, Uslugi_groups, Sertifikate, Zapis, Klients


def welcome(request):
    print(request.path)

    return render(request, 'main/welcome.html')

def home(request):

    if request.method == 'POST':
        form_zapis = ZapisForm(request.POST)
        zapis = form_zapis.save(commit=False)
        zapis.save()
        klient = Klients(name= request.POST.get('client_name'), phone= request.POST.get('phone'))

        klient.save()







    context = {
        'uslugi': Uslugi.objects.order_by('id'),
        'groups': Uslugi_groups.objects.order_by('id'),
        'media': 'static/media',
        'sert': Sertifikate.objects.order_by('priority'),
        'form_zapis': ZapisForm,
        'form_klients': KlientsForm
               }


    return render(request, 'main/home.html', context=context)