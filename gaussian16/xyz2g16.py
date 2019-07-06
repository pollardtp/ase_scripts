#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os, re
import ase.io
from ase import Atoms
from ase.calculators.gaussian import Gaussian

dir_ = os.getcwd()

for file_ in glob.glob('%s/*.xyz' % dir_):
    filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
    inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='xyz')
    filter_filename_ = re.sub(r'[.]','_', filename_) # HPC script cuts filename at first .

    magmom = []

    for atom in inp_:
        if ( atom.symbol == 'O' ):
            magmom.append(0.5)
        else:
            magmom.append(0)

    inp_.set_initial_magnetic_moments(magmom)

    calc_ = Gaussian(mem='64GB', nproc='32', opt='tight, MaxCycles=360', scrf='cpcm, solvent=generic, read', 
                     scf='tight', integral='ultrafine', freq='analytic', method='UPBEPBE', basis='6-31+G(d)', 
                     symmetry='none', extra='empiricaldispersion=gd3bj', addsec="Eps=8\nEpsInf=1.96")

    inp_.set_calculator(calc_)
    calc_.write_input(inp_)
    os.system("mv g09.com %s.gjf" % (filter_filename_))
    os.system("rm g09.ase")

