#This is a script that uses parmed to get the epsilon and sigma for each atom
import parmed
parm = parmed.load_file('cvmethanol.prmtop')
for atom in parm.atoms:
    print(atom.type, atom.rmin, atom.epsilon)

