#!/bin/bash

if [ ! -f pdb2sort.py ]; then
  echo "Proceeding without ASE sorting, hope that's OK."
  for i in *.pdb; do
    x=${i%.pdb}
    file=`echo ${x##*/}`
  
   # back up, doesn't overwrite
    if [ ! -f $file\.pdb_bak ]; then
      cp $file\.pdb $file\.pdb_bak
    fi
  
    # case: too much space, no trailing characters - if sorted with ASE no changes
    if grep -q "[OH]   HOH" $file\.pdb; then
      sed -i s~"O   HOH"~" O  MOL"~g $file\.pdb
      sed -i s~"H   HOH"~" H  MOL"~g $file\.pdb
    fi
  
    # case: trailing characters mess up spacing, first charcater is a number - if sorted with ASE no changes
    if grep -q "[NL]   LiG" $file\.pdb; then
      sed -i s~"Zn   LiG"~" Zn  MOL"~g $file\.pdb
      sed -i s~"Cl   LiG"~" Cl  MOL"~g $file\.pdb
    fi
  
    # generate xyz
    ~/.local_programs/tinker8.6/bin/pdbxyz $file\.pdb ../params/amoddedbabio18_refitDec2020.prm
  
    mv $file\.xyz $file\.xyz_orig
    ./set_tink_atom_type.sh $file\.xyz_orig > $file\.xyz
    boxbox=`grep CRYST1 $file\.pdb | awk '{print $2}'`
    boxboy=`grep CRYST1 $file\.pdb | awk '{print $3}'`
    boxboz=`grep CRYST1 $file\.pdb | awk '{print $4}'`
    #sed s~"BOXBOX"~"$boxbox"~g generic.key | sed s~"BOXBOY"~"$boxboy"~g | sed s~"BOXBOZ"~"$boxboz"~g > $file\.key
    #tar cf $file\.tar $file\.xyz $file\.key
  done
fi

if [ -f pdb2sort.py ]; then
  echo "Proceeding with ASE sorting."
  python pdb2sort.py

  for i in *-sorted.pdb; do
    x=${i%-sorted.pdb}
    file=`echo ${x##*/}`

    # generate xyz
    ~/.local_programs/tinker8.6/bin/pdbxyz $file\-sorted.pdb ../params/amoddedbabio18_refitDec2020.prm

    sed -i s~"Li"~"Li"~g $file\-sorted.xyz
    sed -i s~"Cl"~"Cl"~g $file\-sorted.xyz
    sed -i s~"Zn"~"Zn"~g $file\-sorted.xyz
    mv $file\-sorted.xyz $file\.xyz_orig
    ./set_tink_atom_type.sh $file\.xyz_orig > $file\.xyz
    boxbox=`grep CRYST1 $file\.pdb | awk '{print $2}'`
    boxboy=`grep CRYST1 $file\.pdb | awk '{print $3}'`
    boxboz=`grep CRYST1 $file\.pdb | awk '{print $4}'`
    #sed s~"BOXBOX"~"$boxbox"~g generic.key | sed s~"BOXBOY"~"$boxboy"~g | sed s~"BOXBOZ"~"$boxboz"~g > $file\.key
    #tar cf $file\.tar $file\.xyz $file\.key
  done
fi
