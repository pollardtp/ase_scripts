#!/usr/bin/env python3

'''
usage: python3 digestVaspOutcar.py

Uses ASE to gobble up the OUTCAR and return a json outcar with only info of the
final geometry printed.
'''

import pkg_resources
import glob
import os
import subprocess
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
from ase import Atom, Atoms
from ase.db import connect

# initialize database
db = connect('outcar.json')

# reads OUTCAR/POTCAR/CONTCAR/POSCAR index [-1]
vo = read('OUTCAR')

# write db
db.write(vo)
