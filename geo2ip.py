#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg
import csv
import json
import argparse as ag

parser = ag.ArgumentParser(description="Find IP from GEO Location")
parser.add_argument('lat', type=float, help='latitude of target')
parser.add_argument('lon', type=float, help='longitude of target')

args = parser.parse_args()

def getCountryByCoord(lat, lng):
    results = str(rg.search((lat,lng)))
    print results

#gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
#res = gi.record_by_addr("185.65.53.155")
#print str(res['latitude']) + "," + str(res['longitude'])

getCountryByCoord("40.151371","-3.409015")
