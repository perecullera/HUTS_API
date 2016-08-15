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
import shapely_geojson

django.setup()

__author__ = 'perecullera'

#url = 'http://www.mapquestapi.com/geocoding/v1/address?key= &location=22%%20Agullers%20,BARCELONA,ES'
#url2 = 'http://www.mapquestapi.com/geocoding/v1/address?key=YOUR_KEY_HERE&street=1090 N Charlotte St&city=Lancaster&state=PA&postalCode=17603

csv_filepathname = "csvs/huts_prova_100_gene.csv"


sys.path.append("/Users/perecullera/virtualen/HUTS_API/HUTS_API")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
row_count = sum(1 for row in dataReader)

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')



def geoCoding(list):
    address = quote(str(list[0])) +','+quote(list[1])+','+'Barcelona'+',ES'+','+quote(list[2])
    address = quote(str(list[0]) + ' ' + list[1]) + '&city=Barcelona&country=ES&postalCode=' + quote(list[2])
    url="http://www.mapquestapi.com/geocoding/v1/address?key=9msQDSYldUqqCsEe1VHsG8V2uDGoGznw&street=%s" % address
    response = urllib2.urlopen(url)
    wjdata = json.load(response)
    status = wjdata['info']['statuscode']
    if status== 0 :
        #location =  wjdata['results'][0]['locations'][0]['displayLatLng']
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
    #bloc by default is '' and only full if there's bloc
    bloc = ''
    pis = ''
    porta = ''
    #TODO carrer, num, escala/edifici, pis porta
    if len(addList)>1:
        street = addList[0]
        number = addList[1]
        length_aux = len(addList)
        #we make sure building have flat door info
        if len(addList)>2:
            #if length = 4 means it have bloc info
            if (len(addList)==4):
                bloc = addList[2]
                fullPisPorta = addList[3].strip()
            #otherwise it doesn't have bloc info
            else:
                fullPisPorta = addList[2].strip()
            pisPortaList = fullPisPorta.split(' ')
            pis = pisPortaList[0]
            porta = ' '
            if len(pisPortaList)>1:
                porta = pisPortaList[1]

        return number.strip(),street.strip(), bloc, pis.strip(), porta.strip()
    else:
        return '0','carrer'

def getBuilding(row, hut):
    fullAdd = getAddress(row)
    number = fullAdd[0]
    street = fullAdd[1]
    bloc = fullAdd[2]
    pis = fullAdd[3]
    porta = fullAdd[4]
    zip = row[10]
    if not Building.objects.filter(street = street,number = number,
                                   zip = zip).exists():
        building = Building()
        building.zip = zip
        building.number = number
        building.street = street
        building.bloc = bloc
        building.geocoded
        reqRes = geoCoding([building.number,building.street,building.zip])
        if reqRes[0] == 0:
            building.latitude = float(reqRes[1])
            building.longitude = float(reqRes[2])
            building.zip = int(row[10])
        result = building.save()
    else:
        building = Building()
        building = Building.objects.filter(street = street, number = number, zip = zip).first()
    hut.flat = pis
    hut.door = porta
    hut.building = building





saved = 0
attempts = 0
row_count = 0

file = open('log.txt','w+')
s_g = shapely_geojson.shapely_geocoding()
while (attempts < 15):
    for row in list(dataReader)[:500]:
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
                    if s_g.inBcn(hut.building):
                        hut.building.geocoded = True
                        hut.building.save()
                    result = hut.save()
                    saved += 1
                    print 'saved: ' + str(saved)
                    row_count += 1
                    print 'row counted ' + str(row_count)

        except Exception as e:
            #print str('Hut ' + str(hut.code)+ 'not saved'+ ' cause exception: ' + str(e))
            file.write('Hut ' + str(hut.code)+ 'not saved'+ ' cause exception: ' + str(e) + "\n")

file.close()

print 'row_count = ' + str(row_count) + ' saved = ' + str(saved)

