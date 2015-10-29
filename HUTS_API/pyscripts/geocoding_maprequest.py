import csv
import json
import sys
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
sys.path.append("/Users/perecullera/virtualen/HUTS_API")

from hutsAPI.models import Hut
from urllib import quote
import urllib2

django.setup()

__author__ = 'perecullera'

url = 'http://www.mapquestapi.com/geocoding/v1/address?key=9msQDSYldUqqCsEe1VHsG8V2uDGoGznw&location=22%%20Agullers%20,BARCELONA,ES'

csv_filepathname = "huts.csv"


sys.path.append("/Users/perecullera/virtualen/HUTS_API/HUTS_API")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
row_count = sum(1 for row in dataReader)

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')



def geoCoding(list):
    address = quote(str(list[0])) +','+quote(list[1])+','+'Barcelona'+',ES'
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
        #print "OK" + " lat = " + str(lat) + ' long = ' + str(lng)
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

# def saveAdd(row, hut):
#     address = Address()
#     fullAdd = getAddress(row)
#     address.number = fullAdd[0]
#     address.street = fullAdd[1]
#     address.hut = hut
#     reqRes = geoCoding([address.number,address.street])
#     #print 'resqRes: ' + str(reqRes)
#     if reqRes[0] == 0:
#         address.latitude = float(reqRes[1])
#         address.longitude = float(reqRes[2])
#         address.postal_code = int(row[10])
#         address.save()
#         return 'OK'
#     else:
#         return 'Fail'

#Hut.objects.all().delete()

saved = 0
attempts = 0

file = open('log.txt','w+')

for row in dataReader:
    try:
        if row[4] == 'Barcelona':
            hut = Hut()
            if not Hut.objects.filter(code = row[0]).exists():
                hut.code = row[0]
                hut.DC = int(row[1])
                hut.name = row[2]
                #print 'row[9]: ' + row[9]
                if row[9] is not '':
                    hut.telefon = int(row[9])
                hut.email = row[8]
                fullAdd = getAddress(row)
                hut.number = fullAdd[0]
                hut.street = fullAdd[1]
                reqRes = geoCoding([hut.number,hut.street])
                #print 'resqRes: ' + str(reqRes)
                if reqRes[0] == 0:
                    hut.latitude = float(reqRes[1])
                    hut.longitude = float(reqRes[2])
                    hut.postal_code = int(row[10])
                result = hut.save()
                #print 'result = ' + str(result)
                attempts += 1
                saved += 1
                print 'saved: ' + str(saved)
    except Exception as e:
        file.write('Hut ' + str(hut)+ 'not saved'+ ' cause exception: ' + str(e))

print 'row_count = ' + str(row_count) + ' saved = ' + str(saved)

