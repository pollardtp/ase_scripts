# README

This archive contains scripts useful for running JDFTx and converting between
CIF files (or other formats with modification) and the JDFTx ionpos and lattice
formats. These scripts natively handle the Angstrom to au (cif2jdft) and au to
Angstrom (jdft2cif) unit conversions. The conversion is run using ASE. The
JDFTx.py script is the ase.calculator while the jdftion and jdftlat scripts are
ase.io formats. These scripts assume you treat io with JDFTx like you do with
VASP (i.e., it does everything for you). If JDFTx wrote it and you didn't touch
it - it should work.
