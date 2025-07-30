#Convert .dcd to .xyz
import mdtraj as md

# load the trajectory (needs the topology, e.g., PSF or PDB)
traj = md.load('traj.dcd', top='structure.pdb')

# save as XYZ
traj.save('traj.xyz')