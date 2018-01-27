#!/usr/bin/env python

from urllib2 import Request, urlopen, URLError
import requests
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


url = raw_input('URL: ')
if 'http://' in url:
    pass
if 'https://' in url:
    pass
else:
    url = 'http://'+url

sleepfor = raw_input('Pull a request every x secounds\nTime interval: ')
if sleepfor <= 5:
    sleepfor = 5
else:
    sleepfor = sleepfor

def validate():
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


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get():
    response = requests.get(url, headers=headers)
    print(bcolors.OKGREEN)
    print("Status: %s") % (response.status_code)
    print(bcolors.ENDC)


validate()

while True:
    print('Get requests')
    get()
    print('Sleep for %s seconds') % (sleepfor)
    time.sleep(float(sleepfor))
