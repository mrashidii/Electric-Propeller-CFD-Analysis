# Electric-Propeller-CFD-Analysis
Aerodynamic modeling of NACA 4412 propeller blades for electric aircraft. This project transitions from Bernoulli's principle to viscous Navier-Stokes analysis, implementing a custom Python solver validated against XFOIL data.
## Code Snippet: Viscous Term Calculation
Here is how the solver calculates the viscous diffusion term:

```python
def calculate_viscous_term(velocity, mu, grid_size):
    # Navier-Stokes Viscous Term: mu * Laplacian(v)
    laplacian_v = np.gradient(np.gradient(velocity, axis=0), axis=0)
    viscous_force = mu * laplacian_v
    return viscous_force
```

