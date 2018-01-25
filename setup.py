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


def install():
    print("Setting up KalEl For You...")

    # Create and Copy files to installdir /opt/KalEl
    if os.path.isfile('/opt/KalEl/run.py'):
        reinstall = raw_input('KalEl is allready installed!\nDo you want to reinstall? (y/n): ')
        if reinstall == ('y'):
            print('After removal is complete you have to run $ python setup.py again')
            raw_input('Press [ENTER] to continue...')
            reinstall()
        else:
            exit(1)

    print("[*] Copying KalEl into the /opt/KalEl directory...")
    cwdpath = os.getcwd()
    subprocess.Popen("cp -rf %s /opt/KalEl" % cwdpath, shell=True).wait()
    subprocess.Popen("mkdir /opt/KalEl/.kal", shell=True).wait()

    # Create a symbolic link for performing actions via /usr/bin
    subprocess.Popen("ln -s /opt/KalEl/run.py /opt/KalEl/kalel", shell=True).wait()
    subprocess.Popen("ln -s /opt/KalEl/module/tor/tor.py /opt/KalEl/kalelvpn", shell=True).wait()

    print("[*] Installing KalEl installer to /usr/bin/kalel...")
    if os.path.isfile("/usr/bin/kalel"):
        subprocess.Popen("rm /usr/bin/kalel", shell=True).wait()
    else:
        pass

    # Link for main program
    subprocess.Popen("echo #!/bin/bash > /usr/bin/kalel", shell=True).wait()
    subprocess.Popen("echo cd /opt/KalEl >> /usr/bin/kalel", shell=True).wait()
    subprocess.Popen("echo exec python2 kalel $@ >> /usr/bin/kalel", shell=True).wait()
    subprocess.Popen("chmod +x /usr/bin/kalel", shell=True).wait()

    # Link for TOR TOR VPN
    subprocess.Popen("echo #!/bin/bash > /usr/bin/kalelvpn", shell=True).wait()
    subprocess.Popen("echo cd /opt/KalEl >> /usr/bin/kalelvpn", shell=True).wait()
    subprocess.Popen("echo exec python2 kalelvpn $@ >> /usr/bin/kalelvpn", shell=True).wait()
    subprocess.Popen("chmod +x /usr/bin/kalelvpn", shell=True).wait()

    fixpermissions()

    # Check if config files is present, if they are we will remove them
    if os.path.isfile("/opt/KalEl/src/setupOK"):
        subprocess.call(['rm', '/opt/KalEl/src/setupOK'])

    if os.path.isfile("/opt/KalEl/src/config.py"):
        subprocess.call(['rm', '/opt/KalEl/src/config.py'])

    # CHECK REQUIRED DEPENDENCIES

    FNULL = open(os.devnull, 'w')

    # Install sendemail for mail spoofing
    try:
        subprocess.call(["sendemail"], stdout=FNULL, stderr=subprocess.STDOUT)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print('sendemail not install, installing now')
            subprocess.call(['sudo', 'apt-get', 'install', '-y', 'sendemail'])
        else:
            print("something else went wrong, try again")
            raise

    # Check if ettercap is installed or present
    try:
        subprocess.call(["ettercap"], stdout=FNULL, stderr=subprocess.STDOUT)
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print("We cant seem to find ettercap-ng")
            installettercap = raw_input('Would you like KalEl to try and install it?\n y/n: ')
            if installettercap == ('y'):
                subprocess.call(['sudo', 'apt-get', 'install', '-y', 'ettercap-text-only'])
                print('Done')
            else:
                print("Please install ettercap or define it's install directory")
                etterdir = raw_input("Define ettercap installation directory\nexample (default): /usr/bin/ettercap\nDir: ")
                with open("/opt/KalEl/src/config.py", "w") as filewrite:
                    filewrite.write("\n#[ETTERCAP DIR]\n")
                    filewrite.write("etterdir")
                    filewrite.write(" = ")
                    filewrite.write("'%s'\n" % etterdir)
        else:
            print("something else went wrong, try again")
            raise

    # Install Tor bundle
    subprocess.call(['apt-get', 'install', 'tor', '-y', '-qq'])

    # Install dependencies for TOR
    try:
        import pip
    except ImportError:
        print('we could not find pip, trying to install pip now')
        # Install PIP
        subprocess.call(['apt-get', 'install', 'python3-pip', '-y'])
        subprocess.call(['apt-get', 'install', 'python-pip', '-y'])
    except Exception:
        print("KalEl's VPN Module might not work because of missing pip")
    else:
        print('PIP install OK!')
        pip.main(['install', 'stem'])
        pip.main(['install', 'requests'])
        pass

    # Write setup to src/setupOK to let the tool know setup is complete
    with open("/opt/KalEl/src/setupOK", "w") as filewrite:
        filewrite.write("Installed")

    print(bcolors.OKGREEN + "[*] We are now finished! To run KalEl, type kalel..." + bcolors.ENDC)
    exit(1)

def fixpermissions():
    # Write permission to run
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/run.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/tor/tor.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/trafficgen/generator.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/ettercap/spoof.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/harvester/prep.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/harvester/engine.py'])
    subprocess.Popen(['chmod', '+x', '/opt/KalEl/module/spoofmail/spoofmail.py'])


def uninstall():
    print('KalEl Uninstaller...')

    # Check if KalEl is installed
    if not os.path.isfile('/opt/KalEl/run.py'):
        if not os.path.isfile('/usr/bin/kalel'):
            print('KaleEl Is not installed')
            exit(1)

    # If KalEl is installed we'll remove it
    if os.path.isdir('/opt/KalEl'):
        print('Found KalEl...')
        print('Removing')
        subprocess.Popen("rm /usr/bin/kalel*", shell=True).wait()
        subprocess.Popen("rm -fr /root/.kal", shell=True).wait()
        subprocess.Popen("cd ..;rm -fr /opt/KalEl", shell=True).wait()
        print('Done! Bye KalEl :()')
        time.sleep(2)
        exit(1)


def reinstall():
    if not os.path.isfile('/tmp/setup.py'):
        subprocess.Popen('cp /opt/KalEl/setup.py /tmp/setup.py', shell=True).wait()
    os.chdir('/tmp/')
    subprocess.call(['setup.py', 'reinstall'], shell=True).wait()
    subprocess.call(['git', 'clone', 'https://github.com/noobscode/kalel'], shell=True).wait()
    subprocess.call('cd kalel/', shell=True).wait()
    subprocess.call(['setup.py', 'uninstall'], shell=True).wait()
    subprocess.call(['setup.py', 'install'], shell=True).wait()


arg = sys.argv[1:]

if len(arg) != 1:
    print(bcolors.FAIL + '\n!!! Missing argument !!!' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Choose argument: install/reinstall/uninstall' + bcolors.ENDC)
    sys.exit(1)
elif sys.argv[1] == "install":
    install()
elif sys.argv[1] == "reinstall":
    reinstall()
elif sys.argv[1] == "uninstall":
    uninstall()
else:
    print('Choose argument: install/uninstall')
    sys.exit(1)
