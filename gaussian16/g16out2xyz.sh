#!/bin/bash

echo "Convert Gaussian output to XYZ using OpenBabel."

for i in *.out; do
 x=${i%.out}
 fil=`echo ${x##*/}` 
 if grep -q "Optimization completed" $fil\.out; then
  obabel -iout $fil\.out -oxyz -O$fil\.xyz
 fi
done

