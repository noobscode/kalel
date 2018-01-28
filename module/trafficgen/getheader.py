#!/usr/bin/env python

from urllib2 import Request, urlopen, URLError
import requests
import time
import subprocess
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Make sure Tool is run via sudo or by root
if not os.geteuid() == 0:
    sys.exit(bcolors.FAIL + "\nOnly root can run this script\nTry with $ sudo kalel" + bcolors.ENDC)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
print('\n')
print('Traffic Generator is a tool used to generate fake web traffic \nthat can be used to fake page views and visitor stats.')
print(bcolors.WARNING + '\nIf used with TOR VPN module you will get a new \nIP for each request resulting in unique visitor stats as well' + bcolors.ENDC)
print('\n')

url = raw_input('URL: ')
if 'http://' in url:
    pass
if 'https://' in url:
    pass
else:
    url = 'http://'+url
req = Request(url)

try:
    print('Validating URL...')
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    print('URL is valid')



sleepfor = raw_input('\nPull a request every x secounds\nTime interval: ')
if sleepfor <= 5:
    sleepfor = 5
else:
    sleepfor = sleepfor

usetor = raw_input('\nDo you want to activate VPN? (Required for IP Switching!) y/n: ')
if usetor == 'y':
    print('Starting kalelVPN module (TOR)')
    os.system('module/tor/tor.py start')
else:
    pass


def getreq():
    response = requests.get(url, headers=headers)
    print(bcolors.OKGREEN),
    print("Status: %s") % (response.status_code),
    print(bcolors.ENDC)


def runtraffic():
    while True:
        print('\nSENDING GET REQUESTS')
        getreq()
        print('Sleep for %s seconds') % (sleepfor)
        time.sleep(float(sleepfor))

def runtrafficsw():
    while True:
        print('\nSENDING GET REQUESTS')
        getreq()
        print(bcolors.FAIL + 'Pulling a new IP from Tor' + bcolors.ENDC)
        os.system('module/tor/tor.py switch')
        print('Sleep for %s seconds') % (sleepfor)
        time.sleep(float(sleepfor))


try:
    switchon = raw_input('\nDo you want to use Tor to switch ip for each request?\nThis will potentially give you unique visitor starts. y/n: ')
    if switchon == 'y':
        print(bcolors.OKGREEN + '\nGenerating traffic with IP Switching.....' + bcolors.ENDC)
        runtrafficsw()
    else:
        print(bcolors.OKGREEN + '\nGenerating traffic.....' + bcolors.ENDC)
        runtraffic()
except KeyboardInterrupt:
    print(bcolors.FAIL + 'Stopping VPN' + bcolors.ENDC)
    os.system('module/tor/tor.py stop')
    print(bcolors.OKGREEN + 'VPN Disabled!' + bcolors.ENDC)
    time.sleep(2)
