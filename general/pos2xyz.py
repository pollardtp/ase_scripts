#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os
import ase.io

# works only with cp2k pos-1.xyz or pos-BANDDATA-nr-YYY.xyz

dir_ = os.getcwd()

for file_ in glob.glob('%s/*-pos-*.xyz' % dir_):
   filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
   fileroot_ = filename_.split('-pos') # second part is useless now
   inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='xyz', index=-1)
   out_ = ase.io.write('%s-trim.xyz' % (fileroot_), inp_, format='xyz')

