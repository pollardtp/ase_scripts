#!/usr/bin/env python3

'''
usage: python3 pos2xyz.py

Uses ASE to dump final image of a CP2K trajectory in XYZ (XMOL) format.
'''

import glob
import os
import sys

import check_ase
check_ase()

import ase
from ase.io import read, write

dir = os.getcwd()

# works only with cp2k pos-1.xyz or pos-BANDDATA-nr-YYY.xyz
for file in glob.glob('%s/*-pos-*.xyz' % dir):
   filename, fileext = os.path.splitext(file) # fileext carries the .
   fileroot, filescrap = filename.split('-pos') # second part is useless now
   inp = read('%s%s' % (filename, fileext) , format='xyz', index=-1)
   out = write('%s-trim.xyz' % (fileroot), inp, format='xyz')
