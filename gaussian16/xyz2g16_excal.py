#!/usr/bin/env python3

'''
usage: python3 xyz2g16_excal.py

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
