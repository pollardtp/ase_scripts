#!/bin/bash

# This script uses awk to set atom types in Tinker XYZ/arc files and prepend the first line of the XYZ file.

count=`head -n1 $1`
echo $count

awk '{
	if ($2 == "O")
		printf " %s  %s  %s  %s  %s  349  %d  %d\n", $1, $2, $3, $4, $5, ($1 + 1), ($1 + 2);
	else if ($2 == "H" && $1 % 3 == 0)
                printf " %s  %s  %s  %s  %s  350  %d\n", $1, $2, $3, $4, $5, ($1 - 2);
        else if ($2 == "H" && $1 % 3 != 0)
                printf " %s  %s  %s  %s  %s  350  %d\n", $1, $2, $3, $4, $5, ($1 - 1);
	else if ($2 == "Li")
                printf " %s  %s  %s  %s  %s  351\n", $1, $2, $3, $4, $5;
        else if ($2 == "Zn")
                printf " %s  %s  %s  %s  %s  359\n", $1, $2, $3, $4, $5;
	else if ($2 == "Cl")
                printf " %s  %s  %s  %s  %s  360\n", $1, $2, $3, $4, $5;
}' < $1

