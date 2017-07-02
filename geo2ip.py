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

def getCountryByCoord(lat, lon):
    results = rg.search((lat,lon))
    return results[0]["cc"].lower()

def IPFromCC(cc):
    data = []
    for row in csv.reader(open('netblocks/'+cc+".csv")):
        data.append(row[0:2])
    return data

def IPFromCoord(lat, lon):
    cc = getCountryByCoord(lat,lon)
    return IPFromCC(cc)

#gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
#res = gi.record_by_addr("185.65.53.155")
#print str(res['latitude']) + "," + str(res['longitude'])

print IPFromCoord(args.lat, args.lon)

