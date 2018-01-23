#!/usr/bin/env python


import os
import sys
import commands
from commands import getoutput
import time
import signal
from stem import Signal
from stem.control import Controller


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def logo():
    return


def usage():
    return


def t():
    current_time = time.localtime()
    ctime = time.strftime('%H:%M:%S', current_time)
    return "[" + ctime + "]"


def shutdown():
    print('bcolors.BGRED + bcolors.WHITE + t() + "[info] shutting down torghost" + bcolors.ENDC +"\n\n"')
    sys.exit()


def sigint_handler(signum, frame):
    print('\n user interrupt ! shutting down')
    shutdown()


def ip():
    while True:
        try:
            ipadd = commands.getstatusoutput('wget -qO- https://check.torproject.org | grep -Po "(?<=strong>)[\d\.]+(?=</strong)"')
        except :
            continue
        break
    return ipadd[1]


signal.signal(signal.SIGINT, sigint_handler)

TorrcCfgString = """

##/////ADDED BY TORGHOST ///
VirtualAddrNetwork 10.0.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 53
ControlPort 9051


"""

resolvString = "nameserver 127.0.0.1"

Torrc = "/etc/tor/torrc"
resolv = "/etc/resolv.conf"


def start_torghost():

    if TorrcCfgString in open(Torrc).read():
        print t()+" Torrc file already configured"
    else:

        with open(Torrc, "a") as myfile:

            myfile.write(TorrcCfgString)
            print bcolors.GREEN+"[done]"+bcolors.ENDC
    if resolvString in open(resolv).read():
        print t()+" DNS resolv.conf file already configured"
    else:
        with open(resolv, "w") as myfile:
            print t()+" Configuring DNS resolv.conf file.. ",
            myfile.write(resolvString)
            print bcolors.GREEN+"[done]"+bcolors.ENDC

    print t()+" Starting tor service.. ",
    os.system("service tor start")
    print bcolors.GREEN+"[done]"+bcolors.ENDC
    print t()+" setting up iptables rules",

    iptables_rules = """
    NON_TOR="192.168.1.0/24 192.168.0.0/24"
    TOR_UID=%s
    TRANS_PORT="9040"

    iptables -F
    iptables -t nat -F

    iptables -t nat -A OUTPUT -m owner --uid-owner $TOR_UID -j RETURN
    iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 53
    for NET in $NON_TOR 127.0.0.0/9 127.128.0.0/10; do
    iptables -t nat -A OUTPUT -d $NET -j RETURN
    done
    iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT

    iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    for NET in $NON_TOR 127.0.0.0/8; do
    iptables -A OUTPUT -d $NET -j ACCEPT
    done
    iptables -A OUTPUT -m owner --uid-owner $TOR_UID -j ACCEPT
    iptables -A OUTPUT -j REJECT
    """ % (getoutput("id -ur debian-tor"))

    os.system(iptables_rules)
    print bcolors.GREEN+"[done]"+bcolors.ENDC
    print t()+" Fetching current IP..."
    print t()+" CURRENT IP : "+bcolors.GREEN+ip()+bcolors.ENDC
    f = open('module/tor/tor.ip', 'w')
    f.write(ip())
    f.close()


def stop_torghost():
    print bcolors.RED+t()+"STOPPING torghost"+bcolors.ENDC
    print t()+" Flushing iptables, resetting to default",
    IpFlush = """
    iptables -P INPUT ACCEPT
    iptables -P FORWARD ACCEPT
    iptables -P OUTPUT ACCEPT
    iptables -t nat -F
    iptables -t mangle -F
    iptables -F
    iptables -X
    """
    os.system(IpFlush)
    f = open('module/tor/tor.ip', 'w')
    f.write('VPN Disabled')
    f.close()

    print bcolors.GREEN+"[done]"+bcolors.ENDC
    print t()+" Restarting Network manager",
    os.system("service network-manager restart")
    print bcolors.GREEN+"[done]"+bcolors.ENDC
    print t()+" Fetching current IP..."
    print t()+" CURRENT IP : "+bcolors.GREEN+ip()+bcolors.ENDC


def switch_tor():
    print t()+" Please wait..."
    time.sleep(7)
    print t()+" Requesting new circuit...",
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    print bcolors.GREEN+"[done]"+bcolors.ENDC
    print t()+" Fetching current IP..."
    print t()+" CURRENT IP : "+bcolors.GREEN+ip()+bcolors.ENDC
    f = open('module/tor/tor.ip', 'w')
    f.write(ip())
    f.close()


def tor():
    running = open("module/tor/tor.ip", "r").read().rstrip()
    return running


running = tor()


def torstatus():
    if running != '0':
        print('is running')
        stoptor = raw_input('Stop Tor VPN?\n y/n: ')
        if stoptor == 'y':
            stop_torghost()
    else:
        print('not running')
        starttor = raw_input('Start Tor VPN?\n y/n: ')
        if starttor == 'y':
            start_torghost()


arg = sys.argv[1:]


if len(arg) != 1:
    torstatus()
elif sys.argv[1] == "start":
    logo()
    start_torghost()
elif sys.argv[1] == "stop":
    logo()
    stop_torghost()
elif sys.argv[1] == "switch":
    switch_tor()
else:
    torstatus()
