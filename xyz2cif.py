#!/usr/bin/env python
import ase, sys
from ase import Atom, Atoms
import ase.io

# read xyz
slab = ase.io.read(sys.argv[1], format='xyz');

print(slab)
# Read this info from a log file or restart, or define it manually as I 
#have below; you can do cell shape as well, but here it is alpha=beta=gamma= 
#90 deg
#_cell_length_a                         11.47850
#_cell_length_b                         11.65350
#_cell_length_c                         24.67610
slab.set_cell([3.2671220382, 5.5133116229, 14.8768877246])

# output to the file type of choice; by default cif is in fractional 
#coordinates, VASP/CONTCAR/POSCAR needs 'direct=True' to do the same
vasp = ase.io.write(sys.argv[2], slab, format='cif');
