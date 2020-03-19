#!/usr/bin/env python3

'''
 Usage: xyz2cip_ssip.py foo.xyz latt_a latt_b latt_c alpha beta gamma
        script          file    lattice vectors      lattice shape

 Purpose: takes XYZ (XMOL) format file and converts some atoms to different 
          names to assist in reducing cost to visualize with Jmol. Future
          extensions may involve singling out decomposed PF6 and changing
          F to Cl if reduced but nearby and Br if dissociated.
'''

import os
import sys
from collections import Counter

import ase
from ase.io import read, write
from ase import build
from ase import Atom, Atoms, neighborlist

file = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]
c = sys.argv[4]
alpha = sys.argv[5]
beta = sys.argv[6]
gamma = sys.argv[7]

# 609-614 are LiS, 0 indexed so minus 1
filename, fileext = os.path.splitext(file) # fileext carries the .
inp = read('%s%s' % (filename, fileext) , format='xyz', index=':')
nframes = len(inp)
for frame in range(nframes):
  inp[frame].set_cell([a, b, c, alpha, beta, gamma])
  inp[frame].set_pbc([True, True, True])
  inp[frame][608].symbol = 'K'
  inp[frame][609].symbol = 'K'
  inp[frame][610].symbol = 'K'
  inp[frame][611].symbol = 'K'
  inp[frame][612].symbol = 'K'
  inp[frame][613].symbol = 'K'
  i_dex, j_dex, ij_dis = neighborlist.neighbor_list('ijd', inp[frame], {('P', 'K'): 4.4}, self_interaction=False) # agg/cip limit
  for ith in range(len(i_dex)):
    d = Counter(i_dex)
    if ( inp[frame][i_dex[ith]].symbol == 'P' and d[i_dex[ith]] > 1 ):
      inp[frame][i_dex[ith]].symbol = 'Fe'
    if ( inp[frame][i_dex[ith]].symbol == 'P' and d[i_dex[ith]] == 0 ):
      inp[frame][i_dex[ith]].symbol = 'S'
  write('%s_agg_label.xyz' % (filename), inp[frame], format='xyz', append=True)

