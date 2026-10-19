# Prepara la imagen Sentinel-2 del Refugio Nacional de Vida Silvestre
# Gandoca-Manzanillo usada en el cuaderno de rasterio.
#
# Busca en el catálogo STAC de Microsoft Planetary Computer la escena
# Sentinel-2 L2A del 4 de febrero de 2024 (tesela 17PLL, 7,5 % de nubes),
# lee de los COG originales la ventana que cubre la parte terrestre del
# refugio y escribe gandoca-20240204.tif con cuatro bandas de 10 m:
# azul (B02), verde (B03), roja (B04) e infrarroja cercana (B08), uint16,
# en EPSG:32617 (WGS 84 / UTM zona 17N, el SRC nativo de la escena).
#
# Uso (requiere rasterio y requests):
#   python3 preparar-datos.py

import os

import rasterio
import requests
from rasterio.windows import from_bounds

STAC = "https://planetarycomputer.microsoft.com/api/stac/v1/search"
TOKEN = "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel-2-l2a"
ESCENA = "S2B_MSIL2A_20240204T160509_R054_T17PLL_20240204T213428"
BANDAS = {"B02": "Azul (B02)", "B03": "Verde (B03)", "B04": "Roja (B04)", "B08": "NIR (B08)"}

# Límites de la parte terrestre del refugio, en EPSG:32617 (oeste, sur, este, norte)
LIMITES = (312120, 1054330, 330230, 1066640)
DESTINO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gandoca-20240204.tif")

# Búsqueda de la escena y firma de las direcciones (token de acceso gratuito)
respuesta = requests.post(STAC, json={"collections": ["sentinel-2-l2a"], "ids": [ESCENA]})
respuesta.raise_for_status()
escena = respuesta.json()["features"][0]
token = requests.get(TOKEN).json()["token"]

bandas = []
for banda in BANDAS:
    url = escena["assets"][banda]["href"] + "?" + token
    with rasterio.open(url) as src:
        ventana = from_bounds(*LIMITES, transform=src.transform).round_offsets().round_lengths()
        bandas.append(src.read(1, window=ventana))
        perfil = src.profile
        transformacion = src.window_transform(ventana)
    print("Leída", banda, bandas[-1].shape)

perfil.update(driver="GTiff", count=len(bandas), dtype="uint16", nodata=0,
              height=bandas[0].shape[0], width=bandas[0].shape[1],
              transform=transformacion, compress="deflate", predictor=2, zlevel=9, tiled=False)
perfil.pop("blockxsize", None)
perfil.pop("blockysize", None)
with rasterio.open(DESTINO, "w", **perfil) as dst:
    for i, (banda, descripcion) in enumerate(BANDAS.items(), start=1):
        dst.write(bandas[i - 1], i)
        dst.set_band_description(i, descripcion)
    dst.update_tags(fecha="2024-02-04", escena=ESCENA, fuente="Microsoft Planetary Computer, Sentinel-2 L2A")
print("Escrito", DESTINO)
