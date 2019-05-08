"""
JDFTx format ionpos READ ONLY
"""

from ase.atoms import Atoms

__all__ = ['read_jdftion']

bohr2ang = 1 / 0.52917721067 # from CODATA

def read_jdftion(fileobj):
    lines = fileobj.readlines()
    natoms = int(len(lines) - 1) # ignore title card
    symbols = []
    positions = []
    for line in lines[1:natoms]:
        junk, symbol, x, y, z, move = line.split()[:6]
        symbol = symbol.lower().capitalize()
        symbols.append(symbol)
        positions.append([float(x)/bohr2ang, float(y)/bohr2ang, float(z)/bohr2ang])
    yield Atoms(symbols=symbols, positions=positions)

