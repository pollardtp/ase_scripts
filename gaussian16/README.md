# Gaussian 16
-----

The gaussian.py file is a modified version of the gaussian.py calculator included with ASE. It hijacks the addsec keyword for the purpose of writing
generic solvent data to the input file.

xyz2g16.py converts standard XYZ/XMOL format files to gjf input files. The multiplicity is not calculated, so charge and multiplicity are set to '0 1'
by default.

