#!/usr/bin/env python

import os
import time
import subprocess
import sys

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
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\nTry with $ sudo kalel")

# Check if setup is complete
def setup():
    if not os.path.isfile("/opt/KalEl/src/setupOK"):
        print("You must run setup.py first\n")
        ans1 = raw_input("Would you like to run setup now?\n y/n: ")
        if ans1 == "y":
            import setup
        else:
            exit(1)

# Get the version number:
def get_version():
    define_version = open("src/kalel.version", "r").read().rstrip()
    # define_version = '1.1.1'
    return define_version

define_version = get_version()
subprocess.Popen("rm version.lock", shell=True).wait()

def pullupdate(define_version):
    cv = get_version()

    # pull version
    try:
        version = ""

        def pull_version():
            if not os.path.isfile("version.lock"):
                try:

                    url = (
                        'https://raw.githubusercontent.com/noobscode/kalel/master/src/kalel.version')
                    version = urlopen(url).read().rstrip().decode('utf-8')
                    filewrite = open("version.lock", "w")
                    filewrite.write(version)
                    filewrite.close()

                except KeyboardInterrupt:
                    version = "keyboard interrupt"

            else:
                version = open("version.lock", "r").read()

            if cv != version:
                if version != "":
                    print("There is a new update available!")
            else:
                print("KalEl is up to date!")

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
        # pass

def logo():
    print(bcolors.OKBLUE + """
    __  ___      ___       __          _______  __
   |  |/  /     /   \     |  |        |   ____||  |
   |  '  /     /  ^  \    |  |        |  |__   |  |
   |    <     /  /_\  \   |  |        |   __|  |  |
   |  .  \   /  _____  \  |  `----.   |  |____ |  `----.
   |__|\__\ /__/     \__\ |_______|   |_______||_______|

    - Kal El Network Penetration Testing (""" + bcolors.WARNING + """KalEl NPT""" + bcolors.OKBLUE + """)
    - Created by:""" + bcolors.FAIL + """ NoobsCode """ + bcolors.OKBLUE + """ """ + bcolors.WARNING + """ """ + bcolors.OKBLUE + """
    - Version: """ + bcolors.OKGREEN + """%s""" % (define_version) + bcolors.WARNING + """ """), pullupdate(define_version)
    print("""    - Github: """ + bcolors.OKGREEN + """https://www.Github.com/NoobsCode/KalEl""" + bcolors.OKBLUE + """ """)
# initial user menu
def agreement():
    if not os.path.isfile("/opt/KalEl/src/agreement"):
        with open("LICENSE") as fileopen:
            for line in fileopen:
                print((line.rstrip()))

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
            choice = raw_input("\nDo you agree to the terms of service [y/n]: ")
            if choice == "y":
                with open("/opt/KalEl/src/agreement", "w") as filewrite:
                    filewrite.write("user accepted")
                    print(bcolors.ENDC)
            else:
                print(bcolors.ENDC + "[!] Exiting Kal El, have a nice day." + bcolors.ENDC)
                sys.exit()

#Header information Intro text
def intro():
    print(bcolors.HEADER + bcolors.BOLD + "\n Kal El is a neat tool for Network Stress Testing and Penetration Testing")
    print(" This toolkit is still a work in progress and is a very early build." + bcolors.ENDC)

# Create the main menu
def mainmenu():
    os.system('clear')
    agreement()
    os.system('clear')
    ans=True
    while ans:
        logo()
        intro()
        print ("""
        1.Traffic Spoof Attack # Force Redirect Network Traffic (DNS SPOOF)
        2.The Harvester        # Harvest Email, Vhosts, Subdomain names (more)
        3.Spoof Emails         # Send Fake Emails To And From Anyone
        4.Update KalEl         # Update The KalEl Toolkit
        5.Help/Tutorial
        6.Exit/Quit
        """)
        ans=raw_input("Choose Attack Vector: ")
        if ans=="1":
            os.system('clear')
            logo()
            import module.ettercap.spoof
        elif ans=="2":
            os.system('clear')
            logo()
            import module.harvester.prep
        elif ans=="3":
            os.system('clear')
            logo()
            import module.spoofmail.spoofmail
        elif ans=="4":
            print('Updating')
            update_kalel()
            #import module.ddos
        elif ans=="5":
            print("Visit out github at: https://github.com/noobscode/kalel")
        elif ans=="6":
            print("\n Goodbye")
            exit(1)
        elif ans !="":
            print("\n Not Valid Choice Try again")


#Check if we are running Kali Linux
def check_kali():
    if os.path.isfile("/etc/apt/sources.list"):
        kali = open("/etc/apt/sources.list", "r")
        kalidata = kali.read()
        if "kali" in kalidata:
            return "Kali"
        # if we aren't running kali
        else:
            return "Non-Kali"
    else:
        print("[!] Not running a Debian variant..")
        return "Non-Kali"

# KalEl Update
def update_kalel():
    kali = check_kali()
    if kali == "Kali":
        print("You are running Kali Linux")
        time.sleep(2)
        print("Performing Update Please Wait")
        print("Cleaning up...")
        subprocess.Popen("git clean -fd", shell=True).wait()
        print("Updating, please wait...")
        subprocess.Popen("git pull", shell=True).wait()
        # Create a symbolic link for launching the toolkit via usr/bin
        subprocess.Popen("ln -s /opt/KalEl/run.py /opt/KalEl/kalel", shell=True).wait()
        subprocess.Popen("ln -s /opt/KalEl/kalelupdate.py /opt/KalEl/kalelupdate", shell=True).wait()
        print("Update finished, returning to main menu.")
        time.sleep(2)

# Run the program
setup()
mainmenu()
#End
