#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg
import csv


gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)

print rg.search(coordinates) 

res = gi.record_by_addr("185.65.53.155")
print str(res['latitude']) + "," + str(res['longitude'])

