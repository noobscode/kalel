#!/usr/bin/env python
from __future__ import print_function
import os
import time
import subprocess
import sys
from builtins import input
import webbrowser


# python 2 and 3 compatibility
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import multiprocessing


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


# Check if setup is complete
def dosetup():
    if not os.path.isfile("/opt/KalEl/src/setupOK"):
        print("You must run setup.py first\n")
        ans1 = input("Would you like to run setup now?\n y/n: ")
        if ans1 == "y":
            os.system('sudo -H python setup.py install')
        else:
            sys.exit()

# Kaldir used in the pullupdate function:
kaldir = '/opt/KalEl/.kal'


# Get the version number:
def get_version():
    define_version = open("src/kalel.version", "r").read().rstrip()
    # define_version = '1.1.1'
    return define_version


define_version = get_version()


# Get version number from github
def pullupdate(define_version):
    cv = get_version()

    # pull version
    try:
        def pull_version():
            if not os.path.isfile(kaldir + "/version.lock"):
                try:
                    url = (
                        'https://raw.githubusercontent.com/noobscode/kalel/master/src/kalel.version')
                    version = urlopen(url).read().rstrip().decode('utf-8')
                    filewrite = open(kaldir + "/version.lock", "w")
                    filewrite.write(version)
                    filewrite.close()

                except KeyboardInterrupt:
                    version = "keyboard interrupt"
            else:
                version = open(kaldir + "/version.lock", "r").read()

            if cv != version:
                print(bcolors.FAIL + '      - Version: %s'%(define_version) + bcolors.ENDC),
                print(bcolors.WARNING + "   ! There is a new update available!" + bcolors.ENDC)
            else:
                print(bcolors.OKGREEN + '   - Version: %s'%(define_version) + bcolors.ENDC),
                print(bcolors.OKGREEN + "     KalEl is up to date!" + bcolors.ENDC)

        # Pull the version from out git repo
        p = multiprocessing.Process(target=pull_version)
        p.start()

        # Wait for 5 seconds or until process finishes
        p.join(8)

        # If thread is still active
        if p.is_alive():
            print(
                bcolors.FAIL + " Unable to check for new version are you connected to the internet?\n" + bcolors.ENDC)
            # terminate the process
            p.terminate()
            p.join()

    except Exception as err:
        print(err)
        pass


# Pull the TOR IP/Status Section
def getip():
    torip = open("module/tor/tor.ip", "r").read().rstrip()
    return torip

torip = getip()


# Main Logo and header
def logo():
    print(bcolors.OKBLUE + """\
    __  ___      ___       __          _______  __
   |  |/  /     /   \     |  |        |   ____||  |
   |  '  /     /  ^  \    |  |        |  |__   |  |
   |    <     /  /_\  \   |  |        |   __|  |  |
   |  .  \   /  _____  \  |  `----.   |  |____ |  `----.
   |__|\__\ /__/     \__\ |_______|   |_______||_______| """ + bcolors.ENDC)
    print('\n')
    print(bcolors.OKGREEN + '   - Kal El Network Penetration Testing' + bcolors.ENDC)
    print(bcolors.FAIL + '   - Created by NoobsCode' + bcolors.ENDC)
    print(bcolors.WARNING + '   - Github: https://github.com/noobscode' + bcolors.ENDC)
    print('   - Tor IP: %s' % (torip))
    print('%s' % (pullupdate(define_version)))



# initial user menu
def agreement():
    if not os.path.isfile("/opt/KalEl/src/agreement"):
        with open("LICENSE") as fileopen:
            for line in fileopen:
                print((line.rstrip()))
                print('\n')

            print("{0}Kal El is designed purely"
                  " for good and not evil. If you are planning on "
                  "using this tool for malicious purposes that are "
                  "not authorized by the company you are performing "
                  "assessments for, you are violating the terms of "
                  "service and license of this toolset. By hitting "
                  "yes (only one time), you agree to the terms of "
                  "service and that you will only use this tool for "
                  "lawful purposes only.{1}".format(bcolors.FAIL, bcolors.ENDC))
            print(bcolors.OKGREEN)
            choice = input("\nDo you agree to the terms of service [y/n]: ")
            if choice == "y":
                with open("/opt/KalEl/src/agreement", "w") as filewrite:
                    filewrite.write("user accepted")
                    print(bcolors.ENDC)
            else:
                print(bcolors.ENDC + "[!] Exiting Kal El, have a nice day." + bcolors.ENDC)
                sys.exit()


# Helper function for Pawned.
def impowned():
    rp = open("module/cracking/pawned/README.md","r")
    print (bcolors.OKBLUE + rp.read() + bcolors.ENDC)
    print(bcolors.WARNING + '\nSpecial thanks to: D4Vinci' + bcolors.ENDC)
    print('Github: https://github.com/D4Vinci')
    print('\n')
    pawneduser = input('Email or Username to Scan: ')
    pwnd = ('module/cracking/pawned/pawned.py -api2 -q %s')%(pawneduser)
    os.system(pwnd)



# Just something to prevent some scripts to fly away.
def goon():
    input(bcolors.OKGREEN + 'Press [ENTER] to continue...' + bcolors.ENDC)


# Header information Intro text
def intro():
    print(bcolors.HEADER + bcolors.BOLD + "\n Kal El is a neat tool for Network Stress Testing and Penetration Testing")
    print(" This toolkit is still a work in progress and is a very early build." + bcolors.ENDC)


