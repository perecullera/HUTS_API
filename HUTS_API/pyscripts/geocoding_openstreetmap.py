import csv
import json
import sys
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')
sys.path.append("/Users/perecullera/virtualen/HUTS_API")

#from hutsAPI.models import Hut, Building
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


#list argument: 1st number, 2nd street, 3 zip code
def geoCoding(list):
    #address = quote(str(list[0])) +','+quote(list[1])+','+'Barcelona'+',ES'+','+quote(list[2])
    #print 'address = ' + str(address)
    number = list[0]
    street = list[1]
    city = 'Barcelona'
    country = 'Spain'
    zip = list[2]

    url="http://nominatim.openstreetmap.org/search?street="+ quote(number) +\
        '%20' + quote(street) +\
        "&city=" + quote(city) + "&country=" + quote(country) + "&postalcode=" + quote(zip) + "&format=json"


    print 'url ' + str(url)
    response = urllib2.urlopen(url)

    print 'response ' + str(response)

    wjdata = json.load(response)
    print 'wjdata ' + str(wjdata)
    #status = wjdata['info']['statuscode']
    #if status== 0 :
    lat = wjdata[0]['lat']
    lng = wjdata[0]['lon']
    print "OK" + " lat = " + str(lat) + ' long = ' + str(lng)
    return [lat, lng]
    # else:
    #     print status
    #return status

def getAddress(row):
    fullAdd = row[3]
    addList = fullAdd.split(',')
    if len(addList)>1:
        street = addList[0]
        number = addList[1]
        print 'street: '+ street + ' number: '+ number
        return [number.strip(),street.strip()]
    else:
        return '0','carrer'



saved = 0
attempts = 0

file = open('log_open.txt','w+')
while (attempts < 15):
    for row in list(dataReader)[:1000]:
        #print row
        try:
            if row[4] == 'Barcelona':
                print 'Barcelona'
                attempts += 1
                number_street = getAddress(row)
                print 'number_street ' + str(number_street)
                number_street.append(row[10])
                print 'before geocoding'
                geoCoding(number_street)

                print 'Adrres: ' + str(number_street)

        except Exception as e:
            #print str('Hut ' + str(hut.code)+ 'not saved'+ ' cause exception: ' + str(e))
            print e
            file.write('Hut ' + str(number_street)+ 'not saved'+ ' cause exception: ' + str(e))

file.close()

print 'row_count = ' + str(row_count) + ' saved = ' + str(saved)

