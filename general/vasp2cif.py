#!/usr/bin/env python3

'''
usage: python3 vasp2cif.py

Uses ASE to convert a vasp POSCAR to CIF.
'''

import glob
import os
import sys

from require import check_ase
check_ase()

import ase
from ase.io import read, write

dir = os.getcwd()

for file in glob.glob('%s/*.vasp' % dir):
   filename, fileext = os.path.splitext(file) # fileext carries the .
   inp = read('%s%s' % (filename, fileext) , format='vasp')
   out = write('%s.cif' % (filename), inp, format='cif')

