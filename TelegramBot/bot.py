from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, MessageHandler, filters
import logging




async def main(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text(f"""Hello {update.effective_user.first_name}
    I have only /start command """)
    
  
async def chat(update: Update, context: CallbackContext):
    text="Hello guy"
    await update.message.reply_text(text)

async def get_voice(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    new_file=await context.bot.get_file(update.message.voice.file_id)
    await new_file.download_to_drive(f"voice_note.ogg")

app=ApplicationBuilder().token('6603128229:AAGy0qwJOOpMYSG2EBL7sgkFR5XKU6QEWX0').build()
app.add_handler(CommandHandler("start", main))
app.add_handler(MessageHandler(filters.TEXT, chat, ContextTypes.DEFAULT_TYPE))
app.add_handler(MessageHandler(filters.VOICE, get_voice, ContextTypes.DEFAULT_TYPE))

app.run_polling()