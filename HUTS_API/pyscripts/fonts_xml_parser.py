import xml.etree.ElementTree as ET
import pyproj
import csv
from pyproj import Proj
from pyproj import transform


tree = ET.parse('Fonts.xml')
root = tree.getroot()





#source
p1 = pyproj.Proj(proj='latlong',datum='WGS84')
p3 = Proj("+proj=utm +zone=31 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

# read from csv
cr = csv.reader(open("fonts.csv","rb"),delimiter=';')
next(cr, None)  # skip the headers

# writer to csv
csvfile = open('fonts_latlong.csv', 'wb')
csv_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#source
#p1 = pyproj.Proj(proj='latlong',datum='WGS84')

# final projectoin
#p2 = pyproj.Proj(init='epsg:3857')

for row, child in zip(cr, root):

  print row[0], row[1], row[2], row[3], row[4], row[5], row[6]


  #'%9.3f %11.3f' % (x2,y2)
  print child.tag
  x = child[0].getchildren()[0].text
  print x

  y1=float(row[6])/1000
  x1=float(x)/1000

  x2, y2 = pyproj.transform(p3,p1,x1,y1)

  str_temp = row[0], row[1], row[2], row[3],row[4], x1, row[6], x2,y2
  csv_writer.writerow(str_temp)

