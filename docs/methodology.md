# Research Methodology Summary

1. **Uncertainty Qualification (MDC & BCR):** Multi-epoch MBES bathymetric surfaces are differenced and filtered using a 95% confidence Minimum Detectable Change threshold: $MDC = 1.96 \sqrt{\sigma_{z1}^2 + \sigma_{z2}^2}$.
2. **Geomorphometric Extraction:** Slope Gradient, Aspect, and Seabed Roughness Index (SRI) are derived from qualified Digital Terrain Models.
3. **Spatial Autocorrelation:** Global Moran's I and Local Indicators of Spatial Association (LISA) identify statistically significant scour and deposition clusters ($p < 0.05$).
4. **Probabilistic Risk Modelling (MVI):** An XGBoost classifier fuses hydrodynamic, geomorphometric, and burial parameters to predict pipeline free-span vulnerability, interpreted via SHAP values.
