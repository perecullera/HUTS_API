import csv
import json
import sys
from datetime import date

import django
import os
import json
from shapely.geometry import Point, shape


os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
sys.path.append("/Users/perecullera/virtualen/HUTS_API")

#from hutsAPI.models import Hut, Building
from urllib import quote
import urllib2

django.setup()

__author__ = 'perecullera'

#url = 'http://www.mapquestapi.com/geocoding/v1/address?key=9msQDSYldUqqCsEe1VHsG8V2uDGoGznw&location=22%%20Agullers%20,BARCELONA,ES'

csv_filepathname = "huts.csv"

file = open('logs/log'+str(date.today())+'.txt','w+')

# load GeoJSON file containing sectors
#with ('districtes_geo.json', 'r') as f:
f = open('districtes_geo.json', 'r')
js = json.load(f)

# construct point based on lat/long returned by geocoder
points = Point( 2.17816, 41.425845),Point( 0, 1),Point( 2.17816, 41.425845)



for point in points:
    finded = False
    # check each polygon to see if it contains the point
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            print 'Found containing polygon:', feature['properties']['N_Distri']
            finded = True

    if not finded:
        file.write(str(point) + '\n')


