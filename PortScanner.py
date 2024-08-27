####################
#Network Port Scanner
#
#This script will scan the given ip address and ports and tell if the ports are open or not. 
#This script can also read the list of ips and ports from a ".txt" file. Ensure to name them "ips.txt" and "ports.txt" respectively.
####################

import socket
from scapy.all import *

def TCPScan(ips,ports):   
    #TCP
    for ip in ips:
        for port in ports:
            
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    if s.connect_ex((ip,port)) == 0:
                        print(f'TCP Socket {ip}:{port} is open')
                    else:
                        print(f'TCP port {port} on ip {ip} is closed')                
                except Exception as e:
                    print(f"Error {e} occured while Scanning TCP port {port} on {ip}.")
                

def UDPScan(ips,ports):
    #UDP
    for ip in ips:
        print(f"Scanning UDP ports on IP: {ip}")
        for port in ports:
            try:
                udppacket = sr1(IP(dst=ip)/UDP(port=port),timeout=2)
                if udppacket == None :
                    print(f" UDP socket {ip}:{port} is open or filtered.")
                elif udppacket.haslayer(ICMP):
                    print(f" UDP port {port} on ip {ip} is closed")
                elif udppacket.haslayer(UDP):
                    print(f" UDP socket {ip}:{port} is open.")

            except Exception as e:
                    print(f"Error {e} occured while Scanning UDP port {port} on {ip}.")
ips = []            
ports = []


while True:
    user_input = input("Please enter IPs, one per line.  If list of ips, enter LIST. End with quit. ")
    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "list":
        with open('ips.txt','r') as f:
            ip_list = f.readlines()
        for ip in ip_list:
            ips.append(ip.strip())
        break
    else:      
        ips.append(user_input)

while True:
    user_input = input("Please enter ports, one per line. If list of ports, enter LIST. End with quit. ")
    if user_input.lower() == "quit":
        break
    elif user_input.lower() == "list":
        with open('ports.txt','r') as f:
            port_list = f.readlines()
        for port in port_list:
            ports.append(port.strip())
        break
    else:
        ports.append(int(user_input))


TCPScan(ips, ports)
UDPScan(ips,ports)