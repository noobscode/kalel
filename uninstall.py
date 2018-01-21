#!/usr/bin/env python

import os
import sys
import subprocess
import time

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
    subprocess.Popen("cd ..;rm -fr /opt/KalEl", shell=True).wait()
    print('Done! Bye KalEl :()')
    time.sleep(2)
    exit(1)
