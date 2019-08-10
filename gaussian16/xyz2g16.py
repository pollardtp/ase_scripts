#!/usr/bin/env python3

'''
usage: python3 cp2kneb2xyzmov.py foo1.xyz foo2.xyz ... fooN.xyz

CP2K writes each image in an NEB calculation to its own XYZ (XMOL) file.
This script uses ASE to read each image in and output the final snapshot
from each file to a single file called trj.xyz that shows the optimized
path when viewed.
'''

import glob
import os
import re
import sys

from require import check_ase
check_ase()

import ase
from ase.io import read, write
from ase import Atoms
from ase.calculators.gaussian import Gaussian

dir = os.getcwd()

for file in glob.glob('%s/*.xyz' % dir):
    filename, fileext = os.path.splitext(file) # fileext carries the .
    inp = read('%s%s' % (filename, fileext) , format='xyz')
    filter_filename = re.sub(r'[.]','_', filename) # HPC script cuts filename at first .

    magmom = []

    for atom in inp:
        if ( atom.symbol == 'O' ):
            magmom.append(0.5)
        else:
            magmom.append(0)

    inp.set_initial_magnetic_moments(magmom)

    calc = Gaussian(mem='64GB', nproc='32', opt='tight, MaxCycles=360', scrf='cpcm, solvent=generic, read',
                     scf='tight', integral='superfine', freq='analytic', method='UPBEPBE', basis='6-31+G(d)',
                     symmetry='none', extra='empiricaldispersion=gd3bj', addsec="Eps=8\nEpsInf=1.96")

    inp.set_calculator(calc)
    calc.write_input(inp)
    os.system("mv g09.com %s.gjf" % (filter_filename))
    os.system("rm g09.ase")
