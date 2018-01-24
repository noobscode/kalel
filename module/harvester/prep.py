#!/usr/bin/env python

import os
import subprocess


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def harvester():
    print bcolors.OKBLUE + """
    The Harvester is a tool for gathering e-mail accounts,
    subdomain names, virtual hosts, open ports/ banners,
    and employee names from different public sources
    (search engines and servers).

    - Inspired by edge-security Author: Christian Martorella
    - https://github.com/laramies/theHarvester \n""" + bcolors.ENDC

    domain = raw_input('Domain to harvest from\nDomain: ')
    os.system('module/harvester/engine.py -d %s -b all' % domain)

    raw_input('Press [ENTER] to go to main menu')


try:
    harvester()
except KeyboardInterrupt:
    print("\n\nDon't forget your cat!\n")
finally:
    subprocess.call(['kalel'])
