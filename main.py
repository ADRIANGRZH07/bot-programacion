# main.py

from scrapers.devto_scraper import scrap_devto

def main():
    print("Ejecutando bot de programación...")
    scrap_devto()
    print("Recolección completada.")

if __name__ == "__main__":
    main()
