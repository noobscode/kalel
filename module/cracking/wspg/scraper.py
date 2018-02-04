#!/usr/bin/env python

import os, sys
import requests
import subprocess
from bs4 import BeautifulSoup


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Header info
def wspgintro():
    print(bcolors.WARNING + """
    This tool pulls all the link from given domain and then
    scrapes it clean for all words generating a wordlist for
    you to use as a wordlist for password cracking
    (Dictionary attack)\n""" + bcolors.ENDC)


# Run The wordlist generator from core.py
def runprogram():
    print('\nRunning Wordlist Generator')
    subprocess.Popen('python module/cracking/wspg/core.py', shell=True).wait()


# Define the URL to start pulling links from
def geturl():
    url = raw_input(bcolors.OKGREEN + '\nBase URL to start Harvest\nURL: ' + bcolors.ENDC)
    if 'http://' in url:
        pass
    if 'https://' in url:
        pass
    else:
        url = 'http://'+url

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    soup.prettify()

    for link in soup.find_all('a'):
        if 'http' in (link.get('href')):
            if url in (link.get('href')):
                with open('module/cracking/wspg/sites.scrape', 'a') as f:
                    f.write(link.get('href')+"\n")
                    f.flush()
                    f.close()
        else:
            pass

# Run main program
if __name__ == "__main__":
    try:
        wspgintro()
        geturl()
        runprogram()
    except KeyboardInterrupt:
        sys.exit()
