#!/usr/bin/python2

import GeoIP

gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)

print gi.record_by_addr("10.10.10.10")

