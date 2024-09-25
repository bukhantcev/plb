import os

from PIL import Image
from PIL.EpsImagePlugin import split
from PIL.ImageDraw import ImageDraw


# def Img_save(dir_name):
#     path = f'../static/media/{dir_name}'
#     lst = os.listdir(path)
#     for i in lst:
#         path_tr = f'{path}/{i}'
#         img = Image.open(path_tr)
#         mask = Image.open('../static/media/mask/mask.png').resize([img.size[0],img.size[1]]).convert("L")
#
#
#
#         img.putalpha(mask)
#         dir_name = os.path.dirname(f'{path}-mask/{i.split(".")[0]}-mask.png')
#
#         if not os.path.exists(dir_name):
#             os.mkdir(dir_name)
#
#         img.save(f'{path}-mask/{i.split(".")[0]}-mask.png')
#     return print('Картинка готова')
#
# Img_save('sertifikate-img')

