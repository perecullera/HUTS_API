__author__ = 'perecullera'

csv_filepathname = "huts.csv"

import csv, sys, os
import django

from django.conf import settings


sys.path.append("/Users/perecullera/virtualen/HUTS_API/HUTS_API")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')

from hutsAPI.models import Hut

#settings.configure()

#dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')


dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
fields = ['code', 'DC', 'name', 'email']
for row in dataReader:
    #treiem la primera linia
    if row[0] == "Codi de Registre":
        print row;
    else:
        print "row: " + str(row)
        hut = Hut()
        hut.code = row[0]
        print "row1= " + row[1]
        hut.DC = int(row[1])
        hut.name = row[2]
        hut.email = row[8]
        hut.telefon = row[9]
        hut.save()




