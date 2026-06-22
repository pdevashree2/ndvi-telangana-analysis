import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load bands
b04 = rasterio.open(r"C:\Users\pdeva\ndvi-project\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B04.tiff")
b08 = rasterio.open(r"C:\Users\pdeva\ndvi-project\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B08.tiff")

# Read as arrays
red = b04.read(1).astype(float)
nir = b08.read(1).astype(float)

# Avoid division by zero
np.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))

# Stats
valid = ndvi[ndvi != 0]
print(f"Mean NDVI:  {valid.mean():.3f}")
print(f"Min NDVI:   {valid.min():.3f}")
print(f"Max NDVI:   {valid.max():.3f}")
print(f"Healthy vegetation (NDVI > 0.3): {(valid > 0.3).sum() / len(valid) * 100:.1f}%")
print(f"Stressed vegetation (0 < NDVI < 0.3): {((valid > 0) & (valid < 0.3)).sum() / len(valid) * 100:.1f}%")
print(f"Non-vegetation (NDVI < 0): {(valid < 0).sum() / len(valid) * 100:.1f}%")

# Plot
plt.figure(figsize=(10, 10))
plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
plt.colorbar(label='NDVI')
plt.title('NDVI - Warangal, Telangana (June 16, 2026)')
plt.axis('off')
plt.savefig('ndvi_telangana.png', dpi=150, bbox_inches='tight')
plt.show()