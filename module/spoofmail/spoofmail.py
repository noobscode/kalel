#!/usr/bin/env python

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
    toemail = raw_input('Target email: ')
    fromemail = raw_input('Sender email: ')
    subject = raw_input('Subject: ')
    message = raw_input('Message: ')

    addfile = raw_input('Would you like to give this email any attachment?\ny/n: ')
    if addfile == ('y'):
        attachment = raw_input('Destination to attachment: ')
        subprocess.call(['sendemail', '-s', smtpserver, '-t', toemail, '-f', fromemail, '-a', attachment, '-u', subject, '-m', message])
    else:
        subprocess.call(['sendemail', '-s', smtpserver, '-t', toemail, '-f', fromemail, '-u', subject, '-m', message])
        raw_input(bcolors.OKGREEN + 'Press [ENTER] to return to the main menu...' + bcolors.ENDC)
        subprocess.call(['kalel'])
    sys.exit(1)


try:
    spoofemail()
except KeyboardInterrupt:
    print("\n\nDon't forget your cat!\n")
finally:
    subprocess.call(['kalel'])
