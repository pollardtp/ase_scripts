#!/usr/bin/env python3

'''
usage: python3 cp2kneb2xyzmov.py foo1.xyz foo2.xyz ... fooN.xyz

CP2K writes each image in an NEB calculation to its own XYZ (XMOL) file.
This script uses ASE to read each image in and output the final snapshot
from each file to a single file called trj.xyz that shows the optimized
path when viewed.
'''

import pkg_resources
import sys

from pkg_resources import DistributionNotFound, VersionConflict

try:
    pkg_resources.require("ase>=3.15.0") # pings recent ase
except pkg_resources.DistributionNotFound:
    print('Exiting: Atomic Simulation Environment not found.')
    sys.exit()
except pkg_resources.VersionConflict:
    print('Exiting: Older version of ASE installed, please update.')
    sys.exit()

del sys.modules["pkg_resources"]
del pkg_resources

import ase
from ase.io import read, write

for frame in range(1,len(sys.argv)):
    inp = read(sys.argv[frame], format='xyz', index='-1')
    out = write('trj.xyz', inp, format='xyz', append='True')
