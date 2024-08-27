####################
#Log manipulator
#
#This script will remove all logs associated with the given IP address in a Linux-based system. 
#This script will need root privileges to run successfully.
####################

import os, re
ip = "x.x.x.x" # replace the IP address 
#files that have the log 
files = os.popen("grep -rl \""+ip+"\" /var/log/ ").read().splitlines()

lines=[]
for file in files:
    with open(file, "r+") as f:
        lines = f.read().split()
        f.seek(0)
        f.truncate()
    with open(file,"w") as f:
        for line in lines:
            if ip not in line:
                f.write(line)
print("logs erased with ip "+ip)
