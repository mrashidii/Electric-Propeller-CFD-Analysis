# Electric Propeller CFD Analysis
**Project:** Transition from Bernoulli to Navier-Stokes for NACA 4412 Airfoil  
**Author:** Mohammad Rashidi

---

## 1. Geometry Generation Code
**Description:**
This code generates the analytical coordinates for the **NACA 4412** airfoil. It uses the standard 4-digit series equations to calculate the thickness distribution and camber line separately, then combines them to output the upper and lower surface coordinates.

```python
# --- File: naca_geometry.py ---
import numpy as np
import matplotlib.pyplot as plt

def generate_naca_4412(n_points=100):
    # NACA 4412 Parameters
    m = 0.04  # Max Camber
    p = 0.40  # Position of Max Camber
    t = 0.12  # Max Thickness
    
    x = np.linspace(0, 1, n_points)
    
    # 1. Thickness Distribution
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 
                  0.2843 * x**3 - 0.1015 * x**4)
    
    # 2. Camber Line
    yc = np.where(x <= p, 
                  (m / p**2) * (2 * p * x - x**2), 
                  (m / (1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2))
    
    # 3. Upper & Lower Surfaces
    theta = np.arctan(np.gradient(yc, x))
    x_upper = x - yt * np.sin(theta)
    y_upper = yc + yt * np.cos(theta)
    x_lower = x + yt * np.sin(theta)
    y_lower = yc - yt * np.cos(theta)
    
    return x_upper, y_upper, x_lower, y_lower

# Visualization
xu, yu, xl, yl = generate_naca_4412()
plt.figure(figsize=(10, 3))
plt.plot(xu, yu, 'b')
plt.plot(xl, yl, 'b')
plt.title("NACA 4412 Geometry")
plt.axis('equal')
plt.grid(True)
# plt.savefig("Slide03_Geometry_Plot.png")
