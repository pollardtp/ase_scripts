#!/usr/bin/env python3

'''
usage: python3 jdft2cif.py

Uses ASE to convert JDFTx format coordinates to CIF format.
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
from ase.calculators.JDFTx import JDFTx

# assumes you used bohr, if not, multiply coordinates by inverse of bohr2ang = 1 / 0.52917721067 # from CODATA
ions = read('ionpos', format='jdftion')
cell = read('lattice', format='jdftlat')
ions.set_pbc([True, True, True])
ions.set_cell([[cell_[0][0], cell_[1][0], cell_[2][0]], [cell_[0][1], cell_[1][1], cell_[2][1]], [cell_[0][2], cell_[1][2], cell_[2][2]]])
print ("Check the lengths and angles seem reasonable: %s" % ions.get_cell_lengths_and_angles())
out = write('%s.cif' % ions.get_chemical_formula(mode='reduce'), ions, format='cif')
