#!/usr/bin/env python
import requests
import time

def get():
    r=requests.get("URL", headers={"content-type":"text"});

while True:
    get()
    time.sleep(1)
