#!/usr/bin/env python3

'''
usage: python3 xyz2vasp.py a b c alpha beta gamma

Uses ASE to convert trimmed XYZ (XMOL), see pos2xyz.py, to VASP POSCAR format.
'''

import glob
import os
import sys

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
