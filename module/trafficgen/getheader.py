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



sleepfor = raw_input('Pull a request every x secounds\nTime interval: ')
if sleepfor <= 5:
    sleepfor = 5
else:
    sleepfor = sleepfor

usetor = raw_input('Do you want to use Tor and switch ip for each request?\nThis will give you uniqe visitor starts. y/n: ')
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

def getip():
    running = open("module/tor/tor.ip", "r").read().rstrip()
    return running
    if running != 'VPN Disabled':
        print(bcolors.FAIL + 'Pulling a new IP from Tor' + bcolors.ENDC)
        os.system('module/tor/tor.py switch')
    else:
        pass


while True:
    print('\nGet requests')
    getreq()
    getip()
    print('Sleep for %s seconds') % (sleepfor)
    time.sleep(float(sleepfor))


print('Stopping VPN')
os.system('module/tor/tor.py stop')
