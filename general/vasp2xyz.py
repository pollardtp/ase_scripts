#!/usr/bin/env python3

'''
usage: python3 vasp2xyz.py

Uses ASE to convert VASP POSCAR/CONTCAR to XYZ (XMOL)
'''

import sys

from require import check_ase
check_ase()

import ase
from ase.io import read, write
from ase import build

dir = os.getcwd()

inp = read(sys.argv[1] , format='vasp')
out = write(sys.argv[2], inp, format='xyz')
