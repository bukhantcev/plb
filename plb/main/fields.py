# -*- coding: utf-8 -*-

import io

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile


class MaskFieldFile(ImageFieldFile):

    def save(self, name, content, save=True):
        content.file.seek(0)
        image = Image.open(content.file)
        image.resize([1440, 740])
        image_bytes = io.BytesIO()
        mask = Image.open('static/media/mask/mask.png').resize([image.size[0], image.size[1]]).convert("L")
        image.putalpha(mask)
        image.save(fp=image_bytes, format="WEBP")
        image_content_file = ContentFile(content=image_bytes.getvalue())
        super().save(name, image_content_file, save)


class ImageMaskField(models.ImageField):
    attr_class = MaskFieldFile

