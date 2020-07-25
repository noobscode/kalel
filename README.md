# Network Stress Test and Penetration Testing Toolkit
# Author: NoobsCode
```
__  ___      ___       __          _______  __
|  |/  /     /   \     |  |        |   ____||  |
|  '  /     /  ^  \    |  |        |  |__   |  |
|    <     /  /_\  \   |  |        |   __|  |  |
|  .  \   /  _____  \  |  `----.   |  |____ |  `----.
|__|\__\ /__/     \__\ |_______|   |_______||_______|

- Kal El Network Penetration Testing
- Created by NoobsCode
- Github: https://github.com/noobscode
- Tor IP: 51.129.43.104
- Version: x.x KalEl is up to date!

Kal El is a neat tool for Network Stress Testing and Penetration Testing
This toolkit is still a work in progress and is a very early build.

    1.Traffic Spoofing     # Force Redirect Network Traffic (DNS SPOOF)
    2.The Harvester        # Harvest Emails, Vhosts, Subdomain names (more)
    3.Spoof Emails         # Send Fake Emails To And From Anyone
    4.Traffic Generator    # Generate Fake Visitor Stats on a webpage
    5.Activate Tor(VPN)    # Activate VPN For Anonymity To Hide Yourself
    6.Cracking Tools       # Password Related Attacks

    9.Update KalEl         # Update The KalEl Toolkit
    10.Help/Tutorial
    99.Exit/Quit

Choose Attack Vector:  $
```
Supported OS:
-------------------
Tested on Ubuntu 14/17, Kali Linux, Parrot Security OS and Debian 9.

How to install:
-------------------
``$ git clone https://github.com/noobscode/KalEl``

``$ cd kalel/``

``$ sudo -H python setup.py install``

How to Run KalEl:
-------------------
``$ sudo kalel``

How to uninstall:
-------------------
``$ sudo setup.py uninstall``


# Attack Vectors:
-------------------
DNS Spoof Module:
* DNS Spoof Attack Vector that allow you to force redirect network traffic.
-------------------
The Harvester:
* The Harvester is a tool for gathering e-mail accounts, subdomain names, virtual hosts, open ports/ banners, and employee names from different public sources (search engines and servers).
-------------------
SendEmail:
* Send fake emails to and from anyone. Also supports attachments, plain or HTML.
  Specify a HTML file to use a template.
-------------------
The Traffic Generator:
* Traffic Generator is a tool used to generate fake web traffic that can be used   to fake page views and visitor stats. If used with TOR VPN module you will have the option to enable auto switching where it will get a new IP for each request resulting in unique visitor stats as well as page views.
-------------------
KalElVPN Module (Tor VPN):
* The VPN module included in this tool have three simple functions

  - Start/stop, The VPN module can also be used outside the toolkit
    for encrypting your network traffic and

  - Switch, Allows you to request a new IP address at any time.
    Can be used as many times as you wish.
-------------------
HashBuster:
* Tool for Cracking MD5|SHA1|SHA2 Hashes
-------------------
Pwned:
* Check if an email have been hacked. It uses haveibeenpwned v3 api to test email accounts and tries to find the password in Pastebin Dumps.
-------------------
Web-Scraper Password Generator:
* This tool pulls all the link from a given domain and then
  scrapes all the words, generating a wordlist for you to use as a wordlist for password cracking (Dictionary attack).
  This is very usefull if you have issues finding a wordlist with a uncommon language, we all wish rockyou and realuniq came in our language right?
-------------------
(More attack vectors will be available with updates)

Technical Information:
-------------------------------
* Written in Python

Requirements:
* Python
** PIP
** Stem
** Requests
** future
** pwnedpasswords
** wheel

* Application/Scripts
** Tor
** SendEmail
** ettercap-text-only

Support This Project
--------------------
  Visit us at
  -----------
* https://github.com/noobscode
