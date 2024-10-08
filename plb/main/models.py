from datetime import datetime

from django.db import models
from uuid import uuid4
import os
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
    name = models.CharField(max_length=30, verbose_name='Название процедуры')
    group = models.ForeignKey(to="Uslugi_groups", on_delete=models.CASCADE, verbose_name="Группы процедур")
    desc = models.TextField(max_length=30000, verbose_name="Описание", default='', blank=True)
    price = models.TextField(max_length=300, verbose_name='Стоимомть', default='', blank=True)
    bg_image = ImageMaskField(upload_to='uslugi_bg/', verbose_name="Фоновая картинка", blank=True)



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
     name = models.CharField(max_length=50, verbose_name='Имя клиента', default='')
     phone = models.CharField(max_length=50, verbose_name='Номер телефона клиента', default='')

     def __str__(self):
         return self.name

     class Meta:
         verbose_name = 'Клиент'
         verbose_name_plural = 'Клиенты'






class Zapis(models.Model):
    class Status(models.TextChoices):
        GDET = '1', 'Ждет подтверждения'
        OK = '2', 'Подтверждено'
        DELETE = '3', 'Отменено'


    create_date = models.DateField(verbose_name="Дата создания записи", auto_now_add=True)
    client_name = models.CharField(max_length=50, verbose_name='Имя клиента')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', default='')
    procedura_name = models.ForeignKey(to=Uslugi, on_delete=models.CASCADE, verbose_name='Название процедуры', blank=True, null=True, default='')
    date_proceduri = models.DateField(verbose_name='Дата и время процедуры', default=datetime.now().date())
    time_proceduri = models.TimeField(verbose_name='Время записи', default=datetime.now().time())
    zapis_status = models.CharField(choices=Status.choices, default=Status.GDET, max_length=20)
    price = models.CharField(max_length=50, verbose_name="Стоимость", default='', blank=True)
    descr = models.TextField(max_length=300, verbose_name='Описание', default='', blank=True)






    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



