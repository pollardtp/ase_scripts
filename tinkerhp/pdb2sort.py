#!/p/home/teep/.local_programs/conda3/bin/python

import ase, glob, os, sys
import ase.io
import ase.build
from ase import Atom, Atoms, neighborlist

dir_ = os.getcwd()

check = False

for file_ in glob.glob('%s/*.pdb' % dir_):
    filename_, fileext_ = os.path.splitext(file_) # fileext_ carries the .
    inp_ = ase.io.read('%s%s' % (filename_, fileext_) , format='proteindatabank')

    # Here we want atom order to repeat units of OHH, OHH, ..., Cl, Li
    # sort and push hydrogen to end, else there are indexing issues
    for atom in inp_:
        if ( atom.symbol == 'H' ):
           atom.mass = 9999. 

    # hydrogens are now last
    inp_clean_ = ase.build.sort(inp_, tags = inp_.get_masses())

    # compute distances, save lists of indices - i_dex contains O and H
    i_dex, j_dex, ij_dis = neighborlist.neighbor_list('ijd', inp_clean_, {('H', 'H'): 0.0, ('O', 'O'): 0.0, ('O', 'H'): 0.9}, self_interaction=False)

    # tag each water with the index of the oxygen, the ith water
    for ith in range(len(i_dex)):
        if ( inp_clean_[i_dex[ith]].symbol == 'O' ):
            inp_clean_[i_dex[ith]].tag = i_dex[ith]
            inp_clean_[j_dex[ith]].tag = i_dex[ith]

    # tag the other atoms, just number them in the order you want to see them
    for atom in inp_clean_:
        if ( atom.symbol == 'Cl' ):
            atom.tag = 9999998
        if ( atom.symbol == 'Li' ):
            atom.tag = 9999999

    # sort the reindexed list by water molecule - now H index is > O index, proper order!
    inp_sorted_ = ase.build.sort(inp_clean_, tags=inp_clean_.get_tags())

    # give option for testing without writing anything
    if ( check == True ):
        prvO = -3
        for atom in inp_sorted_:
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
        out_ = ase.io.write('%s-sorted.pdb' % (filename_), inp_sorted_, format='proteindatabank')

