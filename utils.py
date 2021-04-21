from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
from PIL import Image
import numpy as np

def load_and_unzip(zipurl):
"""Lädt das zipfile unter zipurl und entpackt es ins aktuelle Arbeitsverzeichnis"""
  with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
      zfile.extractall()

def img_path_to_float_array(path):
"""Lädt eine unter path gespeicherte Bilddatei und erzeugt ein entsprechendes Numpy Array vom Typ float32 mit Wertebereich 0.0 - 1.0"""
  img = Image.open(path)
  img_as_array = np.array(img)
  return (img_as_array / 255.0).astype("float32")
