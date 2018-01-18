#!/usr/bin/env python

import os
import time
import subprocess
import sys

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

print("Not ready yet...")
exit(1)
