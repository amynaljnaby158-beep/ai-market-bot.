from telegram import Bot
bot = Bot("8893640950:AAH9sFZJuO4KJLiswD2jRGHBl2p_FqMDigo")
import os
from telegram.ext import Application, CommandHandler
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
async def start(update, context):
      await update.message.reply_text("هلا بيك، البوت شغال 🤖")
  app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
