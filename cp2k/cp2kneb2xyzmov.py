#!/usr/bin/env python3

'''
usage: python3 cp2kneb2xyzmov.py foo1.xyz foo2.xyz ... fooN.xyz

CP2K writes each image in an NEB calculation to its own XYZ (XMOL) file.
This script uses ASE to read each image in and output the final snapshot
from each file to a single file called trj.xyz that shows the optimized
path when viewed.
'''

import sys

import check_ase
check_ase()

import ase
from ase.io import read, write

for frame in range(1,len(sys.argv)):
    inp = read(sys.argv[frame], format='xyz', index='-1')
    out = write('trj.xyz', inp, format='xyz', append='True')
