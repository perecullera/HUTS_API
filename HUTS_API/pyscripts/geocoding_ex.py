import json
from urllib import quote

__author__ = 'perecullera'

import urllib2
import csv, sys , os

csv_filepathname = "huts.csv"


sys.path.append("/Users/perecullera/virtualen/HUTS_API/HUTS_API")
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HUTS_API.settings')

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
#row_count = sum(1 for row in dataReader)
print "datReader size: " #+ str(row_count)


def geoCoding(list):
    address = quote(str(list[0])) +','+quote(list[1])+','+'Barcelona'+',ES'
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % address
    wjdata = json.load(urllib2.urlopen(url))
    status = wjdata['status']
    if status=='OK':
        location =  wjdata['results'][0]['geometry']['location']
        print "OK" + " location= " + str(location)
    else:
        print status
    return status

def getAddress(row):
    fullAdd = row[3]
    addList = fullAdd.split(',')
    if len(addList)>1:
        street = addList[0]
        number = addList[1]
        print 'street: '+ street + ' address: '+ number
        return number.strip(),street.strip()
    else:
        return '0','carrer'


for row in dataReader:
    response = geoCoding(getAddress(row))
    print 'response: ' + str(response)

