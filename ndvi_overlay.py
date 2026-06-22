import rasterio
import rasterio.plot
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

# Load NDVI bands
base = r"C:\Users\pdeva\ndvi-project"
red = rasterio.open(base + "\\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B04.tiff").read(1).astype(float)
nir = rasterio.open(base + "\\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B08.tiff").read(1).astype(float)
src = rasterio.open(base + "\\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B08.tiff")

np.seterr(divide='ignore', invalid='ignore')
ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))

# Load boundary
boundary = gpd.read_file(base + "\\warangal_boundary.geojson")
boundary = boundary.to_crs(src.crs)

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
rasterio.plot.show(ndvi, transform=src.transform, ax=ax, cmap='RdYlGn', vmin=-1, vmax=1)
boundary.boundary.plot(ax=ax, color='blue', linewidth=2, label='Warangal Region')
ax.set_title('NDVI with Boundary - Warangal, Telangana (Jun 16, 2026)')
ax.legend()
plt.savefig('ndvi_overlay.png', dpi=150, bbox_inches='tight')
plt.show()