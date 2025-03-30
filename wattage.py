import sys
import os
sys.path.insert(0, os.path.abspath('Hardware-Monitor/'))
from HardwareLib import Linux_UPS_Prober 

temp = sys.stdout
sys.stdout = None
upsProber = Linux_UPS_Prober()
sys.stdout = temp
print(upsProber.get_current_load(), "Watts")
