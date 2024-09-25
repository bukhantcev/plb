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
    desc = models.TextField(max_length=300, verbose_name="Описание", default='', blank=True)
    price = models.TextField(max_length=300, verbose_name='Стоимомть', default='', blank=True)
    bg_image = ImageMaskField(upload_to='uslugi_bg/', verbose_name="Фоновая картинка", blank=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'





class Uslugi_groups(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы процедур", default='')
    bg_image = models.ImageField(upload_to='group_bg', verbose_name="Фоновая картинка",
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



