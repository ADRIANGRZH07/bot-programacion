from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import os
from datetime import datetime

# Coloca aquí tu token
TELEGRAM_TOKEN = "7666669034:AAG3fZzN2LdBha0QesiEEpFxe-pDOKmTL_I"

# Función para responder al comando /start
def start(update, context):
    update.message.reply_text("👋 ¡Hola! Soy tu bot de programación. Cada mañana te enviaré un resumen de noticias.\nPuedes preguntarme sobre ellas también.")

# Función para enviar el resumen
def resumen(update, context):
    hoy = datetime.now().strftime('%Y-%m-%d')
    filename = os.path.join("data", f"noticias_{hoy}.json")

    if not os.path.exists(filename):
        update.message.reply_text("Aún no tengo noticias para hoy. Ejecuta el bot recolector primero.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        noticias = json.load(f)

    mensaje = f"📰 Noticias de programación ({hoy}):\n\n"
    for i, n in enumerate(noticias, start=1):
        mensaje += f"{i}. {n['title']}\n🔗 {n['link']}\n\n"

    update.message.reply_text(mensaje)

# Inicializa el bot
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("resumen", resumen))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
