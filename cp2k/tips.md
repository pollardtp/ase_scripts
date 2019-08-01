# Narrowing energy differences per atom in materials with differing surface areas

A basic template procedure
- Cell optimization with gamma point sampling
- Cell optimization with 2 or 3 k-points padding on smaller dimensions (for graphite, important for stacking dimension)
- At this point, the lattice vectors should be proportional to one another (or identical if the structures share a common dimension)
- Now perform a geometry optimization with a k-point distribution (k*Latt_Vec) for each dimension matching the least common multiple
- If CP2K hangs during the geometry optimization, reduce the k-point of the dimension with the greatest length by 1 and try again
- Restore the k-point scheme if it was changed and compute the energy, report this one
- Ex. (graphite with 96, 160, and 192 atoms) gives -155.130120, -155.130129, -155.130226 eV/atom following this method

# Cell optimizations (or constant pressure simulations) with metals

Problem: The Broyden method for converging SCF with Fermi smearing is quick and robust, making it an ideal choice. However,
in cell optimizations, I find that it locks up after a few optimization steps and the calculation hangs (rests idle until walltime).
I have only ever had this issue with the Broyden method.

1st Solution: Switch to the Pulay/DIIS method. It may take a few extra SCF cycles to get to the solution though and can be led
astray for poor geometries so as to never converge. Also falls prey to spurious R_COND errors.

Fallback solution: Run Kerker a few cycles so that Pulay will be stable, then switch to Pulay. I find that Kerker often struggles
with SCF convergence on the initial geometry and (when things go wrong) will diverge after about 10 cycles or so. The multisecant 
method is not recommended, at all.

```
   &MIXING  T
    METHOD  PULAY_MIXING
    N_SIMPLE_MIX  5 # this requests Kerker for 5 SCF cycles, technically NoDiag + 4 Kerker
    PULAY_ALPHA  0.02 # actually a VASP recommendation for metals
    NMIXING  10
    NBUFFER  8
   &END MIXING
```

