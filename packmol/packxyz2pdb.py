#!/usr/bin/env python3

'''
usage: python3 packxyz2pdb.py a b c alpha beta gamma

Uses ASE to convert Packmol generated XYZ (XMOL) to PDB format.
'''

import glob
import os
import sys

from require import check_ase
check_ase()

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

for file in glob.glob('%s/*.xyz' % dir):
   filename, fileext = os.path.splitext(file) # fileext carries the .
   inp = read('%s%s' % (filename, fileext) , format='xyz')
   inp.set_cell([a, b, c, alpha, beta, gamma])
   out = write('%s.pdb' % (filename), inp, format='proteindatabank')
