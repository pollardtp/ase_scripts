#!/usr/bin/env python3

'''
usage: python3 cif2xyz.py

Uses ASE to convert a CIF format file to XYZ (XMOL) format file.
'''

import glob
import os
import sys

from require import check_ase
check_ase()

import ase
from ase.io import read, write

dir = os.getcwd()

for file in glob.glob('%s/*.cif' % dir):
   filename, fileext = os.path.splitext(infile) # fileext carries the .
   inp = read('%s%s' % (filename, fileext) , format='cif')
   out = write('%s.xyz' % (filename), inp, format='xyz')
