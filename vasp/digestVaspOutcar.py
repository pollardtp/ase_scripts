#!/usr/bin/env python3

'''
usage: python3 digestVaspOutcar.py

Uses ASE to gobble up the OUTCAR and return a json outcar with only info of the
final geometry printed.
'''

import glob
import os
import subprocess
import sys

import ase
from ase.io import read, write
from ase import Atom, Atoms
from ase.db import connect

# initialize database
db = connect('outcar.json')

# reads OUTCAR/POTCAR/CONTCAR/POSCAR index [-1]
vo = read('OUTCAR')

# write db
db.write(vo)
