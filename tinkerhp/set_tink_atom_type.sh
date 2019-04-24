#!/bin/bash

# This script uses awk to set atom types in Tinker XYZ/arc files and prepend the first line of the XYZ file.

count=`head -n1 $1`
echo $count

awk '{
	if ($2 == "O")
		print $1, $2, $3, $4, $5, "349", $7, $8;
	else if ($2 == "H")
		print $1, $2, $3, $4, $5, "350", $7;
	else if ($2 == "LI")
		print $1, $2, $3, $4, $5, "351";
        else if ($2 == "ZN")
                print $1, $2, $3, $4, $5, "359";
	else if ($2 == "CL")
		print $1, $2, $3, $4, $5, "360";
}' < $1

