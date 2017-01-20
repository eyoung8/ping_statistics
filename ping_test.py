#!/usr/bin/python
import subprocess
import os
from datetime import datetime
from time import time

ping_data = subprocess.check_output('ping -c 10 google.com', shell=True).decode('utf-8')
fname = str(datetime.now()) + ".txt"
internal_time = time()
path = os.path.join(os.path.abspath('ping'), fname)
with open(path, 'w') as f:
    f.write("time: " + str(internal_time) + "\n")
    f.write(ping_data)

traceroute_data = subprocess.check_output('traceroute google.com', shell=True).decode('utf-8')
path = os.path.join(os.path.abspath('traceroute'), fname)
with open(path, 'w') as f:
    f.write("time: " + str(internal_time) + "\n")
    f.write(traceroute_data)