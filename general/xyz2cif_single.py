#!/usr/bin/env python3

'''
usage: python3 xyz2cif_single.py a b c alpha beta gamma

Uses ASE to convert trimmed XYZ (XMOL) to CIF format.
Converts a single file, requested in command line.
'''

import glob
import os
import sys

import ase
from ase.io import read, write
from ase import build

file = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]
c = sys.argv[4]
alpha = sys.argv[5]
beta = sys.argv[6]
gamma = sys.argv[7]

filename, fileext = os.path.splitext(file) # fileext carries the .
inp = read('%s%s' % (filename, fileext) , format='xyz')
inp.set_cell([a, b, c, alpha, beta, gamma])
out = write('%s-conv.cif' % (filename), inp, format='cif')

