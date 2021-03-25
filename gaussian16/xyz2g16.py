#!/usr/bin/env python3

'''
usage: python3 xyz2g16.py

Converts XYZ (XMOL) to Gaussian 16 file. Copy to local directory to modify theory.
'''

import glob
import os
import re
import sys

import ase
from ase.io import read, write
from ase import Atoms
from ase.calculators.gaussian import Gaussian

dir = os.getcwd()

for file in glob.glob('%s/*.xyz' % dir):
    filename, fileext = os.path.splitext(file) # fileext carries the .
    inp = read('%s%s' % (filename, fileext) , format='xyz')
    filter_filename = re.sub(r'[.]','_', filename) # HPC script cuts filename at first .

    t1 = re.compile(".*_(q-?(?:\d+,?)+m-?(?:\d+,?)+).*") # regex for charge and spin part of filename
    t2 = t1.match("%s" % (filter_filename)).group(1) # grabs regex
    chg = re.split('[a-z]', t2)[1] # is charge
    spn = re.split('[a-z]', t2)[2] # is spin

    gsolv = 'pcm, solvent=acetone'

    calc = Gaussian(mem='64GB', cpu='40', opt='tight, MaxCycles=360', scrf=gsolv, scf='tight', integral='ultrafine', freq='analytic', method='M052X', basis='6-31+G(d,p)', symmetry='none', charge=int(chg), mult=int(spn))

    inp.set_calculator(calc)
    calc.write_input(inp)
    os.system("mv Gaussian.com %s.inp" % (filter_filename))

