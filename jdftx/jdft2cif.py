#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os, subprocess
from ase import Atom, Atoms
from ase.calculators.JDFTx import JDFTx
import ase.io

# assumes you used bohr, if not, multiply coordinates by inverse of bohr2ang = 1 / 0.52917721067 # from CODATA
ions_ = ase.io.read('ionpos', format='jdftion')
cell_ = ase.io.read('lattice', format='jdftlat')
ions_.set_pbc([True, True, True])
ions_.set_cell([[cell_[0][0], cell_[1][0], cell_[2][0]], [cell_[0][1], cell_[1][1], cell_[2][1]], [cell_[0][2], cell_[1][2], cell_[2][2]]])
print ("Check the lengths and angles seem reasonable: %s" % ions_.get_cell_lengths_and_angles())
outs_ = ase.io.write('%s.cif' % ions_.get_chemical_formula(mode='reduce'), ions_, format='cif')

