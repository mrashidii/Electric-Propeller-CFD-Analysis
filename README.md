## 📊 Simulation Results

### 1. Geometry Generation
Analytic generation of the NACA 4412 profile using the custom Python script.
![NACA 4412 Geometry](Geometry_Plot.png)

### 2. CFD Flow Analysis (Pressure Contours)
Visualization of pressure coefficient ($C_p$) and streamlines at $\alpha = 6^{\circ}$. The solver captures the suction peak and stagnation point accurately.
![CFD Results](CFD_Pressure_Contours.png)

### 3. Validation against XFOIL
Comparison of the custom solver results with standard XFOIL data ($Re=10^6$). The correlation ($R^2 > 0.98$) validates the hybrid approach.
![Validation Plot](Validation.png)
