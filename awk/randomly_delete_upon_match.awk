#!/bin/awk

# reads file, searches for FOO, deletes half of the occurences
awk '!/FOO/ || rand() >= 0.5' file

