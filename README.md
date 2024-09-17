# Security Automation Scripts

Python scripts for automating security tasks. Although I am not allowed to upload all the scripts due to academic policies, I am happy to share my work with you privately. 

## Scripts Overview

### Port Scanning Script:

Purpose: Automates the process of scanning network ports to identify open ports on a target system.

How it Works: Utilizes Python's networking libraries to send requests to specified IP addresses and ports, reporting back on their status.

### Brute Force SSH Script:

_Purpose:_ The script attempts to brute-force SSH login credentials by trying multiple passwords from a specified list against a target IP address and username.

_How it Works:_ Uses **paramiko** library, a target IP address, a username, and a password list to perform the attack. The target IP address, username, and password list must be provided.

### Log Manipulation Script:

_Purpose:_ The script searches through log files in the /var/log/ directory and removes all entries associated with a specified IP address

_How it Works:_ The script identifies log files containing a specified IP address in the ```/var/log/``` directory, reads each file to remove lines with the IP, and writes back the cleaned content, requiring root privileges to execute successfully

### VirusTotal API Integration Script:

_Purpose:_ Interfaces with the VirusTotal API to check files or URLs for potential threats.

_How it Works:_ Sends requests to the VirusTotal service through its API and processes the response to determine the safety of a given file or URL.
