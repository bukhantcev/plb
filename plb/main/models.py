from django.db import models
from uuid import uuid4
import os

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
    bg_image = models.ImageField(upload_to="static/user_img/bg_uslugi", verbose_name="Фоновая картинка", blank=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'





class Uslugi_groups(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название группы процедур", default='')
    bg_image = models.ImageField(upload_to="static/user_img/bg_groups", verbose_name="Фоновая картинка",
                                 blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа процедур'
        verbose_name_plural = 'Группы процедур'

