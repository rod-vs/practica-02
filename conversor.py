
iimport json
import random
from datetime import datetime

# ------------------------------------------------------------
# Carga las tasas de cambio desde un archivo JSON
# ------------------------------------------------------------
def cargar_tasas(ruta):
    with open(ruta, "r") as archivo:
        return json.load(archivo)

# ------------------------------------------------------------
# Convierte el valor en USD a otra moneda según las tasas
# ------------------------------------------------------------
def convertir(precio_usd, moneda_destino, tasas):
    tasa = tasas["USD"].get(moneda_destino)
    
    if not tasa:
        raise ValueError("Moneda no soportada")
    
    return precio_usd * tasa

# ------------------------------------------------------------
# Registra una transacción en un archivo de historial
# ------------------------------------------------------------
def registrar_transaccion(producto, precio_convertido, moneda, ruta_log):
    with open(ruta_log, "a") as archivo:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"{fecha} | {producto}: {precio_convertido:.2f} {moneda}\n")

# ------------------------------------------------------------
# Actualiza las tasas de cambio (simula cambios ±2%)
# ------------------------------------------------------------
def actualizar_tasas(ruta):
    with open(ruta, "r+") as archivo:
        tasas = json.load(archivo)
        for moneda in tasas["USD"]:
            tasas["USD"][moneda] *= 0.98 + (0.04 * random.random())
        tasas["actualizacion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        archivo.seek(0)
        json.dump(tasas, archivo, indent=2)
        archivo.truncate()

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
if __name__ == "__main__":
    # Cargar tasas desde archivo
    tasas = cargar_tasas("../data/tasas.json")

    # Precio base en USD
    precio_usd = 100.00

    # Convertir a euros
    eur = convertir(precio_usd, "EUR", tasas)

    # Registrar la transacción
    registrar_transaccion("Laptop", eur, "EUR", "../logs/historial.txt")

    # 🔹 Probar la nueva función: actualizar tasas
    actualizar_tasas("../data/tasas.json")

    print("✅ Conversión realizada y transacción registrada correctamente.")
