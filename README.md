# Network Stress Test and Penetration Testing Toolkit
# Author: NoobsCode
```
__  ___      ___       __          _______  __
|  |/  /     /   \     |  |        |   ____||  |
|  '  /     /  ^  \    |  |        |  |__   |  |
|    <     /  /_\  \   |  |        |   __|  |  |
|  .  \   /  _____  \  |  `----.   |  |____ |  `----.
|__|\__\ /__/     \__\ |_______|   |_______||_______|

- Kal El Network Penetration Testing (KalEl NPT)
- Created by: NoobsCode   
- Version: 2.1  KalEl is up to date!
- Tor IP: 172.30.144.25
- Github: https://www.Github.com/NoobsCode/KalEl

Kal El is a neat tool for Network Stress Testing and Penetration Testing
This toolkit is still a work in progress and is a very early build.

    1.Traffic Spoof Attack # Force Redirect Network Traffic (DNS SPOOF)
    2.The Harvester        # Harvest Email, Vhosts, Subdomain names (more)
    3.Spoof Emails         # Send Fake Emails To And From Anyone
    4.Traffic Generator    # Generate Fake Visitor Stats on a webpage
    5.Activate Tor(VPN)    # Activate VPN For Anonymity To Hide Yourself
    9.Update KalEl         # Update The KalEl Toolkit
    10.Help/Tutorial
    99.Exit/Quit

Choose Attack Vector:  $
```
Supported OS:
-------------------
Tested on Ubuntu 14/17 and Kali Linux (Debian)


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
* Send fake emails to and from anyone. Also supports attachments.
-------------------
The Traffic Generator:
* Traffic Generator is a tool used to generate fake web traffic that can be used to fake page views and visitor stats. If used with TOR VPN module you will have the option to enable auto switching where it will get a new IP for each request resulting in unique visitor stats as well as page views.
-------------------
KalElVPN Module (Tor VPN):
* The VPN module included in this tool have three simple functions

  - Start/stop, The VPN module can also be used outside the toolkit
    for encrypting your network traffic and

  - Switch, Allows you to request a new IP address at any time.
    Can be used as many times as you wish.

(More attack vectors will be available with updates)

Technical Information:
-------------------------------
* Written in Python

Requirements:
* Python
* PIP
* Stem
* Requests
* Tor
* SendEmail
* ettercap-text-only


Support This Project
--------------------
  Visit us at
  -----------
* https://github.com/noobscode
