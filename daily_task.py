from datetime import datetime
from scrapers.devto_scraper import scrap_devto
from telegram_bot import enviar_resumen_diario

def run_scraper():
    print("Recolectando noticias...")
    hoy = datetime.today().strftime('%Y-%m-%d')
    archivo_salida = f"data/noticias_{hoy}.json"
    scrap_devto()
    print(f"Noticias guardadas en: {archivo_salida}")

def main():
    run_scraper()
    enviar_resumen_diario()

if __name__ == "__main__":
    main()
