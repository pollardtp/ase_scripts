#!/usr/bin/env python3

def check_ase():

    import pkg_resources
    from pkg_resources import DistributionNotFound, VersionConflict
    import sys

    try:
        pkg_resources.require("ase>=3.15.0")
    except pkg_resources.DistributionNotFound:
        print('Exiting: Atomic Simulation Environment not found.')
        sys.exit()
    except pkg_resources.VersionConflict:
        print('Exiting: Older version of ASE installed, please update.')
        sys.exit()

    del sys.modules["pkg_resources"]
    del pkg_resources
