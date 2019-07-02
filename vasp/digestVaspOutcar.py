#!/p/home/teep/.local_programs/conda3/bin/python

import ase
from ase import Atom, Atoms
from ase.db import connect
from ase.io import read, write

# initialize database
db = connect('outcar.json')

# reads OUTCAR/POTCAR/CONTCAR/POSCAR index [-1]
vo = read('OUTCAR')

# write db
db.write(vo)

