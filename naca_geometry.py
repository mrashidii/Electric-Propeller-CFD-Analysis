
"""
Module: NACA 4412 Geometry Generator
Description: Generates the analytical coordinates for the NACA 4412 airfoil profile.
Methodology: Uses the standard NACA 4-digit series equations to calculate camber line,
             thickness distribution, and upper/lower surface coordinates.
Output: Returns (x, y) coordinates for plotting and mesh generation.
Author: Mohammad Rashidi
"""

import numpy as np
import matplotlib.pyplot as plt

def naca4_coordinates(number, n_points=200):
    """
    Generates coordinates for NACA 4-digit airfoils based on analytical equations.
    Reference: Abbott, I. H., and von Doenhoff, A. E., "Theory of Wing Sections".
    
    Parameters:
    number (str): The 4-digit designation (e.g., '4412').
    n_points (int): Number of points along the chord.
    """
    
    # 1. Decode the NACA 4-digit string
    # m: Maximum camber (1st digit) -> 4 means 4% -> 0.04
    # p: Position of max camber (2nd digit) -> 4 means 40% -> 0.4
    # t: Maximum thickness (3rd & 4th digits) -> 12 means 12% -> 0.12
    m = int(number[0]) / 100.0
    p = int(number[1]) / 10.0
    t = int(number[2:]) / 100.0

    # Discretize the chord length (from 0 to 1)
    x = np.linspace(0, 1, n_points)
    
    # 2. Thickness Distribution Equation (Symmetric Profile)
    # This formula defines the thickness variation along the chord.
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 
                  0.2843 * x**3 - 0.1015 * x**4)

    # 3. Camber Line Calculation (Mean Line)
    yc = np.zeros_like(x)
    dyc_dx = np.zeros_like(x) # Derivative for slope calculation

    for i in range(len(x)):
        if x[i] <= p:
            # Forward of maximum camber position
            yc[i] = (m / p**2) * (2 * p * x[i] - x[i]**2)
            dyc_dx[i] = (2 * m / p**2) * (p - x[i])
        else:
            # Aft of maximum camber position
            yc[i] = (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * x[i] - x[i]**2)
            dyc_dx[i] = (2 * m / (1 - p)**2) * (p - x[i])
            
    # Calculate local slope angle (theta)
    theta = np.arctan(dyc_dx)

    # 4. Final Coordinate Transformation
    # Project thickness perpendicular to the camber line
    xu = x - yt * np.sin(theta)  # Upper surface X
    yu = yc + yt * np.cos(theta)  # Upper surface Y
    xl = x + yt * np.sin(theta)  # Lower surface X
    yl = yc - yt * np.cos(theta)  # Lower surface Y

    return xu, yu, xl, yl, x, yc

# --- Plotting Routine ---

# Generate Data for NACA 4412
xu, yu, xl, yl, xc, yc = naca4_coordinates("4412")

# Create Plot
plt.figure(figsize=(10, 3.5)) # Wide aspect ratio for better presentation

# Plot Airfoil Surface (Filled)
plt.fill_between(xu, yu, y2=yl, color='#D3D3D3', label='NACA 4412 Profile')
plt.plot(xu, yu, 'k-', linewidth=2) # Upper surface outline
plt.plot(xl, yl, 'k-', linewidth=2) # Lower surface outline

# Plot Chord Line (Reference)
plt.plot([0, 1], [0, 0], 'r--', linewidth=1.5, label='Chord Line (c)')

# Plot Mean Camber Line (Optional but technical)
plt.plot(xc, yc, 'b-.', linewidth=1, alpha=0.7, label='Mean Camber Line')

# Labels and Styling
plt.title("Analytic Generation of NACA 4412 Geometry", fontsize=14, fontweight='bold')
plt.xlabel("x / c (Normalized Position)", fontsize=12)
plt.ylabel("y / c (Normalized Thickness)", fontsize=12)
plt.legend(loc='upper right', frameon=True)
plt.axis('equal') # Crucial to maintain correct aspect ratio
plt.grid(True, linestyle=':', alpha=0.6)

# Save and Show
plt.tight_layout()
plt.savefig("Slide3_NACA4412_Geometry.png", dpi=300)
plt.show()