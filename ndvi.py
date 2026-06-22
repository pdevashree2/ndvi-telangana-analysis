import rasterio
import numpy as np
import matplotlib.pyplot as plt


def calc_ndvi(b04_path, b08_path):
    red = rasterio.open(b04_path).read(1).astype(float)
    nir = rasterio.open(b08_path).read(1).astype(float)
    np.seterr(divide="ignore", invalid="ignore")
    ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))
    return ndvi


base = r"C:\Users\pdeva\ndvi-project"

dates = {
    "May 19 2026": (
        base + "\\2026-05-19-00_00_2026-05-19-23_59_Sentinel-2_L2A_B04_(Raw).tiff",
        base + "\\2026-05-19-00_00_2026-05-19-23_59_Sentinel-2_L2A_B08_(Raw).tiff",
    ),
    "Jun 16 2026": (
        base + "\\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B04.tiff",
        base + "\\2026-06-16-00_00_2026-06-16-23_59_Sentinel-2_L2A_B08.tiff",
    ),
    "Aug 05 2025": (
        base + "\\2025-08-05-00_00_2025-08-05-23_59_Sentinel-2_L2A_B04_(Raw).tiff",
        base + "\\2025-08-05-00_00_2025-08-05-23_59_Sentinel-2_L2A_B08_(Raw).tiff",
    ),
}

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
mean_ndvi = []

for ax, (date, (b04, b08)) in zip(axes, dates.items()):
    ndvi = calc_ndvi(b04, b08)
    valid = ndvi[ndvi != 0]
    mean = valid.mean()
    mean_ndvi.append((date, mean))
    im = ax.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
    ax.set_title(date + "\nMean NDVI: " + str(round(mean, 3)))
    ax.axis("off")

plt.colorbar(im, ax=axes, label="NDVI", fraction=0.02)
plt.suptitle("NDVI Time Series - Warangal, Telangana", fontsize=14)
plt.savefig("ndvi_timeseries.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nNDVI Summary:")
for date, mean in mean_ndvi:
    print(date + ": " + str(round(mean, 3)))

    # Bar chart of mean NDVI over time
dates_list = [d for d, _ in mean_ndvi]
means_list = [m for _, m in mean_ndvi]

plt.figure(figsize=(8, 5))
bars = plt.bar(dates_list, means_list, color=['#d4e157', '#8bc34a', '#2e7d32'])
plt.ylim(0, 0.5)
plt.title('Mean NDVI Over Time - Warangal, Telangana')
plt.ylabel('Mean NDVI')
plt.xlabel('Date')
for bar, val in zip(bars, means_list):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
             str(round(val, 3)), ha='center', fontsize=11)
plt.tight_layout()
plt.savefig('ndvi_barchart.png', dpi=150, bbox_inches='tight')
plt.show()