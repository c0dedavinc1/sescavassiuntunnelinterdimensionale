from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

BOT_TOKEN = "INSERISCI_IL_TUO_TOKEN_TELEGRAM"

# Carica il modello open source
model_name = "microsoft/phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32)

# Funzione di risposta
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat_id

    print(f"Messaggio da {chat_id}: {user_message}")

    # Prepara il prompt
    inputs = tokenizer(f"Utente: {user_message}\nAssistente:", return_tensors="pt")

    # Genera la risposta
    outputs = model.generate(**inputs, max_new_tokens=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Pulisce la risposta (togli il testo utente iniziale)
    response = response.split("Assistente:")[-1].strip()

    await update.message.reply_text(response)

# Avvio del bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 Bot con modello open source avviato...")
app.run_polling()
