from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging




async def main(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text(f"""Hello {update.effective_user.first_name}
    I have only /start command """)
  


app=ApplicationBuilder().token('6603128229:AAGy0qwJOOpMYSG2EBL7sgkFR5XKU6QEWX0').build()
app.add_handler(CommandHandler("start", main))
#ogging.basicConfig(filename='bot.log', filemode='w', format='%(name)s=%(levelname)s-%(message)s')
#logging.info('Bot started')
app.run_polling()