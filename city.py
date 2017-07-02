#!/usr/bin/python2

import GeoIP

gi = GeoIP.open("GeoLiteCity.dat", GeoIP.GEOIP_STANDARD)

res = gi.record_by_addr("185.65.53.155")
print str(res['latitude']) + "," + str(res['longitude'])

