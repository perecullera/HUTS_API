import pyproj
import csv
from pyproj import Proj
from pyproj import transform


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

for row in cr:
  print row[0], row[1], row[2], row[3], row[4], row[5], row[6]
  x1=float(row[5])/1000
  y1=float(row[6])/1000

  x2, y2 = pyproj.transform(p3,p1,x1,y1)
  #'%9.3f %11.3f' % (x2,y2)

  str_temp = row[0], row[1], row[2], row[3],row[4], row[5], row[6], x2,y2
  csv_writer.writerow(str_temp)