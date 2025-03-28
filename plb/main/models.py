from datetime import datetime

import django.utils.timezone
from django.db import models
from uuid import uuid4
import os

from django.db.models import ImageField

from .fields import ImageMaskField






# def path_and_rename(path):
#     def wrapper(instance, filename):
#         ext = filename.split(".")[-1]
#         # get filename
#         filename = "{}.{}".format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(path, filename)
#     return wrapper


class Uslugi(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название процедуры')
    group = models.ForeignKey(to="Uslugi_groups", on_delete=models.CASCADE, verbose_name="Группы процедур")
    desc = models.TextField(max_length=30000, verbose_name="Описание", default='', blank=True)
    price = models.TextField(max_length=30000, verbose_name='Стоимомть', default='', blank=True)
    bg_image = ImageMaskField(upload_to='uslugi_bg/', verbose_name="Фоновая картинка", blank=True)
    zastavka = ImageField(upload_to='bg_uslugi_full/', verbose_name='Заставка', blank=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'





class Uslugi_groups(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы процедур", default='')
    bg_image = ImageMaskField(upload_to='group_bg', verbose_name="Фоновая картинка",
                                 blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа процедур'
        verbose_name_plural = 'Группы процедур'

#-----------------USLUGI-------------------------------#


#_________________SERTIFIKATI__________________________#



class Sertifikate(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название", default='')
    file = models.ImageField(upload_to='sertifikate-img/', verbose_name="Фото сертификата")
    priority = models.IntegerField( verbose_name="Приоритет (чем меньше - тем раньше появится)")


    def __str__(self):
        return self.file.url

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'



class Klients(models.Model):
     name = models.CharField(max_length=50, verbose_name='Имя', default='')
     otchestvo = models.CharField(max_length=50, verbose_name='Отчество', default='', blank=True)
     last_name = models.CharField(max_length=50, verbose_name='Фамилия', default='')
     date_r = models.DateField(verbose_name='Дата рождения', default=None, blank=True, null=True)
     hron = models.TextField(verbose_name="Хронические заболевания", max_length=3000, default='', blank=True)
     alergo = models.TextField(verbose_name="Алергоанамнез", max_length=3000, default='', blank=True)
     primech = models.TextField(verbose_name="Примечания", max_length=3000, default='', blank=True)
     phone = models.CharField(max_length=50, verbose_name='Номер телефона клиента', default='')

     def __str__(self):
         return f'{self.name} {self.last_name}'

     class Meta:
         verbose_name = 'Клиент'
         verbose_name_plural = 'Клиенты'






class Zapis(models.Model):
    class Status(models.TextChoices):
        GDET = '1', 'Ждет подтверждения'
        OK = '2', 'Подтверждено'
        COMPLET = '4', 'Выполнено'
        DELETE = '3', 'Отменено'


    create_date = models.DateField(verbose_name="Дата создания записи", auto_now_add=True)
    client_name = models.CharField(max_length=50, verbose_name='Имя клиента')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', default='')
    procedura_name = models.ForeignKey(to=Uslugi, on_delete=models.CASCADE, verbose_name='Название процедуры', blank=True, null=True, default='')
    date_proceduri = models.DateField(verbose_name='Дата и время процедуры', default=datetime.now().date())
    time_proceduri = models.TimeField(verbose_name='Время записи', default=datetime.now().time())
    zapis_status = models.CharField(choices=Status.choices, default=Status.GDET, max_length=20)
    price = models.CharField(max_length=50, verbose_name="Стоимость", default='', blank=True)
    descr = models.TextField(max_length=500, verbose_name='Описание', default='', blank=True)
    primechanie = models.TextField(max_length=500, verbose_name='Примечание', default='', blank=True)
    preparat = models.ForeignKey(to='Preparati', on_delete=models.CASCADE, verbose_name='Препарат', blank=True, null=True, default='')
    kolvo_preparata = models.CharField(max_length=100, verbose_name="Количество препарата", default='', blank=True)
    zone = models.CharField(max_length=300, verbose_name="Зона введения", default='', blank=True)
    next_date = models.DateField(verbose_name='Следующий визит', default=datetime.now().date(), blank=True, null=True)



    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



class Preparati(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название', default='')
    proishogdenie = models.CharField(max_length=100, verbose_name='Страна происхождения', default='', blank=True)
    edinica = models.CharField(max_length=20, verbose_name='Единица измерения', default='', blank=True)
    kolichestvo = models.CharField(max_length=30, verbose_name='Количество', default='', blank=True)
    price = models.CharField(max_length=100, verbose_name='Цена', default='')
    procedura = models.ForeignKey(Uslugi, on_delete=models.CASCADE, verbose_name='Процедура', blank=True, null=True)
    opisanie = models.TextField(max_length=1000, verbose_name='Описание', default='', blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
