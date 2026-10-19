# Prepara las capas raster de WorldClim 2.1 usadas en el cuaderno de rasterio.
#
# Descarga los archivos originales (ZIP con GeoTIFF, uno por mes para las
# variables climáticas) de https://geodata.ucdavis.edu/climate/worldclim/2_1/base/
# y escribe en este directorio:
#
#   altitud.tif                  altitud (m), 10 minutos de arco, int16
#   temperatura.tif              temperatura media anual (°C), 10', float32
#   precipitacion.tif            precipitación anual (mm), 10', int16
#   altitud-centroamerica.tif    altitud (m), 2,5 minutos de arco, recortada
#                                a Centroamérica, int16
#
# Uso (requiere rasterio y numpy):
#   python3 preparar-datos.py [directorio_con_los_zip]
# Si se indica un directorio que ya contiene los ZIP, no se vuelven a descargar.

import os
import sys
import tempfile
import urllib.request
import zipfile

import numpy as np
import rasterio
from rasterio.windows import from_bounds

BASE = "https://geodata.ucdavis.edu/climate/worldclim/2_1/base/"
ARCHIVOS = ["wc2.1_10m_elev", "wc2.1_10m_tavg", "wc2.1_10m_prec", "wc2.1_2.5m_elev"]
DESTINO = os.path.dirname(os.path.abspath(__file__))

# Límites de Centroamérica (Guatemala a Panamá), en grados
CENTROAMERICA = (-93, 7, -77, 19)  # oeste, sur, este, norte

directorio = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp()
os.makedirs(directorio, exist_ok=True)

for nombre in ARCHIVOS:
    ruta_zip = os.path.join(directorio, nombre + ".zip")
    if not os.path.exists(ruta_zip):
        print("Descargando", nombre)
        urllib.request.urlretrieve(BASE + nombre + ".zip", ruta_zip)
    with zipfile.ZipFile(ruta_zip) as z:
        z.extractall(os.path.join(directorio, nombre))


def escribir(ruta, datos, perfil, nodata, dtype, descripcion):
    """Escribe una capa de una banda, comprimida, con nodata y descripción."""
    perfil = perfil.copy()
    perfil.update(driver="GTiff", count=1, dtype=dtype, nodata=nodata,
                  compress="lzw", tiled=False)
    perfil.pop("blockxsize", None)
    perfil.pop("blockysize", None)
    with rasterio.open(ruta, "w", **perfil) as dst:
        dst.write(datos.astype(dtype), 1)
        dst.set_band_description(1, descripcion)
    print("Escrito", os.path.basename(ruta), datos.shape, dtype)


# Altitud a 10' (SRTM remuestreado por WorldClim)
with rasterio.open(os.path.join(directorio, "wc2.1_10m_elev", "wc2.1_10m_elev.tif")) as src:
    perfil = src.profile
    altitud = src.read(1)
    escribir(os.path.join(DESTINO, "altitud.tif"), altitud, perfil, src.nodata,
             "int16", "Altitud (m)")

# Temperatura media anual: promedio de los 12 meses (float32, nodata de WorldClim)
meses = []
for m in range(1, 13):
    with rasterio.open(os.path.join(directorio, "wc2.1_10m_tavg", f"wc2.1_10m_tavg_{m:02d}.tif")) as src:
        meses.append(src.read(1, masked=True))
        perfil, nodata = src.profile, src.nodata
temperatura = np.ma.mean(np.ma.stack(meses), axis=0).filled(nodata)
escribir(os.path.join(DESTINO, "temperatura.tif"), temperatura, perfil, nodata,
         "float32", "Temperatura media anual 1970-2000 (°C)")

# Precipitación anual: suma de los 12 meses (int16)
meses = []
for m in range(1, 13):
    with rasterio.open(os.path.join(directorio, "wc2.1_10m_prec", f"wc2.1_10m_prec_{m:02d}.tif")) as src:
        meses.append(src.read(1, masked=True).astype("int32"))
        perfil = src.profile
precipitacion = np.ma.sum(np.ma.stack(meses), axis=0).filled(-32768)
escribir(os.path.join(DESTINO, "precipitacion.tif"), precipitacion, perfil, -32768,
         "int16", "Precipitación anual 1970-2000 (mm)")

# Altitud de Centroamérica a 2,5' (ventana de lectura con los límites)
with rasterio.open(os.path.join(directorio, "wc2.1_2.5m_elev", "wc2.1_2.5m_elev.tif")) as src:
    ventana = from_bounds(*CENTROAMERICA, transform=src.transform)
    ventana = ventana.round_offsets().round_lengths()
    altitud_ca = src.read(1, window=ventana)
    perfil = src.profile
    perfil.update(height=altitud_ca.shape[0], width=altitud_ca.shape[1],
                  transform=src.window_transform(ventana))
    escribir(os.path.join(DESTINO, "altitud-centroamerica.tif"), altitud_ca, perfil,
             src.nodata, "int16", "Altitud (m)")
