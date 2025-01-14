# The interatomic distances are computed using MDAnalysis
import os
import MDAnalysis as mda
frameanddistancen10c4 = []
for i in range(1, 3):  
    file_path = os.path.join('xyzfiles/', f'f{i}.xyz')
    u = mda.Universe(file_path)
    selected_atoms = u.atoms[:32] # This selects so only the first 32 atoms are considered, which was the case for cresyl violet dye with 32 atoms
    n10 = selected_atoms[10]  # Atoms start with index 0
    c4 = selected_atoms[4]  
    n10c4distance = mda.lib.distances.distance_array(n10.position, c4.position)[0][0] # Computes distances between nitrogen and carbon
    frameanddistancen10c4.append((i, n10c4distance))
print(frameanddistancen10c4)
