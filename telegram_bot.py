from telegram.ext import Updater, CommandHandler
import json
import os
from datetime import datetime
import telegram

# Coloca aquí tu token
TELEGRAM_TOKEN = "7666669034:AAG3fZzN2LdBha0QesiEEpFxe-pDOKmTL_I"

# Chat ID (asegúrate de poner el tuyo como variable de entorno en Render)
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Función para responder al comando /start
def start(update, context):
    update.message.reply_text("👋 ¡Hola! Soy tu bot de programación. Cada mañana te enviaré un resumen de noticias.\nPuedes preguntarme sobre ellas también.")

# Función para enviar el resumen (comando manual)
def resumen(update, context):
    mensaje = generar_mensaje_resumen()
    update.message.reply_text(mensaje)

# Nueva función reutilizable para generar el texto del resumen
def generar_mensaje_resumen():
    hoy = datetime.now().strftime('%Y-%m-%d')
    filename = os.path.join("data", f"noticias_{hoy}.json")

    if not os.path.exists(filename):
        return "Aún no tengo noticias para hoy. Ejecuta el bot recolector primero."

    with open(filename, "r", encoding="utf-8") as f:
        noticias = json.load(f)

    mensaje = f"📰 Noticias de programación ({hoy}):\n\n"
    for i, n in enumerate(noticias, start=1):
        mensaje += f"{i}. {n['title']}\n🔗 {n['link']}\n\n"

    return mensaje

# ✅ Esta es la función que se llamará desde daily_task.py
def enviar_resumen_diario():
    if not CHAT_ID:
        raise ValueError("TELEGRAM_CHAT_ID no está definido en las variables de entorno.")

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    mensaje = generar_mensaje_resumen()
    bot.send_message(chat_id=CHAT_ID, text=mensaje)

# Inicializa el bot para modo interactivo
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("resumen", resumen))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
