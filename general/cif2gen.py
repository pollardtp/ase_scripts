#!/p/home/teep/.local_programs/conda3/bin/python

import ase, sys
import ase.io

coords = ase.io.read(sys.argv[1], format='cif')
genout = ase.io.write(sys.argv[2], coords, format='gen')

