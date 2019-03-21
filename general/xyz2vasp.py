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

for file_ in glob.glob('%s/*-trim.xyz' % dir_):
   filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
   fileroot_, filescrap_ = filename_.split('-trim') # second part is useless now
   inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='xyz')
   inp_.set_cell([a, b, c, alpha, beta, gamma])
   out_ = ase.io.write('%s-opt.vasp' % (fileroot_), inp_, format='vasp', direct=True, sort=True, vasp5=True)

