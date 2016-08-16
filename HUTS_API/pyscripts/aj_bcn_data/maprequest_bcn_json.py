import csv
import json
import sys
import urllib

import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
sys.path.append("/Users/perecullera/virtualen/HUTS_API")

from hutsAPI.models import Hut, Building
from urllib import quote
import urllib2
import shapely_geojson_bcn

django.setup()

__author__ = 'perecullera'

#url = 'http://www.mapquestapi.com/geocoding/v1/address?key= &location=22%%20Agullers%20,BARCELONA,ES'
#url2 = 'http://www.mapquestapi.com/geocoding/v1/address?key=YOUR_KEY_HERE&street=1090 N Charlotte St&city=Lancaster&state=PA&postalCode=17603

csv_filepathname = "csvs/huts.csv"


sys.path.append("/Users/perecullera/virtualen/HUTS_API/HUTS_API")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
row_count = sum(1 for row in dataReader)

#dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')


#list[0]= number, list[1]=street, list[2]=zip
def geoCoding(list):
    try:
        url = do_url(list)
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
    except Exception as e:
        print e

#list[0]= number, list[1]=street, list[2]=zip
def do_url(list):
    address = {}
    fulladdress = {}
    address['street'] = list[1] + ' ' + list[0]
    address['city'] = 'Barcelona'
    address['country'] = 'ES'
    address['postalCode'] = list[2]
    fulladdress['location'] = address
    fulladdress = json.dumps(fulladdress)
    url = urllib.quote(
        "http://www.mapquestapi.com/geocoding/v1/address?key=9msQDSYldUqqCsEe1VHsG8V2uDGoGznw&inFormat=json&json=" \
        "%s" % fulladdress, safe=":/?=&")
    return url


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


#gets a row from csv
#returns the address dict: number, street, bloc, pis, porta, barri, districte
def read_row_aj(row):
    options = {'C' : 'carrer',
               'PL' : 'plaça    ',
               'PTGE' : 'peatge',
               'VIA' : 'via',
               'RBLA' : 'rambla',
               'RIER' : 'riera',
               'AV' : 'avinguda',
               'PG' : 'passeig',
               'CTRA' : 'carretera',
               'G.V.':'gran via',
               'TRAV':'travessera',
               'RDA':'ronda',
               'BDA':'BDA',
               'PLA':'pla',
               'TRVS':'travessia',
               'CSTA':'costa',
               }
    address = {}
    address['tipus_carrer'] = options[row[3]]()
    address['carrer'] = row[4]
    address['numero'] = row[6]
    #is letter
    if row[7]!='':
        address['numero'] =+ row[7]
    #is number 2?
    if row[8]!='':
        address['numero'] =+ row[8]
    #is letter 2?
    if row[9] != '':
        address['numero'] =+ row[9]
    address['bloc'] = ''
    #it's bloc?
    if row[10] != '':
        address['bloc'] = row[10]
    #it's portal?
    if row[11] != '':
        address['bloc'] =+ row[11]
    #it's 'escala'?
    if row[12] != '':
        address['bloc'] =+ row[12]
    #hi ha pis?
    pis =''
    if row[13] != '':
        address['bloc'] = row[13]
    #hi ha porta
    address['porta'] = ''
    if row[14] != '':
        address['porta'] = row[14]
    #districte
    address['districte'] = row[1]
    #barri
    address['barri'] = row[2]
    return address



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
s_g = shapely_geojson_bcn.shapely_geocoding()
while (attempts < 15):
    for row in list(dataReader)[:50000]:
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

