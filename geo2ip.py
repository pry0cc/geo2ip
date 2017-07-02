#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg
import csv
import json

def getCountryByCoord(lat, lng):
    results = rg.search((lat,lng))
    return results[0]["cc"].lower()

def IPFromCC(cc):
    print csv.reader(open('netblocks/'+cc+".csv")).next()

#gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
#res = gi.record_by_addr("185.65.53.155")
#print str(res['latitude']) + "," + str(res['longitude'])

IPFromCC(getCountryByCoord("40.151371","-3.409015"))

