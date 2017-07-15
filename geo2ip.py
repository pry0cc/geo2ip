#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg
import csv
import argparse as ag
import math
import socket, struct

parser = ag.ArgumentParser(description="Find IP from GEO Location")
parser.add_argument('lat', type=float, help='latitude of target')
parser.add_argument('lon', type=float, help='longitude of target')

args = parser.parse_args()

def ips(start, end):
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

def simpleForm(val):
    # Take input as float.
    if str(val).split(".")[1] == "0":
        return str(int(val))
    else:
        return str(val)

def shortenIP(ip):
    result = ""
    octets = ip.split(".")[0:3]
    for octet in octets:
        if octets.index(octet) < 2:
            result += octet + "."
        else:
            result += octet + ".1"
    return result

def IPFromCoord(lat, lon):
    gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)
    cc = getCountryByCoord(lat,lon)
    results = IPFromCC(cc)

    try:
        for ip_range in results:
            ips_basic = []
            for ip in ips(ip_range[0], ip_range[1]):
                ips_basic.append(shortenIP(ip))

            for ip in sorted(set(ips_basic)):
                res = gi.record_by_addr(ip)
                ip_lat = str(float(math.floor(res["latitude"] * 1000) / 1000))
                ip_lon = str(float(math.floor(res["longitude"] * 1000) / 1000))
                
                if (str(lon) == "0.0") and (str(lat) == "0.0"):
                    # No Search filter, print everything
                    print shortenIP(ip)[:-1] + "0/24: " + ip_lat + ", " + ip_lon + " " + str(res["city"])
                else:
                    if (simpleForm(lat) in ip_lat) and (simpleForm(lon) in ip_lon):
                        print shortenIP(ip)[:-1] + "0/24: " + ip_lat + ", " + ip_lon + " " + str(res["city"])

    except Exception as e:
        print "ERROR: " + str(e)

print IPFromCoord(args.lat, args.lon)
