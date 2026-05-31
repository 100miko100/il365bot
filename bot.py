from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_URL = "https://t.me/Israel365Tips"

keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🚀 הצטרף לערוץ", url=CHANNEL_URL)]
])

KEYWORDS = ["365", "סוכן", "בטים", "הפקדה", "בונוס"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 ברוכים הבאים להמלצות 365 ישראל\n\nלחץ על הכפתור כדי להצטרף לערוץ:",
        reply_markup=keyboard
    )

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").lower()

    if any(word in text for word in KEYWORDS):
        await update.message.reply_text(
            "📢 מצאנו מידע רלוונטי.\nהצטרף לערוץ לקבלת עדכונים:",
            reply_markup=keyboard
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, messages))

app.run_polling()