#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg
import csv
import argparse as ag
import math

parser = ag.ArgumentParser(description="Find IP from GEO Location")
parser.add_argument('lat', type=float, help='latitude of target')
parser.add_argument('lon', type=float, help='longitude of target')

args = parser.parse_args()

def ips(start, end):
    import socket, struct
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]

def getCountryByCoord(lat, lon):
    results = rg.search((lat,lon))
    return results[0]["cc"].lower()

def IPFromCC(cc):
    data = []
    for row in csv.reader(open('netblocks/'+cc+".csv")):
        data.append(row[0:2])
    return data

def IPFromCoord(lat, lon, radius):
    gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
    cc = getCountryByCoord(lat,lon)
    results = IPFromCC(cc)
    for ip_range in results:
        print "Starting new range"
        for ip in ips(ip_range[0], ip_range[1]):
            res = gi.record_by_addr(ip)
            ip_lat = str(float(math.floor(res["latitude"] * 1000) / 1000))
            ip_lon = str(float(math.floor(res["longitude"] * 1000) / 1000))
            
            if (str(lat) in ip_lat) and (str(lon) in ip_lon):
                print ip + ": " + ip_lat + ", " + ip_lon

#gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
#res = gi.record_by_addr("185.65.53.155")
#print str(res['latitude']) + "," + str(res['longitude'])

print IPFromCoord(args.lat, args.lon, 3)

