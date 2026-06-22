import rasterio
import numpy as np
import matplotlib.pyplot as plt

b04 = rasterio.open(r"C:\Users\pdeva\Downloads\Browser_images (1)\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B04.tiff")
b08 = rasterio.open(r"C:\Users\pdeva\Downloads\Browser_images (1)\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B08.tiff")

red = b04.read(1).astype(float)
nir = b08.read(1).astype(float)

ndvi = (nir - red) / (nir + red)

plt.figure(figsize=(10, 10))
plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
plt.colorbar(label='NDVI')
plt.title('NDVI - Warangal, Telangana (June 16, 2026)')
plt.axis('off')
plt.savefig('ndvi_telangana.png', dpi=150, bbox_inches='tight')
plt.show()
