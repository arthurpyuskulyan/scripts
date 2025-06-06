#This is a script that uses parmed to get the epsilon and sigma for each atom
# It gets rmin/2 (Å)   σ (Å)      εpsilon (kcal/mol)    εpsilon (kJ/mol)  
import parmed

parm = parmed.load_file('cresyl_methanol_dorplet.prmtop')

two_sixth = 2 ** (1/6)  # Calculate the sixth root of 2 (~1.12246), used to convert rmin to sigma

print(f"{'Atom':<6} {'Type':<6} {'rmin/2 (Å)':<12} {'σ (Å)':<10} {'ε (kcal/mol)':<15} {'ε (kJ/mol)':<15}")

for atom in parm.atoms:
    rmin_full = atom.rmin * 2      # Convert rmin/2 to rmin (Å)
    sigma = rmin_full / two_sixth  # Convert rmin to sigma (Å)
    epsilon_kcal = atom.epsilon
    epsilon_kj = epsilon_kcal * 4.184
    print(f"{atom.name:<6} {atom.type:<6} {atom.rmin:<12.4f} {sigma:<10.4f} {epsilon_kcal:<15.4f} {epsilon_kj:<15.4f}")

