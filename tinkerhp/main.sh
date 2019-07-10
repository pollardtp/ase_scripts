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
    if grep -q "[OHil]   MOL" $file\.pdb; then
      sed -i s~"O   MOL"~" O  MOL"~g $file\.pdb
      sed -i s~"H   MOL"~" H  MOL"~g $file\.pdb
      sed -i s~"Li   MOL"~" Li  MOL"~g $file\.pdb
      sed -i s~"Cl   MOL"~" Cl  MOL"~g $file\.pdb
    fi
  
    # case: trailing characters mess up spacing, first charcater is a number - if sorted with ASE no changes
    if grep -q "[OHil][0-9].* MOL" $file\.pdb; then
      sed -i s~"O[0-9].* MOL"~" O  MOL"~g $file\.pdb
      sed -i s~"H[0-9].* MOL"~" H  MOL"~g $file\.pdb
      sed -i s~"Li[0-9].* MOL"~" Li  MOL"~g $file\.pdb
      sed -i s~"Cl[0-9].* MOL"~" Cl  MOL"~g $file\.pdb
    fi
  
    # generate xyz
    ~/.local_programs/tinker.oleg/bin/pdbxyz $file\.pdb amoddedbabio18.prm
  
    sed -i s~"LI"~"Li"~g $file\.xyz
    sed -i s~"CL"~"Cl"~g $file\.xyz
    sed -i s~"ZN"~"Zn"~g $file\.xyz
    mv $file\.xyz $file\.xyz_orig
    ./set_tink_atom_type.sh $file\.xyz_orig > $file\.xyz
    boxbox=`grep CRYST1 $file\.pdb | awk '{print $2}'`
    sed s~"BOXBOX"~"$boxbox"~g generic.key > $file\.key
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
    ~/.local_programs/tinker.oleg/bin/pdbxyz $file\-sorted.pdb amoddedbabio18.prm

    sed -i s~"LI"~"Li"~g $file\-sorted.xyz
    sed -i s~"CL"~"Cl"~g $file\-sorted.xyz
    sed -i s~"ZN"~"Zn"~g $file\-sorted.xyz
    mv $file\-sorted.xyz $file\.xyz_orig
    ./set_tink_atom_type.sh $file\.xyz_orig > $file\.xyz
    boxbox=`grep CRYST1 $file\.pdb | awk '{print $2}'`
    sed s~"BOXBOX"~"$boxbox"~g generic.key > $file\.key
    #tar cf $file\.tar $file\.xyz $file\.key
  done
fi

