import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt


# Liste der Einzugsgebiete
dateien = {
    1: "C:/Users/n-bel/BA_Code/input_data/catchments/EZG_Derneburg.shp",
    2: "C:/Users/n-bel/BA_Code/input_data/catchments/EZG_Pionierbrücke.shp",
    3: "C:/Users/n-bel/BA_Code/input_data/catchments/EZG_Weitzmühlen.shp",
}

def get_catchment_gdf(datei_id):
    if datei_id in dateien:
        dateipfad = dateien[datei_id]
        gdf = gpd.read_file(dateipfad)
        gdf['name'] = f'Einzugsgebiet {datei_id}'
        return gdf
    else:
        print(f"Datei mit ID {datei_id} nicht gefunden.")
        return None

def plot_catchments():
    fig, ax = plt.subplots()
    for datei_id in dateien:
        gdf = get_catchment_gdf(datei_id)
        if gdf is not None:
            gdf.plot(ax=ax, label=f'Gebiet {datei_id}')
    plt.legend()
    plt.show()