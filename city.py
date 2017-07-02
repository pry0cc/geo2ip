#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg

gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)

res = gi.record_by_addr("185.65.53.155")
print res['longitude']
print res['latitude']

