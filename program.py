import geopandas as gpd
import matplotlib.pyplot as plt

archivo = gpd.read_file("../PredioUPub.json")
barrio_filtrado = archivo[archivo['BARRIOS'].astype(str).str.upper().str.contains("SALITRE SUBA", na=False)].copy()

barrio_filtrado = barrio_filtrado.to_crs(epsg=3116)

barrio_filtrado['Area_M2'] = barrio_filtrado.geometry.area

fig, ax = plt.subplots(figsize=(12, 10))

barrio_filtrado.plot(
    column='Area_M2', 
    cmap='YlOrRd',       
    legend=True, 
    scheme='quantiles', 
    k=5, 
    ax=ax,
    edgecolor='black',   
    linewidth=0.4,
    legend_kwds={'fmt': "{:.0f}"}
)

plt.title("Predios de Salitre (Suba) por Rango de Área en m²", fontsize=14, fontweight='bold')
plt.axis('off') 

plt.tight_layout()
plt.show()