#!/usr/bin/python3

import sys
import time
import argparse
import os
sys.path.insert(0, os.path.abspath('Hardware-Monitor/'))
from HardwareLib import Linux_UPS_Prober

parser = argparse.ArgumentParser(description="Get Wattage from system.")
parser.add_argument('-m', '--monitor', action='store_true', help="Enable monitoring mode")
args = parser.parse_args()

temp = sys.stdout
sys.stdout = None
upsProber = Linux_UPS_Prober()
sys.stdout = temp
while args.monitor:
    try:
        print(upsProber.get_current_load(), "Watts", end='\r')
        time.sleep(1)
    except KeyboardInterrupt:
        break
print(upsProber.get_current_load(), "Watts")
