#!/usr/bin/env python3

'''
usage: python3 cif2poscar.py

Uses ASE to convert CIF file format to VASP ver 5.X+ input deck. Copy to local
directory to edit.
'''

import glob
import os
import subprocess
import sys

from require import check_ase
check_ase()

import ase
from ase.io import read, write
from ase import Atom, Atoms
from ase.calculators.vasp import Vasp

dir = os.getcwd()

for file in glob.glob('%s/*.cif' % dir):
	filename, fileext = os.path.splitext(file) # fileext carries the .
	fileroot = os.path.basename(filename) # grab just filename
	inp = read('%s%s' % (filename, fileext) , format='cif')

	magmoms = []

	for atom in inp:
		if ( atom.symbol == 'Ni' ):
			magmoms.append(4.0)
		elif ( atom.symbol == 'Mn' ):
			magmoms.append(4.0)
		else:
			magmoms.append(0.6)

	inp.set_initial_magnetic_moments(magmoms)

	calc = Vasp(xc='PBE', ncore=16, nelmdl=-12, istart=1, icharg=1, lorbit=11,
	            voskown=1, lasph=True, kpts=(1, 1, 1), prec='high', algo='fast',
				ediff=0.00001, ediffg=-0.02, potim=0, lreal='auto', ibrion=1,
				nsw=400, nelm=200, isif=2, encut=520, ismear=1, sigma=0.2,
				lmaxmix=4, amix=0.2, bmix=0.0001, amix_mag=0.8, bmix_mag=0.0001,
	            maxmix=40, nwrite=1, ispin=2, ldau=True, ldauprint=1, ldautype=2,
				nelmin=4, lwave='true', ivdw=12,
				ldau_luj={'Ni': {'L': 2, 'U': 6.37, 'J': 0.0}, 'Mn': {'L': 2, 'U': 4.84, 'J': 0.0}},
				setups={'Li': '_sv', 'Ni': '_pv', 'Mn': '_pv'})

# dump files
	os.system("mkdir -p %s" % filename) # makes folder with basename of cif
	os.system("sed s~'filename'~'%s'~g %s/vasp.pbs > %s/vasp.pbs" % (fileroot, dir, filename)) # grab pbs script
	inp.set_calculator(calc)
	calc.initialize(inp)
	calc.write_incar(inp)
	calc.write_potcar()
	calc.write_kpoints()
	write("POSCAR", inp, format="vasp", direct=True, sort=True, vasp5=True)
	os.system("mv POSCAR KPOINTS INCAR POTCAR %s" % (filename))
