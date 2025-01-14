import os
import MDAnalysis as mda
frameanddistancen10c4 = []
for i in range(1, 3):  # Assumes you have f1.xyz to f5.xyz
    file_path = os.path.join('xyzfiles/', f'f{i}.xyz')
    u = mda.Universe(file_path)
    selected_atoms = u.atoms[:32]
    n10 = selected_atoms[10]  # Assuming atom with index 0
    c4 = selected_atoms[4]  # Assuming atom with index 1
    n10c4distance = mda.lib.distances.distance_array(n10.position, c4.position)[0][0]
    frameanddistancen10c4.append((i, n10c4distance))
print(frameanddistancen10c4)
