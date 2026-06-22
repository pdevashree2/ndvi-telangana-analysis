import geopandas as gpd
from shapely.geometry import box

# Bounding box around Warangal, Telangana
warangal_bbox = box(79.2, 17.8, 80.2, 18.6)
gdf = gpd.GeoDataFrame({'name': ['Warangal Region']}, geometry=[warangal_bbox], crs='EPSG:4326')
gdf.to_file('warangal_boundary.geojson', driver='GeoJSON')
print("Boundary created!")