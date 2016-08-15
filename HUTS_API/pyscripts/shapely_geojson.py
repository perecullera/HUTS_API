import csv
import json
import sys
from datetime import date

import django
import os
import json
from shapely.geometry import Point, shape

class shapely_geocoding:

    os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
    sys.path.append("/Users/perecullera/virtualen/HUTS_API")


    django.setup()

    __author__ = 'perecullera'

    csv_filepathname = "huts.csv"

    print 'current path' + os.path.abspath(os.curdir)
    file = open('logs/log'+str(date.today())+'.txt','w+')

    #print os.path.abspath(os.curdir)
    #os.chdir("..") #one folder up
    #print os.path.abspath(os.curdir)
    f = open('jsons/districtes_geo.json', 'r')
    js = json.load(f)


    # construct point based on lat/long returned by geocoder
    points = Point( 2.17816, 41.425845),Point( 0, 1),Point( 2.17816, 41.425845)

    def inBcn(self, building):
        # load GeoJSON file containing sectors
        #with ('districtes_geo.json', 'r') as f:

        point = Point(building.longitude, building.latitude)
        finded = False
        # check each polygon to see if it contains the point
        for feature in self.js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                print 'Found containing polygon:', feature['properties']['N_Distri']
                finded = True


        if not finded:
            file.write(str(building) + '\n')

        return finded


