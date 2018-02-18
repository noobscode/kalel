#!/usr/bin/env python

import subprocess
import sys
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


def spoofemail():

    # Write SMTP server to config file
    def writetoconf():
        with open("src/config.py", "a") as filewrite:
            filewrite.write("\n#[SPOOFMAIL]\n")
            filewrite.write("smtpserver")
            filewrite.write(" = ")
            filewrite.write("'%s'\n" % smtpserver)

    # SPOOFMAIL Header
    print(bcolors.HEADER + "\n      SpoofMail is a tool to send fake emails to and from anyone." + bcolors.ENDC)
    print(bcolors.OKGREEN + """
    In order for spoofmail to work we need to use an open smtp relay server.
    Its recomended to use your own smtp server from example: your ISP.
    If you are not sure how to find your ISP's smtp server you can let kalel
    try and use some free and open smtp servers on the internet\n    but it might not work.\n""" + bcolors.ENDC)

    # Check if SMTP server is defined in src/config
    try:
        from src.config import smtpserver
        print('SMTP Server is manually set in src/conf.py\n')
    except ImportError:
        usecustom = raw_input('Use a custom SMTP server? (RECOMENDED!)\n y/n: ')
        if usecustom == ('y'):
            smtpserver = raw_input('Enter your smtp server:\n Server: ')
            # If you want to write smtp server as static to config file, uncheck this function.
            # writetoconf()
        else:
            smtpserver = ''
            print('Letting Kalel decide smtp server\nServer: %s' % smtpserver)

    # Input variables to use when performing action
    print(bcolors.WARNING + '\nTarget email examples:' + bcolors.ENDC)
    print('Example 1: single@target.com')
    print('Example 2: first@target.com, second@target.com')

    print(bcolors.WARNING + '\nYou can also use -cc | -bcc' + bcolors.ENDC)
    print('Example 3: first@target.com -cc second@target.com')

    toemail = raw_input('\nTarget email: ')
    fromemail = raw_input('\nSender email: ')
    subject = raw_input('\nSubject: ')
    print('\n')
    predefined = raw_input(bcolors.WARNING + 'Use a predefined template from a txt or html file?\ny/n: ' + bcolors.ENDC)
    if predefined == 'y':
        template = raw_input('Location of your template: ')

        addfile = raw_input(bcolors.WARNING + '\nWould you like to give this email any attachment?\ny/n: ' + bcolors.ENDC)
        if addfile == ('y'):
            attachment = raw_input('Destination to attachment: ')
            cmd1 = "cat %s | sendemail -s %s -t %s -f %s -u %s -a %s"%(template,smtpserver,toemail,fromemail,subject,attachment)
            os.system(cmd1)
            raw_input(bcolors.OKGREEN + 'Press [ENTER] to return to the main menu...' + bcolors.ENDC)
        else:
            cmd2 = "cat %s | sendemail -s %s -t %s -f %s -u %s"%(template,smtpserver,toemail,fromemail,subject)
            os.system(cmd2)
            raw_input(bcolors.OKGREEN + 'Press [ENTER] to return to the main menu...' + bcolors.ENDC)

    else:
        message = raw_input('\nMessage: ')

        addfile = raw_input(bcolors.WARNING + '\nWould you like to give this email any attachment?\ny/n: ' + bcolors.ENDC)
        if addfile == ('y'):
            attachment = raw_input('Destination to attachment: ')
            cmd3 = "sendemail -s %s -t %s -f %s -u %s -m %s -a %s"%(smtpserver,toemail,fromemail,subject,message,attachment)
            os.system(cmd3)
            raw_input(bcolors.OKGREEN + 'Press [ENTER] to return to the main menu...' + bcolors.ENDC)
        else:
            cmd4 = "sendemail -s %s -t %s -f %s -u %s -m %s"%(smtpserver,toemail,fromemail,subject,message)
            os.system(cmd4)
            raw_input(bcolors.OKGREEN + 'Press [ENTER] to return to the main menu...' + bcolors.ENDC)



try:
    spoofemail()
except KeyboardInterrupt:
    print("\n\nDon't forget your cat!\n")
