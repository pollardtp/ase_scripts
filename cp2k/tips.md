Narrowing energy differences per atom in materials with differing surface areas
-----

A basic template procedure
- Cell optimization with gamma point sampling
- Cell optimization with 2 or 3 k-points padding on smaller dimensions (for graphite, important for stacking dimension)
- At this point, the lattice vectors should be proportional to one another (or identical if the structures share a common dimension)
- Now perform a geometry optimization with a k-point distribution (k*Latt_Vec) for each dimension matching the least common multiple
- If CP2K hangs during the geometry optimization, reduce the k-point of the dimension with the greatest length by 1 and try again
- Restore the k-point scheme if it was changed and compute the energy, report this one
- Ex. (graphite with 96, 160, and 192 atoms) gives -155.130120, -155.130129, -155.130226 eV/atom following this method

