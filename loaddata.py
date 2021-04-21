from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

def load_and_unzip(zipurl):
  with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
      zfile.extractall()

// veraenderung
