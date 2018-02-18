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


# Make sure Tool is run via sudo or by root
if not os.geteuid() == 0:
    sys.exit(bcolors.FAIL + "\nOnly root can run this script\nTry with $ sudo -H setup.py install|uninstall" + bcolors.ENDC)


def install():
    print(bcolors.WARNING + "Setting up KalEl For You..." + bcolors.ENDC)

    # Create and Copy files to installdir /opt/KalEl
    if os.path.isfile('/opt/KalEl/run.py'):
        reinstall = raw_input('KalEl is allready installed!\nDo you want to uninstall? (y/n): ')
        if reinstall == ('y'):
            print(bcolors.WARNING + 'After removal is complete you have to run $ python setup.py again' + bcolors.ENDC)
            raw_input('Press [ENTER] to continue...')
            uninstall()
        else:
            sys.exit()

    print(bcolors.WARNING + "[*] Copying KalEl into the /opt/KalEl directory..." + bcolors.ENDC)
    cwdpath = os.getcwd()
    subprocess.Popen("cp -rf %s /opt/KalEl" % cwdpath, shell=True).wait()
    subprocess.Popen("mkdir /opt/KalEl/.kal", shell=True).wait()

    # Create a symbolic link for performing actions via /usr/bin
    subprocess.Popen("ln -s /opt/KalEl/run.py /opt/KalEl/kalel", shell=True).wait()
    subprocess.Popen("ln -s /opt/KalEl/module/tor/tor.py /opt/KalEl/kalelvpn", shell=True).wait()

    print(bcolors.WARNING + "[*] Installing KalEl installer to /usr/bin/kalel..." + bcolors.ENDC)
    if os.path.isfile("/usr/bin/kalel"):
        subprocess.Popen("rm /usr/bin/kalel", shell=True).wait()
    else:
        pass
        setlinks()
        fixpermissions()


    # CHECK REQUIRED DEPENDENCIES
    FNULL = open(os.devnull, 'w')

    # sendemail for mail spoofing
    try:
        subprocess.call(["sendemail"], stdout=FNULL, stderr=subprocess.STDOUT)
        with open("/opt/KalEl/src/config.py", "w") as filewrite:
            filewrite.write("\n#[SENDEMAIL DIR]\n")
            filewrite.write("sendemaildir")
            filewrite.write(" = ")
            filewrite.write("/usr/bin/sendemail\n")
        print(bcolors.OKGREEN + '[*] SendEmail OK!' + bcolors.ENDC)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(bcolors.WARNING + "Please install SendEmail or define it's install directory" + bcolors.ENDC)
            sendemaildir = raw_input("Define SendEmail installation directory\nexample (default): /usr/bin/sendemail\nDir: ")
            with open("/opt/KalEl/src/config.py", "w") as filewrite:
                filewrite.write("\n#[SENDEMAIL DIR]\n")
                filewrite.write("sendemaildir")
                filewrite.write(" = ")
                filewrite.write("'%s'\n" % sendemaildir)
        else:
            print(bcolors.FAIL + "something else went wrong, try again" + bcolors.ENDC)
            raise

        # check sslstrip
    try:
        subprocess.call(["sslstrip", "-h"], stdout=FNULL, stderr=subprocess.STDOUT)
        with open("/opt/KalEl/src/config.py", "w") as filewrite:
            filewrite.write("\n#[SSLSTRIP-DIR]\n")
            filewrite.write("sslstripdir")
            filewrite.write(" = ")
            filewrite.write("/usr/bin/sslstrip\n")
        print(bcolors.OKGREEN + '[*] SSLSTRIP OK!' + bcolors.ENDC)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(bcolors.WARNING + "Please install SSLSTRIP or define it's install directory" + bcolors.ENDC)
            sslstripdir = raw_input("Define SSLSTRIP installation directory\nexample (default): /usr/bin/sslstrip\nDir: ")
            with open("/opt/KalEl/src/config.py", "w") as filewrite:
                filewrite.write("\n#[SENDEMAIL-DIR]\n")
                filewrite.write("sslstripdir")
                filewrite.write(" = ")
                filewrite.write("'%s'\n" % sslstripdir)
        else:
            print(bcolors.FAIL + "something else went wrong, try again" + bcolors.ENDC)
            raise


    # Check if ettercap is installed or present
    try:
        subprocess.call(["ettercap", "-h"], stdout=FNULL, stderr=subprocess.STDOUT)
        with open("/opt/KalEl/src/config.py", "w") as filewrite:
            filewrite.write("\n#[ETTERCAP-DIR]\n")
            filewrite.write("etterdir")
            filewrite.write(" = ")
            filewrite.write("/usr/bin/ettercap\n")
        print(bcolors.OKGREEN + '[*] Ettercap OK!' + bcolors.ENDC)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(bcolors.WARNING + "We cant seem to find ettercap-ng" + bcolors.ENDC)
            print(bcolors.WARNING + "Please install ettercap or define it's install directory" + bcolors.ENDC)
            etterdir = raw_input("Define ettercap installation directory\nexample (default): /usr/bin/ettercap\nDir: ")
            with open("/opt/KalEl/src/config.py", "w") as filewrite:
                filewrite.write("\n#[ETTERCAP-DIR]\n")
                filewrite.write("etterdir")
                filewrite.write(" = ")
                filewrite.write("'%s'\n" % etterdir)
        else:
            print(bcolors.FAIL + "something else went wrong, try again" + bcolors.ENDC)
            raise

    # Tor bundle
    try:
        subprocess.call(["tor", "-h"], stdout=FNULL, stderr=subprocess.STDOUT)
        with open("/opt/KalEl/src/config.py", "w") as filewrite:
            filewrite.write("\n#[TOR-DIR]\n")
            filewrite.write("tordir")
            filewrite.write(" = ")
            filewrite.write("/usr/bin/tor\n")
        print(bcolors.OKGREEN + '[*] TOR OK!' + bcolors.ENDC)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(bcolors.WARNING + "We cant seem to find TOR" + bcolors.ENDC)
            print(bcolors.WARNING + "Please install TOR or define it's directory" + bcolors.ENDC)
            tordir = raw_input("Define TOR installation directory\nexample (default): /usr/bin/TOR\nDir: ")
            with open("/opt/KalEl/src/config.py", "w") as filewrite:
                filewrite.write("\n#[TOR-DIR]\n")
                filewrite.write("tordir")
                filewrite.write(" = ")
                filewrite.write("'%s'\n" % tordir)
        else:
            print(bcolors.FAIL + "something else went wrong, try again" + bcolors.ENDC)
            raise

    # Install python dependencies
    try:
        import pip
    except ImportError:
        print(bcolors.FAIL + "KalEl's Modules might not work because of missing pip" + bcolors.ENDC)
        print(bcolors.FAIL + "Try installing pip for python manually!" + bcolors.ENDC)
        sys.exit()
    else:
        print(bcolors.OKGREEN + '[*] PIP OK!' + bcolors.ENDC)

        # Install Required python packages from requirements.txt
        try:
            subprocess.call(["pip","install", "-r", "requirements.txt"], stdout=FNULL, stderr=subprocess.STDOUT)
        except OSError:
            print(bcolors.FAIL + 'Requirements install gave us an error' + bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + '[*] Requirements install OK!' + bcolors.ENDC)
        pass

    # Write setup to src/setupOK to let kalel know setup is complete
    with open("/opt/KalEl/src/setupOK", "w") as filewrite:
        filewrite.write("Installed")

    print(bcolors.WARNING + "[*] We are now finished! To run KalEl, type kalel..." + bcolors.ENDC)
    sys.exit()