# Create the main menu
def mainmenu():
    os.system('clear')
    agreement()
    os.system('clear')
    ans = True
    while ans:
        logo()
        intro()
        print ("""
        1.Traffic Spoofing     # Force Redirect Network Traffic (DNS SPOOF)
        2.The Harvester        # Harvest Emails, Vhosts, Subdomain names (more)
        3.Spoof Emails         # Send Fake Emails To And From Anyone
        4.Traffic Generator    # Generate Fake Visitor Stats on a webpage
        5.Activate Tor(VPN)    # Activate VPN For Anonymity To Hide Yourself
        6.Cracking Tools       # Password Related Attacks

        9.Update KalEl         # Update The KalEl Toolkit
        10.Help/Tutorial
        99.Exit/Quit
        """)
        ans = input("Choose Attack Vector: ")
        if ans == "1":
            os.system('clear')
            logo()
            os.system('module/ettercap/spoof.py')
        elif ans == "2":
            os.system('clear')
            logo()
            os.system('module/harvester/prep.py')
        elif ans == "3":
            os.system('clear')
            logo()
            os.system('module/spoofmail/spoofmail.py')
        elif ans == "4":
            os.system('clear')
            logo()
            os.system('module/trafficgen/getheader.py')
        elif ans == "5":
            submenu_tor()
        elif ans == "6":
            submenu_cracking()
        elif ans == "9":
            print('Updating')
            update_kalel()
        elif ans == "10":
            print(bcolors.WARNING + '\nIf you have any issues you can open an issue on github' + bcolors.ENDC)
            print(bcolors.FAIL + 'https://github.com/noobscode/kalel/issues' + bcolors.ENDC)
            print(bcolors.OKGREEN + '\nFor guides and tutorials go to: ' + bcolors.ENDC),
            print(bcolors.FAIL + 'https://noobscode.github.io/kalel\n' + bcolors.ENDC)
            goon()
        elif ans == "99":
            print("\n Goodbye")
            sys.exit()
        elif ans != "":
            print("\n Not Valid Choice Try again")


# Create the submenu for tor
def submenu_tor():
    os.system('clear')
    ans = True
    while ans:
        logo()
        intro()
        print ("""
        1.Start TOR VPN        # Start TOR VPN
        2.Stop TOR VPN         # Stop TOR VPN
        3.Switch IP (Renew)    # Request new IP address

        99.Back to main menu
        """)
        ans = input("Choose Action: ")
        if ans == "1":
            os.system('module/tor/tor.py start')
        elif ans == "2":
            os.system('module/tor/tor.py stop')
        elif ans == "3":
            os.system('module/tor/tor.py switch')
        elif ans == "99":
            mainmenu()
        elif ans != "":
            print("\n Not Valid Choice Try again")


# Create the submenu for cracking
def submenu_cracking():
    os.system('clear')
    ans = True
    while ans:
        logo()
        intro()
        print ("""
        1.Hash Buster        # Tool for Cracking MD5|SHA1|SHA2 Hashes
        -----------------------------------------------------------------
        2.Pawned             # Check if an email have been hacked.
                               Then use the credentials and try to
                               auto-login to services like facebook etc.
        -----------------------------------------------------------------
        3.Wordlist Generator # Scrapes all the words from a specified
                               domain to generate a wordlist for use in
                               a dictionary password attack.

        99.Back to main menu
        """)
        ans = input("Choose Action: ")
        if ans == "1":
            os.system('clear')
            logo()
            os.system('module/cracking/hashbuster/hashbuster.py')
        if ans == "2":
            os.system('clear')
            logo()
            impowned()
        if ans == "3":
            os.system('clear')
            logo()
            subprocess.Popen('python module/cracking/wspg/scraper.py', shell=True).wait()
            #os.system('module/cracking/web_scrape_pwd_gen/scraper.py')
        elif ans == "99":
            mainmenu()
        elif ans != "":
            print("\n Not Valid Choice Try again")

# KalEl Update
def update_kalel():
    if os.getcwd() == '/opt/KalEl':
        pass
    else:
        print(bcolors.FAIL + '\nYou are not in KalEl Directory!\n' + bcolors.ENDC)
        print(bcolors.WARNING + 'Please run KalEl from /opt/KalEl/\n' + bcolors.ENDC)
        time.sleep(2)
        mainmenu()

    print("Performing Update Please Wait")
    print("Cleaning up...")
    subprocess.Popen("git clean -fd", shell=True).wait()
    print("Updating, please wait...")
    subprocess.Popen("git fetch origin master", shell=True).wait()
    subprocess.Popen("git reset --hard FETCH_HEAD", shell=True).wait()
    subprocess.Popen("mkdir /opt/KalEl/.kal", shell=True).wait()

    # Create a symbolic link for launching the toolkit via usr/bin
    subprocess.Popen("ln -s /opt/KalEl/run.py /opt/KalEl/kalel", shell=True).wait()

    # Set symlinks
    import setup.setlinks

    # Fix permissions
    import setup.fixpermissions

    print("Update finished, You need to manually start kalel again")
    goon()
    sys.exit()
    time.sleep(2)


def cleanup():
    #if os.path.isfile(kaldir + '/version.lock'):
        #os.remove(kaldir + '/version.lock')
    if torip != 'VPN Disabled':
        print('NB: Tor is still running!')
        print('You can shut it down manually by typing\n$ sudo kalelvpn stop')


# Run the program
try:
    dosetup()
    mainmenu()
except KeyboardInterrupt:
    print("\n\nDon't forget your cat!\n")
# End
