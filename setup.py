#!/usr/bin/env python
import os
import time
import subprocess
import sys

# Verify that the user is root
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\nTry with $ sudo python setup.py")

print("Setting up KalEl For You...")

# Write permission to run
subprocess.call(['chmod', '+x', 'run.py'])
subprocess.call(['chmod', '+x', 'modules/harvester/engine.py'])

# Check if config files is present, if they are we will remove them
if os.path.isfile("src/setupOK"):
    subprocess.call(['rm', 'src/setupOK'])

if os.path.isfile("src/config.cfg"):
    subprocess.call(['rm', 'src/config.py'])

# Install sendemail for mail spoofing
try:
    subprocess.call(["sendemail"])
except OSError as e:
    if e.errno == os.errno.ENOENT:
        print('sendemail not install, installing now')
        subprocess.call(['sudo', 'apt-get', 'install', '-y', 'sendemail'])
    else:
        print("something else went wrong, try again")
        raise

# Check if ettercap is installed or present
try:
    subprocess.call(["ettercap"])
except OSError as e:
    if e.errno == os.errno.ENOENT:
        print("We cant seem to find ettercap-ng")
        print("Please install ettercap or define it's install directory")
        etterdir = raw_input("Define ettercap installation directory\nexample (default): /usr/bin/ettercap\nDir: ")
        with open("src/config.py", "w") as filewrite:
            filewrite.write("\n#[ETTERCAP DIR]\n")
            filewrite.write("etterdir")
            filewrite.write(" = ")
            filewrite.write("'%s'\n" % etterdir)
    else:
        print("something else went wrong, try again")
        raise
# Write setup to src/setupOK to let the tool know setup is complete
with open("src/setupOK", "w") as filewrite:
    filewrite.write("Installed")

#Setup done
print("Setup is done, sending you to KalEl Main menu")
time.sleep(3)

# Start KalEl Toolkit when setup is done
import run
