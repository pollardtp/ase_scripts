"""
JDFTx format lattice READ ONLY
"""

from ase.atoms import Atoms

__all__ = ['read_jdftlat']

bohr2ang = 1 / 0.52917721067 # from CODATA

def read_jdftlat(fileobj):
    lines = fileobj.readlines()
    vects = int(len(lines))
    latt = []
    for line in lines[1:vects]:
        x, y, z, endl = line.split()[:4]
        latt.append([float(x)/bohr2ang, float(y)/bohr2ang, float(z)/bohr2ang])
    return latt

