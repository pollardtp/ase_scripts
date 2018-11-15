#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os
import ase.io

dir_ = os.getcwd()

for file_ in glob.glob('%s/*.cif' % dir_):
   filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
   inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='cif')
   out_ = ase.io.write('%s.xyz' % (filename_), inp_, format='xyz')

