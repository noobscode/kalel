#!/usr/bin/env python

import os
import time
import subprocess
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def setup():
    if not os.path.isfile("src/setupOK"):
        print("You must run setup.py first\n")
        ans1 = raw_input("Would you like to run setup now?\n y/n: ")
        if ans1 == "y":
            import setup
        else:
            exit(1)

def logo():
    print """
 __  ___      ___       __          _______  __
|  |/  /     /   \     |  |        |   ____||  |
|  '  /     /  ^  \    |  |        |  |__   |  |
|    <     /  /_\  \   |  |        |   __|  |  |
|  .  \   /  _____  \  |  `----.   |  |____ |  `----.
|__|\__\ /__/     \__\ |_______|   |_______||_______|
                                                     """

# initial user menu
def agreement():
    if not os.path.isfile("src/agreement"):
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
                with open("src/agreement", "w") as filewrite:
                    filewrite.write("user accepted")
                    print(bcolors.ENDC)
            else:
                print(bcolors.ENDC + "[!] Exiting Kal El, have a nice day." + bcolors.ENDC)
                sys.exit()

#Header information Intro text
def intro():
    print bcolors.HEADER + bcolors.BOLD
    print("Kal El is a neat tool for Network Stress Testing and Penetration Testing")
    print("This toolkit is still a work in progress and is a very early build.")
    print bcolors.ENDC

def mainmenu():
    os.system('clear')
    agreement()
    os.system('clear')
    logo()
    intro()
    ans=True
    while ans:
        print ("""
        1.Traffic Spoof Attack # Force Redirect Network Traffic
        2.The Harvester        # Harvest Email, Vhosts, Subdomain names (more)
        3.Spoof Emails         # Send Fake Emails To And From Anyone
        4.Not in use
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
            print('Not in use yet')
            #import module.ddos
        elif ans=="5":
            print("Visit out github at: https://github.com/noobscode/kalel")
        elif ans=="6":
            print("\n Goodbye")
            exit(1)
        elif ans !="":
            print("\n Not Valid Choice Try again")
setup()
mainmenu()
#End
