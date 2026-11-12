import numpy as np
import scipy.ndimage as ndimage

def compute_slope_and_aspect(elevation: np.ndarray, cell_size: float = 2.0):
    """Compute Slope Gradient (degrees) and Aspect (degrees from North) via Horn's method."""
    dz_dx = ndimage.sobel(elevation, axis=1) / (8.0 * cell_size)
    dz_dy = ndimage.sobel(elevation, axis=0) / (8.0 * cell_size)
    slope = np.arctan(np.sqrt(dz_dx**2 + dz_dy**2)) * (180.0 / np.pi)
    aspect = np.arctan2(-dz_dy, dz_dx) * (180.0 / np.pi)
    aspect = np.where(aspect < 0, aspect + 360.0, aspect)
    return slope, aspect

def compute_roughness(elevation: np.ndarray, window_size: int = 3) -> np.ndarray:
    """Compute Seabed Roughness Index (SRI) using moving window standard deviation."""
    return ndimage.generic_filter(elevation, np.std, size=window_size)
