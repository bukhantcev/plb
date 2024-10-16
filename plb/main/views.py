
from datetime import datetime

from django.shortcuts import render, redirect


from .forms import ZapisForm, KlientsForm
from .models import Uslugi, Uslugi_groups, Sertifikate, Zapis, Klients, Preparati

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
        'form_klients': KlientsForm,
        'preparati': Preparati.objects.all(),
               }


    return render(request, 'main/home.html', context=context)

#----------------------------ZAPIS BEZ USLUGI
def zapis(request):
    if request.method == 'POST':

        form_zapis = ZapisForm(request.POST)
        if form_zapis.is_valid():

            zapis = form_zapis.save(commit=False)
            zapis.phone = zapis.phone[-10:]
            try:
                klient = Klients.objects.get(phone=request.POST.get('phone'))
                zapis.client_name = f'{klient.name} {klient.last_name}'
            except:
                pass
            zapis.save()


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
        'form_klients': KlientsForm,
        'preparati': Preparati.objects.all(),
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
            zapis.phone = zapis.phone[-10:]
            try:
                klient = Klients.objects.get(phone=request.POST.get('phone'))
                zapis.client_name = f'{klient.name} {klient.last_name}'
            except:
                pass
            zapis.save()
            new_zapis = Zapis.objects.get(id=zapis.id)
            new_zapis.procedura_name = Uslugi.objects.get(id=nameUslugi)
            new_zapis.save()
            # klient = Klients(name= request.POST.get('client_name'), phone= request.POST.get('phone'))
            #
            # klient.save()
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
        'form_klients': KlientsForm,
        'preparati': Preparati.objects.all(),
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
        'preparati': Preparati.objects.all(),
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
            'preparati': Preparati.objects.all(),
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
        'preparati': Preparati.objects.all(),
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
            if request.POST.get('kolvo_preparata') != '':
                zapis.kolvo_preparata = request.POST.get('kolvo_preparata')
            if request.POST.get('zone') != '':
                zapis.zone = request.POST.get('zone')
            if request.POST.get('primechanie') != '':
                zapis.primechanie = request.POST.get('primechanie')
            if request.POST.get('next_date') != '':
                zapis.next_date = request.POST.get('next_date')
            if request.POST.get('usluga') != '':
                id_uslugi = str(request.POST.get('usluga')).split('-')[1]
                name_usluga = Uslugi.objects.get(id=id_uslugi)
                zapis.procedura_name = name_usluga
            if request.POST.get('preparat') != '':
                id_preparata = str(request.POST.get('preparat')).split('-')[1]
                name_preparata = Preparati.objects.get(id=id_preparata)
                zapis.preparat = name_preparata
            zapis.zapis_status = '2'
            try:
                klient = Klients.objects.get(phone=zapis.phone)
                zapis.client_name = f'{klient.name} {klient.last_name}'
            except:
                pass
            zapis.save()
            return redirect('/calendar/jdut-podtvergdeniy')
        except:
            return render(request, 'main/calendar-gdut.html', context=context) if request.user.is_staff else redirect('home')

    if 'deleteBtn' in request.POST:
        Zapis.objects.filter(id=int(request.POST.get('deleteBtn'))).delete()
        return redirect('/calendar/jdut-podtvergdeniy')



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
        'preparati': Preparati.objects.all(),
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
            if request.POST.get('kolvo_preparata') != '':
                zapis.kolvo_preparata = request.POST.get('kolvo_preparata')
            if request.POST.get('zone') != '':
                zapis.zone = request.POST.get('zone')
            if request.POST.get('primechanie') != '':
                zapis.primechanie = request.POST.get('primechanie')
            if request.POST.get('next_date') != '':
                zapis.next_date = request.POST.get('next_date')
            if request.POST.get('status') != '':
                zapis.zapis_status = request.POST.get('status')
            if request.POST.get('usluga') != '':
                id_uslugi = str(request.POST.get('usluga')).split('-')[1]
                name_usluga = Uslugi.objects.get(id=id_uslugi)
                zapis.procedura_name = name_usluga
            if request.POST.get('preparat') != '':
                id_preparata = str(request.POST.get('preparat')).split('-')[1]
                name_preparata = Preparati.objects.get(id=id_preparata)
                zapis.preparat = name_preparata

            try:
                klient = Klients.objects.get(phone=zapis.phone)
                zapis.client_name = f'{klient.name} {klient.last_name}'
            except:
                pass
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




def politica_conf(request):


    return render(request, 'main/politica-conf.html')



def client_card(request):
    if request.method == 'GET':
        try:
            klient = Klients.objects.get(phone=request.GET.get('phone'))
            age = datetime.now().year - klient.date_r.year - ((datetime.now().month, datetime.now().day) < (klient.date_r.month, klient.date_r.day))
            context = {
                'klient': klient,
                'age': age,
                'path': '-1',
            }
        except:
            klient = Klients(phone=request.GET.get('phone'))
            klient.save()
            context = {
                'klient': klient,
                'age': '?',
                'path': '-1',
            }

    if request.method == 'POST':
        if 'btnClientCard' in request.POST:
            print(request.POST)

            try:
                klient = Klients.objects.get(phone=request.POST.get('phone'))
                klient.last_name = request.POST.get('last_name')
                klient.otchestvo = request.POST.get('otchestvo')
                klient.name = request.POST.get('name')
                klient.date_r = datetime.strptime(request.POST.get('date_r'), "%Y-%m-%d").date()
                klient.hron = request.POST.get('hron')
                klient.alergo = request.POST.get('alergo')
                klient.primech = request.POST.get('primech')
                klient.save()

                context = {
                    'klient': klient,
                    'message': 'Данные сохранены',
                    'path': '-1',
                }

                try:
                    zapis_edit = Zapis.objects.get(phone=klient.phone)
                    zapis_edit.client_name = f'{klient.name} {klient.last_name}'
                    zapis_edit.save()
                except:
                    pass
                context['path'] = '-2'
            except:
                context = {
                    'message': 'Ошибка',

                }

    context['zapisi'] = Zapis.objects.all()
    print(context)



    return render(request, 'main/client-card.html', context=context)




