# This script converts XYZ files to PDB files by utilizing the OpenBabel module.

import os
import subprocess

# Create a directory for PDB files if it does not exist
pdb_dir = "pdbfiles"
if not os.path.exists(pdb_dir):
    os.mkdir(pdb_dir)

xyz_dir = "xyzfiles" # This is your folder name with the XYZ files
xyz_files = [f for f in os.listdir(xyz_dir) if f.startswith("gsopted") and f.endswith(".xyz")]

for xyz_file in xyz_files:
    xyz_path = os.path.join(xyz_dir, xyz_file)
    pdb_filename = os.path.splitext(xyz_file)[0] + ".pdb"
    pdb_path = os.path.join(pdb_dir, pdb_filename)
    
    # Convert XYZ to PDB using Open Babel (assuming Open Babel is installed)
    subprocess.run(["obabel", "-ixyz", xyz_path, "-opdb", "-O", pdb_path])
    
    print(f"Converted {xyz_path} to {pdb_path}")

print("Conversion complete.")
