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

print bcolors.OKBLUE + """
The Harvester is a tool for gathering e-mail accounts,
subdomain names, virtual hosts, open ports/ banners,
and employee names from different public sources
(search engines and servers).

- Inspired by edge-security author Christian Martorella
- https://github.com/laramies/theHarvester \n""" + bcolors.ENDC

domain = raw_input('Domain to harvest from\nDomain: ')
os.system('module/harvester/engine.py -d %s -b all' % domain)

backtomen = raw_input('Press [ENTER] to go to main menu')
if backtomen != (''):
    mainmenu()
