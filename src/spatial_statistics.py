import numpy as np
import geopandas as gpd
import libpysal
from esda.moran import Moran, Moran_Local

def run_spatial_autocorrelation(gdf: gpd.GeoDataFrame, column: str, k: int = 8):
    """Run Global Moran's I and Local Moran's I (LISA) hot-spot classification."""
    w = libpysal.weights.KNN.from_dataframe(gdf, k=k)
    w.transform = "r"
    moran_global = Moran(gdf[column], w)
    moran_local = Moran_Local(gdf[column], w)

    gdf = gdf.copy()
    gdf["lisa_q"] = moran_local.q
    gdf["lisa_p"] = moran_local.p_sim

    sig = gdf["lisa_p"] < 0.05
    labels = np.full(len(gdf), "Not Significant", dtype=object)
    labels[sig & (gdf["lisa_q"] == 1)] = "High-High (Scour Hot-Spot)"
    labels[sig & (gdf["lisa_q"] == 3)] = "Low-Low (Cold-Spot)"
    labels[sig & (gdf["lisa_q"] == 2)] = "Low-High (Outlier)"
    labels[sig & (gdf["lisa_q"] == 4)] = "High-Low (Outlier)"
    gdf["cluster"] = labels
    return moran_global, gdf
