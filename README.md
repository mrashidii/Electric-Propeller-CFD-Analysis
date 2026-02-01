# Electric Propeller CFD Analysis: From Bernoulli to Navier-Stokes

**Author:** Mohammad Rashidi  
**Semester:** WiSe 2025/26  
**Description:** A Python-based aerodynamic analysis suite for the NACA 4412 airfoil, transitioning from inviscid potential flow to viscous Navier-Stokes modeling. Validated against XFOIL.

---

## 1. Geometry Generation
**File:** `naca_geometry.py`

**Description:**
This module is responsible for generating the analytical coordinates of the **NACA 4412** profile. It implements the standard NACA 4-digit series equations to calculate the mean camber line and thickness distribution separately, then combines them to produce the upper and lower surface coordinates required for the mesh generation.

```python
import numpy as np

def generate_naca_4412(chord=1.0, n_points=100):
    """
    Generates x, y coordinates for NACA 4412.
    Parameters: m=0.04 (Max Camber), p=0.40 (Position), t=0.12 (Thickness)
    """
    x = np.linspace(0, chord, n_points)
    
    # 1. Calculate Mean Camber Line (yc)
    # Using piecewise function for forward and aft camber
    yc = np.where(x < 0.4 * chord,
                  (0.04 / 0.4**2) * (2 * 0.4 * (x/chord) - (x/chord)**2),
                  (0.04 / (1-0.4)**2) * ((1 - 2*0.4) + 2*0.4*(x/chord) - (x/chord)**2))
    
    # 2. Calculate Thickness Distribution (yt)
    yt = 5 * 0.12 * (0.2969 * np.sqrt(x/chord) - 0.1260*(x/chord) - ... )
    
    return x, yc, yt
