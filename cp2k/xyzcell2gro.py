#!/usr/bin/env python3

'''
usage: python3 xyzcell2gro.py

Reads XMOL format file, adds lattice parameters, dumps Gromos file that can
be read by VMD.
'''

import glob
import os
import sys
import numpy as np

import ase
from ase.io import read, write

dir = os.getcwd()

# trajectory is XMOL format
# cell       is step time ax ay az bx by bz cx cy cz vol
for file in glob.glob('%s/*-pos-*.xyz' % dir):
   filename, fileext = os.path.splitext(file)
   fileroot, filescrap = filename.split('-pos')
   trj = read('%s%s' % (filename, fileext) , format='xyz', index=':')
   cel = np.loadtxt('%s-1.cell' % (fileroot), usecols=range(2,11), dtype=np.double)
   nframes = len(trj)
   for frame in range(nframes):
      trj[frame].set_cell([(cel[frame][0], cel[frame][1], cel[frame][2]),
                           (cel[frame][3], cel[frame][4], cel[frame][5]),
                           (cel[frame][6], cel[frame][7], cel[frame][8])])
      trj[frame].set_pbc([True, True, True])
      write('%s.g96' % (fileroot), trj[frame], format='gromos', append=True)
