#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os, subprocess
from ase import Atom, Atoms
from ase.calculators.JDFTx import JDFTx
import ase.io

dir_ = os.getcwd()

for file_ in glob.glob('%s/*.cif' % dir_):
    filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
    fileroot_ = os.path.basename(filename_) # grab just filename
    inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='cif')
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
    inp_.set_calculator(calc)
    calc.update(inp_)
    os.system('mkdir -p %s' % fileroot_)
    os.system('cp in %s.cif %s' % (fileroot_, fileroot_))
    os.system("sed s~'filename'~'%s'~g %s/jdftx.pbs > %s/jdftx.pbs" % (fileroot_, dir_, filename_)) # grab pbs script
    os.system('rm in')

