from playwright.sync_api import sync_playwright
import json
import os
from datetime import datetime

def scrap_devto(filename):
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

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Guardar datos en archivo JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Guardadas {len(data)} noticias en: {filename}")
