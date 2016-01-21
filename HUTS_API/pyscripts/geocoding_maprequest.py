import csv
import json
import sys
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
sys.path.append("/Users/perecullera/virtualen/HUTS_API")

from hutsAPI.models import Hut, Building
from urllib import quote
import urllib2

django.setup()

__author__ = 'perecullera'

#url = 'http://www.mapquestapi.com/geocoding/v1/address?key=9msQDSYldUqqCsEe1VHsG8V2uDGoGznw&location=22%%20Agullers%20,BARCELONA,ES'

csv_filepathname = "huts.csv"


sys.path.append("/Users/perecullera/virtualen/HUTS_API/HUTS_API")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
row_count = sum(1 for row in dataReader)

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')



def geoCoding(list):
    address = quote(str(list[0])) +','+quote(list[1])+','+'Barcelona'+',ES'+','+quote(list[2])
    #print 'address = ' + str(address)
    url="http://www.mapquestapi.com/geocoding/v1/address?key=9msQDSYldUqqCsEe1VHsG8V2uDGoGznw&location=%s" % address
    response = urllib2.urlopen(url)
    #print 'response = ' + str(response)
    wjdata = json.load(response)
    #print 'json response = ' + str(wjdata)
    status = wjdata['info']['statuscode']
    if status== 0 :
        location =  wjdata['results'][0]['locations'][0]['displayLatLng']
        lat = wjdata['results'][0]['locations'][0]['displayLatLng']['lat']
        lng = wjdata['results'][0]['locations'][0]['displayLatLng']['lng']
        print "OK" + " lat = " + str(lat) + ' long = ' + str(lng)
        return [status, lat, lng]
    else:
        print status
    return status

def getAddress(row):
    fullAdd = row[3]
    addList = fullAdd.split(',')
    if len(addList)>1:
        street = addList[0]
        number = addList[1]
        #print 'street: '+ street + ' address: '+ number
        return number.strip(),street.strip()
    else:
        return '0','carrer'

def getBuilding(row, hut):
    fullAdd = getAddress(row)
    street = fullAdd[0]
    number = fullAdd[1]
    zip = row[10]
    if not Building.objects.filter(street = street,number = number,
                                   zip = zip).exists():
        building = Building()
        building.zip = zip
        building.number = number
        building.street = street
        reqRes = geoCoding([building.number,building.street,building.zip])
        #print 'resqRes: ' + str(reqRes)
        if reqRes[0] == 0:
            building.latitude = float(reqRes[1])
            building.longitude = float(reqRes[2])
            building.zip = int(row[10])
        result = building.save()
    else:
        building = Building()
        building = Building.objects.filter(street = street,
            number = number, zip = zip).first()

    hut.building = building





saved = 0
attempts = 0

file = open('log.txt','w+')
while (attempts < 15):
    for row in list(dataReader)[:1000]:
        print row
        try:
            if row[4] == 'Barcelona':
                attempts += 1
                hut = Hut()
                if not Hut.objects.filter(code = row[0]).exists():
                    hut.code = row[0]
                    hut.DC = int(row[1])
                    hut.name = row[2]
                    #print 'row[9]: ' + row[9]
                    if row[9] is not '':
                        hut.telefon = int(row[9])
                    hut.email = row[8]
                    getBuilding(row, hut)
                    result = hut.save()
                    #print 'result = ' + str(result)

                    saved += 1
                    print 'saved: ' + str(saved)
        except Exception as e:
            #print str('Hut ' + str(hut.code)+ 'not saved'+ ' cause exception: ' + str(e))
            file.write('Hut ' + str(hut.code)+ 'not saved'+ ' cause exception: ' + str(e))

file.close()

print 'row_count = ' + str(row_count) + ' saved = ' + str(saved)

