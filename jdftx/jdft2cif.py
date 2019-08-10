#!/usr/bin/env python3

'''
usage: python3 jdft2cif.py

Uses ASE to convert JDFTx format coordinates to CIF format.
'''

import glob
import os
import subprocess
import sys

from require import check_ase
check_ase()

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
