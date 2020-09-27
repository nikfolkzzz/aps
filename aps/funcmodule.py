from PIL import Image
from skimage.io import imread_collection
import os
import sys


def my_function(text_to_display):
    print('text from my_function :: {}'.format(text_to_display))


def ctp(path):
    path = '{}'.format(path)
    image = []
    count = 0
    for root, dirs, filename in os.walk(path):
        for files in filename:
            if 'png' in files or 'jpg' in files:
                image.append(files)
        for img in image:
            count += 1
            Image.open(img, 'r').convert('RGB').save(
                r'' + str(img)[:-4] + '.pdf')


def cti():
    print('i am image converter')
