#!/usr/bin/env python3

'''
usage: python3 xyz2vasp.py a b c alpha beta gamma

Uses ASE to convert trimmed XYZ (XMOL), see pos2xyz.py, to VASP POSCAR format.
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
from ase import build

dir = os.getcwd()

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
alpha = sys.argv[4]
beta = sys.argv[5]
gamma = sys.argv[6]

for file in glob.glob('%s/*-trim.xyz' % dir):
   filename, fileext = os.path.splitext(file) # fileext carries the .
   fileroot, filescrap = filename.split('-trim') # second part is useless now
   inp = read('%s%s' % (filename, fileext) , format='xyz')
   inp.set_cell([a, b, c, alpha, beta, gamma])
   out = write('%s-opt.vasp' % (fileroot), inp, format='vasp', direct=True, sort=True, vasp5=True)
