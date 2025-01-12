# This scripts computes the full width half maximum 
# taking in as input the energies and intensities.
def calculate_fwhm(energies, intensities):
    max_intensity = max(intensities)
    half_max = max_intensity / 2

    left_idx = None
    right_idx = None

    for i, intensity in enumerate(intensities):
        if intensity >= half_max:
            left_idx = i
            break

    for i in range(len(intensities) - 1, -1, -1):
        if intensities[i] >= half_max:
            right_idx = i
            break
            

    fwhm = energies[right_idx] - energies[left_idx]
    return fwhm
