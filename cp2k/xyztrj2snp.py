#!/p/home/teep/.local_programs/conda3/bin/python

import ase, sys
import ase.io 

for frame in range(1,len(sys.argv)):
    inp_ = ase.io.read(sys.argv[frame], format='xyz', index='-1')
    out_ = ase.io.write('trj.xyz', inp_, format='xyz', append='True')

