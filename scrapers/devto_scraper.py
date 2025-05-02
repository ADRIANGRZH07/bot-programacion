from playwright.sync_api import sync_playwright
import json
import os
from datetime import datetime

def scrap_devto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://dev.to")
        page.wait_for_timeout(5000)

        titles = page.locator(".crayons-story__title")
        count = titles.count()
        data = []

        for i in range(min(10, count)):
            title = titles.nth(i).inner_text().strip()
            link = titles.nth(i).locator("a").get_attribute("href")
            data.append({
                "title": title,
                "link": f"https://dev.to{link}",
                "source": "Dev.to",
                "date": datetime.now().isoformat()
            })

        browser.close()

    # === Guardar en carpeta 'data' sin errores de ruta ===

    # Ruta absoluta al directorio base del proyecto
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    # Crear carpeta si no existe
    os.makedirs(DATA_DIR, exist_ok=True)

    # Ruta final del archivo JSON
    filename = os.path.join(DATA_DIR, f"noticias_{datetime.now().strftime('%Y-%m-%d')}.json")

    # Guardar datos en archivo JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Guardadas {len(data)} noticias en: {filename}")

# Si deseas probar directamente este archivo, puedes descomentar esto:
# if __name__ == "__main__":
#     scrap_devto()
