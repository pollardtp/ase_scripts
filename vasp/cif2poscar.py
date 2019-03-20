#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os, subprocess
from ase import Atom, Atoms
from ase.calculators.vasp import Vasp
import ase.io

print("This script sets up an unconstrained optimization of *bulk* materials. Initializing with ferromagnetic (high) spin distribution.")

dir_ = os.getcwd()

for file_ in glob.glob('%s/*.cif' % dir_):
	filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
	fileroot_ = os.path.basename(filename_) # grab just filename
	inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='cif')

	magmoms = []

	for atom in inp_:
		if ( atom.symbol == 'Ni' ):
			magmoms.append(4.0)
		elif ( atom.symbol == 'Mn' ):
			magmoms.append(4.0)
		else:
			magmoms.append(0.6)

	inp_.set_initial_magnetic_moments(magmoms)

#ldau_luj={'Mn':{'L':2, 'U':4.84, 'J':0.0},
#          'Co':{'L':2, 'U':5.14, 'J':0.0},
#          'Ni':{'L':2, 'U':6.37, 'J':0.0},
#          'H':{'L':-1, 'U':0.0, 'J':0.0},
#          'C':{'L':-1, 'U':0.0, 'J':0.0},
#          'O':{'L':-1, 'U':0.0, 'J':0.0},
#          'F':{'L':-1, 'U':0.0, 'J':0.0},
#          'Li':{'L':-1, 'U':0.0, 'J':0.0}}

# pbe 520 eV, high precision for cell optimization, tight convergence, lbfgs from vtst optimizer
	calc = Vasp(xc='PBE', npar=8, nsim=1, nelmdl=-12, istart=1, icharg=1, lorbit=11, voskown=1, lasph=True, kpts=(12, 12, 2),
	prec='high', algo='normal', ediff=0.00001, ediffg=-0.001, potim=0, lreal='auto', ibrion=-1, nsw=400,
	nelm=600, isif=2, encut=520, ismear=1, sigma=0.2, lmaxmix=4, amix=0.2, bmix=0.0001, amix_mag=0.8, bmix_mag=0.0001,
	maxmix=40, nwrite=1, ispin=2, ldau=True, ldauprint=1, ldautype=2, nelmin=4, lwave='true', iopt=1,
	ldau_luj={'Ni': {'L': 2, 'U': 6.37, 'J': 0.0}, 'Mn': {'L': 2, 'U': 4.84, 'J': 0.0}}, setups={'Li': '_sv', 'Ni': '_pv', 'Mn': '_pv'})

# dump files
	os.system("mkdir -p %s" % filename_) # makes folder with basename of cif
	os.system("sed s~'filename'~'%s'~g %s/vasp.pbs > %s/vasp.pbs" % (fileroot_, dir_, filename_)) # grab pbs script
	inp_.set_calculator(calc)
	calc.initialize(inp_)
	calc.write_incar(inp_)
	calc.write_potcar()
	calc.write_kpoints()
	ase.io.write("POSCAR", inp_, format="vasp", direct=True, sort=True, vasp5=True)
	os.system("mv POSCAR KPOINTS INCAR POTCAR %s" % (filename_))

