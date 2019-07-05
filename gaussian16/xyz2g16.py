#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os
import ase.io
from ase import Atoms
from ase.calculators.gaussian import Gaussian

dir_ = os.getcwd()

for file_ in glob.glob('%s/*.xyz' % dir_):
    filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
    inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='xyz')

    calc_ = Gaussian(mem='64GB', nproc='32', opt='tight, MaxCycles=360, recalcfc=20', scrf='cpcm, solvent=generic, read', 
                     scf='tight', integral='ultrafine', freq='analytic', method='UM05-2X', basis='6-31+G(d,p)', symmetry='none',
                     addsec="Eps=8\nEpsInf=1.4")

    inp_.set_calculator(calc_)
    calc_.write_input(inp_)
    os.system("mv g09.com %s.gjf" % (filename_))
    os.system("rm g09.ase")