# Write permission to run
def fixpermissions():
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/run.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/tor/tor.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/cracking/pawned/pawned.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/cracking/hashbuster/hashbuster.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/trafficgen/getheader.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/ettercap/spoof.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/harvester/prep.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/harvester/engine.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/spoofmail/spoofmail.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/cracking/wspg/core.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/cracking/wspg/scraper.py'])


    # Link for main program
def setlinks():
    subprocess.Popen("echo #!/bin/bash > /usr/bin/kalel", shell=True).wait()
    subprocess.Popen("echo cd /opt/KalEl >> /usr/bin/kalel", shell=True).wait()
    subprocess.Popen("echo exec python2 kalel $@ >> /usr/bin/kalel", shell=True).wait()
    subprocess.Popen("chmod +x /usr/bin/kalel", shell=True).wait()
    # Link for TOR TOR VPN
    subprocess.Popen("echo #!/bin/bash > /usr/bin/kalelvpn", shell=True).wait()
    subprocess.Popen("echo cd /opt/KalEl >> /usr/bin/kalelvpn", shell=True).wait()
    subprocess.Popen("echo exec python2 kalelvpn $@ >> /usr/bin/kalelvpn", shell=True).wait()
    subprocess.Popen("chmod +x /usr/bin/kalelvpn", shell=True).wait()

# KalEl uninstaller arg: uninstall
def uninstall():
    print(bcolors.WARNING + 'KalEl Uninstaller...' + bcolors.ENDC)

    # Check if KalEl is installed
    if not os.path.isfile('/opt/KalEl/run.py'):
        if not os.path.isfile('/usr/bin/kalel'):
            print(bcolors.FAIL + 'KaleEl Is not installed' + bcolors.ENDC)
            sys.exit()

    # If KalEl is installed we'll remove it
    if os.path.isdir('/opt/KalEl'):
        print(bcolors.OKBLUE + 'Found KalEl...' + bcolors.ENDC)
        print(bcolors.FAIL + 'Removing' + bcolors.ENDC)
        subprocess.Popen("rm /usr/bin/kalel*", shell=True).wait()
        subprocess.Popen("rm -fr /root/.kal", shell=True).wait()
        subprocess.Popen("cd ..;rm -fr /opt/KalEl", shell=True).wait()
        print(bcolors.OKGREEN + 'Done! Bye KalEl :(' + bcolors.ENDC)
        time.sleep(2)
        sys.exit()


arg = sys.argv[1:]

if len(arg) != 1:
    print(bcolors.FAIL + '\n!!! Missing argument !!!' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Choose argument: install/uninstall' + bcolors.ENDC)
    print(bcolors.WARNING + 'Install = sudo -H python setup.py install' + bcolors.ENDC)
    sys.exit()
elif sys.argv[1] == "install":
    install()
elif sys.argv[1] == "uninstall":
    uninstall()
else:
    print(bcolors.FAIL + '\n!!! Missing argument !!!' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Choose argument: install/uninstall' + bcolors.ENDC)
    print(bcolors.WARNING + 'Install = sudo -H python setup.py install' + bcolors.ENDC)
    sys.exit()
