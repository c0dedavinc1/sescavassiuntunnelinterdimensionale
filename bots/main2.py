import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = '8498664237:AAH9bIO2aUuZqj4RGiRCmI1PbIftHrGwpME'

# Mappa parole chiave -> file immagine
# ovviamente vanno criptate
KEYWORDS = {
    "stella non guardare di lato": "photo/star.png",
}

# 🔹 Funzione che genera solo testo di risposta
def genera_risposta(messaggio: str) -> str:
    messaggio = messaggio.lower().strip()

    if any(parola in messaggio for parola in ["ciao"]):
        return "Ciao protagonista, tanto tempo che non ci sentiamo..."

    elif "come stai" in messaggio:
        return "Sei sicuro di volermelo chiedere?"

    else:
        return "..."

# 🔹 Handler che riceve i messaggi
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    testo_utente = update.message.text.lower()

    # Controlla se contiene parole chiave e invia immagine
    for parola, immagine in KEYWORDS.items():
        if parola in testo_utente:
                await update.message.reply_photo(photo=open(immagine, "rb"))
           
    # Se non è una parola chiave, risponde normalmente
    risposta = genera_risposta(testo_utente)
    await asyncio.sleep(2.6)
    await update.message.reply_text(risposta)

# 🔹 Avvio del bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 Bot avviato!")
app.run_polling()
