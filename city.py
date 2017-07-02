#!/usr/bin/python2

import GeoIP
import reverse_geocoder as rg

gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)

print gi.record_by_addr("123.45.23.14")

