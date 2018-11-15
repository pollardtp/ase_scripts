#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os
import ase.io

dir_ = os.getcwd()

for file_ in glob.glob('%s/*.gen' % dir_):
   filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
   inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='gen')
   out_ = ase.io.write('%s.cif' % (filename_), inp_, format='cif')

