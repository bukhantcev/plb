import os
from datetime import datetime

from django.shortcuts import render, redirect


from .forms import ZapisForm, KlientsForm
from .models import Uslugi, Uslugi_groups, Sertifikate, Zapis, Klients

from .calendar_fill import fill_cal

from telegram.telegram_base import sendMessage


def welcome(request):


    return render(request, 'main/welcome.html')

def home(request):
    # obj = Uslugi.objects.all()
    # for i in obj:
    #     os.mkdir(f'/Users/buha/Documents/Новая папка/{i.name}')
    #     my_file = open(f'/Users/buha/Documents/Новая папка/{i.name}/{i.name}.txt', "w+")
    #     my_file.write("")
    #     my_file.close()









    context = {
        'uslugi': Uslugi.objects.order_by('id'),
        'groups': Uslugi_groups.objects.order_by('id'),
        'media': 'static/media',
        'sert': Sertifikate.objects.order_by('priority'),
        'form_zapis': ZapisForm,
        'form_klients': KlientsForm
               }


    return render(request, 'main/home.html', context=context)

#----------------------------ZAPIS BEZ USLUGI
def zapis(request):
    if request.method == 'POST':

        form_zapis = ZapisForm(request.POST)
        if form_zapis.is_valid():

            zapis = form_zapis.save(commit=False)
            zapis.save()
            klient = Klients(name= request.POST.get('client_name'), phone= request.POST.get('phone'))

            klient.save()
            try:
                sendMessage()
            except:
                print('Не удалось отправить сообщение')
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
#----------------------------ZAPIS S USLUGOI
def zapis_usluga(request):
    if 'nameUslugi' in request.GET:
        nameUslugi = request.GET.get('nameUslugi')
    if request.method == 'POST':

        form_zapis = ZapisForm(request.POST)
        if form_zapis.is_valid():

            zapis = form_zapis.save(commit=False)
            zapis.save()
            new_zapis = Zapis.objects.get(id=zapis.id)
            new_zapis.procedura_name = Uslugi.objects.get(id=nameUslugi)
            new_zapis.save()
            klient = Klients(name= request.POST.get('client_name'), phone= request.POST.get('phone'))

            klient.save()
            try:
                sendMessage()
            except:
                print('Не удалось отправить сообщение')
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


#_______________ZAPOLNENIE KALENDARYA
def calendar_view(request):



    zapisi = Zapis.objects.all()
    uslugi = Uslugi.objects.all()
    try:
        status1_quant = len(zapisi.filter(zapis_status='1'))
    except:
        status1_quant = 0

    context = {
        'fill_cal': fill_cal()['date_list'],
        'months': fill_cal()['month_list'],
        'years': fill_cal()['year_list'],
        'zapisi': zapisi,
        'current_year': fill_cal()['current_year'],
        'current_month': fill_cal()['current_month'],
        'today': datetime.today(),
        'status1_quant': status1_quant,
        'uslugi': uslugi,
    }

    if 'monthSwitch' in request.GET:
        context = {
            'fill_cal': fill_cal(month=int(request.GET["monthSwitch"]), year=int(request.GET["yearSwitch"]))['date_list'],
            'months': fill_cal(month=int(request.GET["monthSwitch"]))['month_list'],
            'years': fill_cal(year=int(request.GET["yearSwitch"]))['year_list'],
            'zapisi': zapisi,
            'current_year': fill_cal(year=int(request.GET["yearSwitch"]))['current_year'],
            'current_month': fill_cal(month=int(request.GET["monthSwitch"]))['current_month'],
            'today': datetime.today(),
            'status1_quant': status1_quant,
            'uslugi': uslugi,
        }
    return render(request, 'main/calendar.html', context=context) if request.user.is_staff else redirect('home')



#______________________________STRANICA NEPODTVERGDENNIH ZAPISEI
def calendar_gdut_view(request):
    zapisi = Zapis.objects.all()
    uslugi = Uslugi.objects.all()


    try:
        status1_quant = len(zapisi.filter(zapis_status='1'))
    except:
        status1_quant = 0
    context = {
        'zapisi': zapisi,
        'uslugi': uslugi,
        'status1_quant': status1_quant,
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
            return render(request, 'main/calendar-gdut.html', context=context) if request.user.is_staff else redirect('home')





    return render(request, 'main/calendar-gdut.html', context=context)
#---------------------REDAKTIROVANIE ZAPISEI
def calendar_edit(request):
    print(request.POST)

    zapisi = Zapis.objects.all()
    uslugi = Uslugi.objects.all()


    try:
        status1_quant = len(zapisi.filter(zapis_status='1'))
    except:
        status1_quant = 0
    context = {
        'zapisi': zapisi,
        'uslugi': uslugi,
        'status1_quant': status1_quant,
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
            if request.POST.get('status') != '':
                zapis.zapis_status = request.POST.get('status')
            if request.POST.get('usluga') != '':
                id_uslugi = str(request.POST.get('usluga')).split('-')[1]
                name_usluga = Uslugi.objects.get(id=id_uslugi)
                zapis.procedura_name = name_usluga
            zapis.save()
            return redirect('/calendar')
        except:
            return render(request, 'main/calendar.html', context=context)

    if 'deleteBtn' in request.POST:
        Zapis.objects.filter(id=int(request.POST.get('deleteBtn'))).delete()
        return redirect('/calendar')





    return render(request, 'main/calendar.html', context=context) if request.user.is_staff else redirect('home')





def CustomCal(request):

    zapisi = Zapis.objects.all()
    context = {
        'fill_cal': fill_cal()['date_list'],
        'zapisi': zapisi,
    }

    return render(request, 'main/calendar.html', context=context)