# Standard Operating Workflow

1. **Ingest:** Download hydrodynamic subsets via `01_copernicus_data_download.ipynb` and place restricted NUPRC rasters in `02_data_raw/` (excluded from Git).
2. **Qualify:** Run `02_mdc_bcr_template.ipynb` to mask vertical sonar noise and export qualified rasters to `03_data_processed/`.
3. **Extract & Cluster:** Run `03_terrain_parameters.ipynb` and `04_spatial_autocorrelation.ipynb` to generate terrain predictors and LISA maps.
4. **Model & Publish:** Train the MVI model in `05_xgboost_mvi_template.ipynb` and export 300 DPI manuscript figures via `06_conference_paper_figures.ipynb` to `07_figures/`.
