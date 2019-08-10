#!/usr/bin/env python3

'''
usage: python3 cif2gen.py

Uses ASE to convert a CIF format file to a DFTB+ gen format file.
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

for file in glob.glob('%s/*.cif' % dir):
   filename, fileext = os.path.splitext(infile) # fileext carries the .
   inp = read('%s%s' % (filename, fileext) , format='cif')
   out = write('%s.gen' % (filename), inp, format='gen')
