#!/usr/bin/env python2

import csv
import argparse as ag

parser = ag.ArgumentParser(description="Generate Masscan configuration files")
parser.add_argument("country", type=str, help="Country code to generate file for")

args = parser.parse_args()


conf = '''rate =  100000.00
randomize_hosts = true
output-format = xml
banners = true
show = open,,
ports = 0-65535
'''

conf += "output-filename = scan-" + args.country.split(".")[0] + ".xml\n"

try:
    for row in csv.reader(open(args.country)):
        conf += "range = " + row[0] + "-" + row[1] + "\n"
except:
    pass

conf += "excludefile = exclude.txt"

file = open("configs/"+args.country.split(".")[0]+".conf", "w")

for line in conf.split("\n"):
    file.write(line+"\n")

file.close
