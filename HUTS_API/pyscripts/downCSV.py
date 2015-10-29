import sys
import django
import os

__author__ = 'perecullera'


os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
sys.path.append("/Users/perecullera/virtualen/HUTS_API")

from hutsAPI.admin import HutResource
from import_export import resources



django.setup()

dataset = HutResource().export()
file = open('huts_latlong.csv','w+')
file.write(dataset.csv)
