from datetime import datetime
from http.cookiejar import month
from lib2to3.fixes.fix_input import context
from lib2to3.pgen2.tokenize import group

from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from sympy.logic.inference import valid
from sympy.plotting.textplot import is_valid

from .forms import ZapisForm, KlientsForm
from .models import Uslugi, Uslugi_groups, Sertifikate, Zapis, Klients
from django.contrib import messages
from .calendar_fill import fill_cal
from django.http import JsonResponse


def welcome(request):


    return render(request, 'main/welcome.html')

def home(request):











    context = {
        'uslugi': Uslugi.objects.order_by('id'),
        'groups': Uslugi_groups.objects.order_by('id'),
        'media': 'static/media',
        'sert': Sertifikate.objects.order_by('priority'),
        'form_zapis': ZapisForm,
        'form_klients': KlientsForm
               }


    return render(request, 'main/home.html', context=context)


def zapis(request):
    if request.method == 'POST':

        form_zapis = ZapisForm(request.POST)
        if form_zapis.is_valid():

            zapis = form_zapis.save(commit=False)
            zapis.save()
            klient = Klients(name= request.POST.get('client_name'), phone= request.POST.get('phone'))

            klient.save()

            return render(request, 'main/zapis-success.html')
        else:
            print(form_zapis.cleaned_data)
    else:
        form_zapis = ZapisForm()


    context = {
        'uslugi': Uslugi.objects.order_by('id'),
        'groups': Uslugi_groups.objects.order_by('id'),
        'media': 'static/media',
        'sert': Sertifikate.objects.order_by('priority'),
        'form_zapis': form_zapis,
        'form_klients': KlientsForm
               }

    return render(request, template_name='main/modal-zapis.html', context=context)




def calendar_view(request):
    print(request.GET)


    zapisi = Zapis.objects.all()

    context = {
        'fill_cal': fill_cal()['date_list'],
        'months': fill_cal()['month_list'],
        'years': fill_cal()['year_list'],
        'zapisi': zapisi,
        'current_year': fill_cal()['current_year']
    }

    if 'monthSwitch' in request.GET:
        context = {
            'fill_cal': fill_cal(month=int(request.GET["monthSwitch"]), year=int(request.GET["yearSwitch"]))['date_list'],
            'months': fill_cal(month=int(request.GET["monthSwitch"]))['month_list'],
            'years': fill_cal(year=int(request.GET["yearSwitch"]))['year_list'],
            'zapisi': zapisi,
            'current_year': fill_cal(year=int(request.GET["yearSwitch"]))['current_year'],
        }
    return render(request, 'main/calendar.html', context=context)




def calendar_gdut_view(request):
    zapisi = Zapis.objects.all()
    uslugi = Uslugi.objects.all()



    context = {
        'zapisi': zapisi,
        'uslugi': uslugi,
    }

    if 'editBtn' in request.POST:

        id_zapisi = request.POST.get('editBtn')

        zapis = Zapis.objects.get(id=id_zapisi)
        try:
            if request.POST.get('date') != '':
                zapis.date_proceduri = request.POST.get('date')
            if request.POST.get('time') != '':
                zapis.time_proceduri = request.POST.get('time')
            if request.POST.get('price') != '':
                zapis.price = request.POST.get('price')
            if request.POST.get('recomendacii') != '':
                zapis.descr = request.POST.get('recomendacii')
            if request.POST.get('usluga') != '':
                id_uslugi = str(request.POST.get('usluga')).split('-')[1]
                name_usluga = Uslugi.objects.get(id=id_uslugi)
                zapis.procedura_name = name_usluga
            zapis.zapis_status = '2'
            zapis.save()
            return redirect('/calendar/jdut-podtvergdeniy')
        except:
            return render(request, 'main/calendar-gdut.html', context=context)





    return render(request, 'main/calendar-gdut.html', context=context)





def CustomCal(request):

    print('ok')
    zapisi = Zapis.objects.all()
    context = {
        'fill_cal': fill_cal()['date_list'],
        'zapisi': zapisi,
    }

    return render(request, 'main/calendar.html', context=context)