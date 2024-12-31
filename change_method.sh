#!/bin/bash

# This script changes the method in the inputfile. It is especially 
# useful when have it have many folders, which can be looped through 
# example of loop usage  for i in {1..10}; do cd "$i"; bash ../change_method.sh; cd ..; done


sed -i -e 's/METHOD FC/METHOD CUMULANT/g'  inputfile
