
import json
from datetime import datetime

# Convierte el valor a otra moneda
def convertir(precio_usd, moneda_destino, tasas):
    # Obtiene la tasa de cambio de dólares a moneda de destino
    tasa = tasas["USD"].get(moneda_destino)
    
    # Si la moneda de destino no existe, lanza una excepción
    if not tasa:
        raise ValueError("Moneda no soportada")
    
    return precio_usd * tasa

# Escribe una nueva línea en el archivo de registro
def registrar_transaccion(producto, precio_convertido, moneda, ruta_log):
    with open(ruta_log, "a") as archivo:
        # Obtiene la fecha y hora actual en formato YYYY-MM-DD HH:MM:SS
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Escribe una línea nueva en el archivo de registro
        archivo.write(f"{fecha} | {producto}: {precio_convertido:.2f} {moneda}\n")

# Ejemplo de uso
if __name__ == "__main__":
    tasas = cargar_tasas("../data/tasas.json")
    precio_usd = 100.00
    eur = convertir(precio_usd, "EUR", tasas)
    registrar_transaccion("Laptop", eur, "EUR", "../logs/historial.txt")