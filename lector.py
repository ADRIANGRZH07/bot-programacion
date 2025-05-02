import json
import os
from datetime import datetime

def mostrar_resumen():
    # Ruta al archivo más reciente (hoy)
    hoy = datetime.now().strftime('%Y-%m-%d')
    filename = os.path.join("data", f"noticias_{hoy}.json")

    if not os.path.exists(filename):
        print(f"No hay datos para hoy ({hoy}). Asegúrate de correr el scraper primero.")
        return

    # Leer archivo
    with open(filename, "r", encoding="utf-8") as f:
        noticias = json.load(f)

    print(f"\n📰 Resumen de noticias de programación ({hoy}):\n")

    for i, noticia in enumerate(noticias, start=1):
        print(f"{i}. {noticia['title']}")
        print(f"   🔗 {noticia['link']}\n")

if __name__ == "__main__":
    mostrar_resumen()
