from datetime import datetime
from scrapers.devto_scraper import scrap_devto
from telegram_bot import enviar_resumen_diario

def run_scraper():
    print("Recolectando noticias...")
    scrap_devto()  # ✅ Ya no pasamos 'filename'
    print("Noticias recolectadas.")

def main():
    run_scraper()
    enviar_resumen_diario()

if __name__ == "__main__":
    main()