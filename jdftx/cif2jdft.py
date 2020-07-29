#!/usr/bin/env python3

'''
usage: python3 cif2jdft.py

Uses ASE to generate JDFTx input files from CIF format files.
'''

import glob
import os
import subprocess
import sys

import ase
from ase.io import read, write
from ase import Atom, Atoms
from ase.calculators.JDFTx import JDFTx

dir = os.getcwd()

for file in glob.glob('%s/*.cif' % dir):
    filename, fileext = os.path.splitext(file) # fileext carries the .
    fileroot = os.path.basename(filename) # grab just filename
    inp = read('%s%s' % (filename, fileext) , format='cif')
    calc = JDFTx(executable='mpiexec -np 1 /p/home/teep/.local_programs/jdftx/bin/bin/jdftx', pseudoSet='GBRV',
                 commands={
                           'elec-ex-corr' : 'gga',
                           'elec-cutoff'  : '200 1600', # geo - SSSP max 60 Ry, USPP rhocut is x8, latt is x2 of geo cutoff
                           'kpoint-folding' : '10 10 10',
                           'elec-smearing' : 'Fermi 0.002',
                           'spintype' : 'z-spin',
                           'elec-initial-magnetization' : '0 no',
                           'electronic-scf' : 'nIterations 400',
                           'lattice-minimize' : 'nIterations 100 linminMethod Relax energyDiffThreshold 1e-7 knormThreshold 1e-4',
                          }
                )
    inp.set_calculator(calc)
    calc.update(inp)
    os.system('mkdir -p %s' % fileroot)
    os.system('cp in %s.cif %s' % (fileroot, fileroot))
    os.system("sed s~'filename'~'%s'~g %s/jdftx.pbs > %s/jdftx.pbs" % (fileroot, dir, filename)) # grab pbs script
    os.system('rm in')
