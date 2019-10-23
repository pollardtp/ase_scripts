# README

Series of scripts to perform common tasks in CP2K.

dumpdcd is modified version of the CP2K file where I change the format of the 
title line. TRAVIS (trajectory analyzer) can now read 
`x-ang y-ang z-ang alpha-deg beta-deg gamma-deg` from the title card.

xyzcell2gro.py is a script for converting an XYZ trajectory in combination with
a text file containing `step# time(fs) ax ay az bx by bz cx cy cz vol` to Gromos96 
format for visualization with VMD. This is a script to save your bacon if you run 
variable cell calculations without printing a DCD trajectory.
