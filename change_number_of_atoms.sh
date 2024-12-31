#!/bin/bash

# This script changes the number of atoms and frozen atoms in the inputfile.
# It goes into the xyz file, gets how many atoms there are, and uses that 
# (example 32 is number of atoms of the nonfrozen atoms). It is especially 
# useful it have many folders can run this script on them with. To run with 
# many folders type for i in {1..10}; do cd "$i"; bash ../changenumatoms.sh; cd ..; done


NUM_ATOMS=$(head -n 1 qm.xyz)
NUM_FROZEN_ATOMS=$((NUM_ATOMS - 32))

# Modify inputfile with the extracted numbers
sed -i "s/NUM_ATOMS [0-9]*/NUM_ATOMS $NUM_ATOMS/" inputfile
sed -i "s/NUM_FROZEN_ATOMS [0-9]*/NUM_FROZEN_ATOMS $NUM_FROZEN_ATOMS/" inputfile
