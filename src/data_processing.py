import numpy as np
import xarray as xr

def calculate_current_speed(u: xr.DataArray, v: xr.DataArray) -> xr.DataArray:
    """Compute sea surface current magnitude from u and v velocity components."""
    speed = np.sqrt(u**2 + v**2)
    speed.name = "current_speed"
    speed.attrs["units"] = "m/s"
    return speed

def calculate_mdc(sigma_z1: float, sigma_z2: float) -> float:
    """Compute Minimum Detectable Change (MDC) at 95% confidence level (IHO S-44)."""
    return 1.96 * np.sqrt(sigma_z1**2 + sigma_z2**2)

def compute_qualified_bcr(grid_t1: xr.DataArray, grid_t2: xr.DataArray, mdc: float, years: float) -> xr.DataArray:
    """Compute uncertainty-qualified annualized Bathymetric Change Rate (BCR)."""
    diff = grid_t2 - grid_t1
    qualified = xr.where(np.abs(diff) >= mdc, diff, np.nan)
    bcr = qualified / years
    bcr.name = "BCR"
    bcr.attrs["units"] = "m/yr"
    return bcr
