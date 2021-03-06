#!/usr/bin/env python3

'''
usage: python3 pdb2sort.py

Uses ASE to generate sort a PDB in a particular order - OHH, Cl, Li. Can be
modified for other purposes.
'''

import glob
import os
import sys

import ase
from ase.io import read, write
from ase.build import sort
from ase import Atom, Atoms, neighborlist, build

dir = os.getcwd()

check = False

for file in glob.glob('%s/*.pdb' % dir):
    filename, fileext = os.path.splitext(file) # fileext carries the .
    inp = read('%s%s' % (filename, fileext) , format='proteindatabank')

    # Here we want atom order to repeat units of OHH, OHH, ..., Cl, Li
    # sort and push hydrogen to end, else there are indexing issues
    for atom in inp:
        if ( atom.symbol == 'H' ):
           atom.mass = 9999.

    # hydrogens are now last
    inp_clean = sort(inp, tags = inp.get_masses())

    # compute distances, save lists of indices - i_dex contains O and H
    i_dex, j_dex, ij_dis = neighborlist.neighbor_list('ijd', inp_clean, {('H', 'H'): 0.0, ('O', 'O'): 0.0, ('O', 'H'): 1.1}, self_interaction=False)

    # tag each water with the index of the oxygen, the ith water
    for ith in range(len(i_dex)):
        if ( inp_clean[i_dex[ith]].symbol == 'O' ):
            inp_clean[i_dex[ith]].tag = i_dex[ith]
            inp_clean[j_dex[ith]].tag = i_dex[ith]

    # tag the other atoms, just number them in the order you want to see them
    for atom in inp_clean:
        if ( atom.symbol == 'Cl' ):
            atom.tag = 9999998
        if ( atom.symbol == 'Zn' ):
            atom.tag = 9999999

    # sort the reindexed list by water molecule - now H index is > O index, proper order!
    inp_sorted = build.sort(inp_clean, tags=inp_clean.get_tags())

    # give option for testing without writing anything
    if ( check == True ):
        prvO = -3
        for atom in inp_sorted:
            if ( atom.symbol == 'O' ):
                loc = atom.index
                res = loc - prvO
                if ( loc == 0 and prvO == -3 ):
                    print ('Beginning check for oxygen positions - right order if you see nothing but this message.')
                    prvO += 3
                    continue
                elif ( res == 3 and loc != 0 ):
                    prvO += 3
                    continue
                elif ( res != 3 and prvO != -3 and loc != 0):
                    print ('Holy sorting error, Batman!')
                    break
                else:
                    print ('Something is amiss - check that your PDB begins with oxygen.')
                    break
    else:
        out = write('%s-sorted.pdb' % (filename), inp_sorted, format='proteindatabank')
