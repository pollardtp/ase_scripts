# README

Python source code for using the atomic simulation environment (ASE) to accomplish various tasks from converting formats to setting up
calculations.

Source is written with the following practices,

  1) Variables labeled as `foo_` with an underscore appended to their end to remain obviously distinct
  2) Where possible, written to be run in any directory (the Python script does not need to be located in `cwd`)
  3) glob is used to chew up all files in a directory and make whatever modifications are called
  4) Written to Python3 standards. Not guaranteed to work with Python2, but should mostly be OK.
