#!/usr/bin/env python3

'''
usage: python3 pos2xyz.py

Uses ASE to dump final image of a CP2K trajectory in XYZ (XMOL) format.
'''

import pkg_resources
import glob
import os
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

dir = os.getcwd()

# works only with cp2k pos-1.xyz or pos-BANDDATA-nr-YYY.xyz
for file in glob.glob('%s/*-pos-*.xyz' % dir):
   filename, fileext = os.path.splitext(file) # fileext carries the .
   fileroot, filescrap = filename.split('-pos') # second part is useless now
   inp = read('%s%s' % (filename, fileext) , format='xyz', index=-1)
   out = write('%s-trim.xyz' % (fileroot), inp, format='xyz')
