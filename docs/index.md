---
layout: default
---



Kal El is a neat tool for Network Stress Testing and Penetration Testing.

This toolkit is still a work in progress and is still in the BETA fase.

### ***KalEl CAN BE HARMFUL IF NOT USED WITH CAUTION! IT IS NOT DESIGNED FOR MALICIOUS USE AND IS PERMITTED BY LAW!***


## Supported OS:

Tested on Ubuntu 14/17 and Kali Linux (Debian)


## How to install:
```
$ git clone https://github.com/noobscode/KalEl

$ cd kalel/

$ sudo -H python setup.py install
```
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/1-get.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/2-install.png)

## How to Run KalEl:
```
$ sudo kalel
```
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/3-menu.png)

## How to uninstall:
```
$ sudo setup.py uninstall
```


# Attack Vectors:

## DNS Spoof Module:
DNS Spoof Attack Vector that allow you to force redirect network traffic.
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/4-dns-spoof.png)

## The Harvester:
The Harvester is a tool for gathering e-mail accounts, subdomain names, virtual hosts, open ports/ banners, and employee names from different public sources (search engines and servers).
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/5-harvester.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/5-harvester1.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/5-harvester2.png)

## SendEmail:
Send fake emails to and from anyone. Also supports attachments.
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/6-mailspoof.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/6-mailspoof-example.png)

## The Traffic Generator:
Traffic Generator is a tool used to generate fake web traffic that can be used to fake page views and visitor stats. If used with TOR VPN module you will have the option to enable auto switching where it will get a new IP for each request resulting in unique visitor stats as well as page views.
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/7-tg1.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/7-tg2.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/7-tg3.png)
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/7-tg4.png)

## KalElVPN Module (Tor VPN):

The VPN module included in this tool have three simple functions

  - Start/stop, The VPN module can also be used outside the toolkit
    for encrypting your network traffic and

  - Switch, Allows you to request a new IP address at any time.
    Can be used as many times as you wish.

![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/8-tor.png)

## Password Cracker (MD5, SHA1 and SHA2):
![](https://github.com/noobscode/kalel/raw/master/docs/assets/images/9-md5.png)

### (More attack vectors will be available with updates)

## Technical Information:

* Written in Python

## Requirements:
* Python
* PIP
* Stem
* Requests
* Tor
* SendEmail
* ettercap-text-only


# Support This Project
--------------------
  Visit us at
  -----------
* https://github.com/noobscode
