#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os, sys
import ase.io, ase.build

dir_ = os.getcwd()

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
alpha = sys.argv[4]
beta = sys.argv[5]
gamma = sys.argv[6]

for file_ in glob.glob('%s/*.xyz' % dir_):
   filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
   inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='xyz')
   inp_.set_cell([a, b, c, alpha, beta, gamma])
   out_ = ase.io.write('%s.pdb' % (filename_), inp_, format='proteindatabank')

