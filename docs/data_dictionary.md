# Data Dictionary

| Variable | Unit | Source | Description |
|---|---|---|---|
| `uo`, `vo` | m/s | Copernicus Marine | Eastward and northward sea surface velocity components |
| `current_speed` | m/s | Derived | Horizontal current magnitude $\sqrt{u^2 + v^2}$ |
| `MDC` | m | Derived (IHO S-44) | 95% confidence vertical detection threshold |
| `BCR` | m/yr | Derived (MBES) | Annualized Bathymetric Change Rate |
| `slope_deg` | degrees | Derived (MBES) | Maximum local seabed inclination |
| `roughness_sri` | m | Derived (MBES) | Local elevation standard deviation (3x3 window) |
| `burial_depth_m` | m | SBP / Magnetometer | Depth of pipeline cover (negative values indicate exposure/free-span) |
| `MVI` | 0–1 | XGBoost Output | Predicted probability of critical free-span vulnerability |
