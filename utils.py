from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from PIL import Image
from PIL import ImageOps
import numpy as np
from os import path

## Laden

def load_and_unzip_from_url(zipurl):
  with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
      zfile.extractall()

## Laden und Umwandeln

def img_path_to_np_array(path):
  img = Image.open(path)
  img_as_array = np.array(img)
  return (img_as_array / 255.0).astype("float32")

## Numpy-Arrays Umwandeln (Farbe)

def rgb_to_grayscale(np_array):
  return np.dot(np_array, [0.33, 0.33, 0.33])

def grayscale_to_rgb(np_array):
  return np.stack((np_array,)*3, axis=-1)

def add_color_channel(np_array):
  return np_array[..., None]

## Bild Dateien umwandeln

def load_resize_save(img_path, target_width, target_height, prepend_filename):
  img = Image.open(img_path)
  resized_img = ImageOps.fit(img, (target_width, target_height), Image.ANTIALIAS)
  save_path = path.split(img_path)[0] + "/" + prepend_filename + path.split(img_path)[1]
  print(save_path);

  resized_img.save(save_path);
