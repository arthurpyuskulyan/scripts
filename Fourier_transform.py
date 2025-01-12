# This script Fourier tranforms from the time domain to the frequency domain.
# It also verifies the Fourier transform procedure is correct
# by checking and showing that the numerical Fourier transform of a 
# Gaussian is a Gaussian and it equals the analytical expression.
# 

import numpy as np
import matplotlib.pyplot as plt

# Define the width of the Gaussian in time and frequency domains
sigma = 20  # Standard deviation (controls the width of the Gaussian)

# Define the frequency range
w = np.arange(-0.25, 0.25, 0.001)  # Frequency grid

# Analytical Fourier Transform of a Gaussian in time:
# If the time-domain function is: ct(t) = exp(-t^2 / (2 * sigma^2)),
# The frequency-domain function is: cw(w) = sigma * sqrt(2*pi) * exp(-w^2 * sigma^2 / 2).
cw = sigma * np.sqrt(2 * np.pi) * np.exp(-w * w * sigma * sigma / 2.0)

# Plot the analytical Fourier transform (frequency domain Gaussian)
plt.plot(w, cw)  # Orange solid line represents the analytical result
plt.show()


sigma = 20
w = np.arange(-0.25, 0.25, 0.001)  # Frequency grid
t = np.arange(-100, 100, 1)  # Time grid

# Define a Fourier transform function using the trapezoidal rule
def fourier_transform_trapezoid(t, w, time_func):
    # Calculate time step
    dt = t[1] - t[0]  # Step size in the time domain

    # Initialize the result array for the Fourier transform
    fw = np.zeros(len(w), dtype=complex)

    # Loop over the frequencies
    for i in range(len(w)):
        # Define the integrand for Fourier transform:
        # f(t) = exp(i * w * t) * time_func(t)
        f = np.exp(complex(0, 1) * w[i] * t) * time_func  
        
        # Numerically integrate f(t) over t using the trapezoidal rule:
        # fw(w) = ∫ f(t) dt ≈ Σ f(t_k) * Δt
        fw[i] = np.trapz(f, dx=dt)

    return fw

# Define the time-domain Gaussian:
# ct(t) = exp(-t^2 / (2 * sigma^2))
time_func = np.exp((-t**2) / (2 * sigma * sigma))

# Compute the numerical Fourier transform of time_func
fw_with_time_func = fourier_transform_trapezoid(t, w, time_func)
#print(fw_with_time_func)  # Prints the complex Fourier transform values



# Plot the numerical Fourier transform (dashed blue line)
plt.plot(w, fw_with_time_func, linestyle='dashed', color='blue',label='Numerical')
# Plot the analytical Fourier transform (dotted orange line)
plt.plot(w, cw, linestyle='dotted', color='orange',label='Analytical')
plt.xlabel('Frequency (w)')
plt.ylabel('F(w)')
plt.legend()
# Show both the numerical (blue) and analytical (orange) results
plt.show()
