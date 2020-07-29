#!/usr/bin/env python3

'''
usage: python3 gen2cif.py

Uses ASE to convert a DFTB+ gen format file to a CIF format file.
'''

import glob
import os
import sys

import ase
from ase.io import read, write

dir = os.getcwd()

for file in glob.glob('%s/*.gen' % dir):
   filename, fileext = os.path.splitext(file) # fileext carries the .
   inp = read('%s%s' % (filename, fileext) , format='gen')
   out = write('%s.cif' % (filename), inp, format='cif')
