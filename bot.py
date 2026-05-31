from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_URL = "https://t.me/Israel365Tips"

# תפריט ראשי
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎁 בונוסים", callback_data="bonus")],
        [InlineKeyboardButton("💳 הפקדה", callback_data="deposit")],
        [InlineKeyboardButton("👤 סוכן", callback_data="agent")],
        [InlineKeyboardButton("📢 לערוץ", url=CHANNEL_URL)]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 ברוכים הבאים להמלצות 365 ישראל\nבחר אפשרות:",
        reply_markup=main_menu()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "bonus":
        text = "🎁 בונוסים זמינים עכשיו. להצטרפות לערוץ:"
    elif data == "deposit":
        text = "💳 מידע על הפקדות. כל העדכונים בערוץ:"
    elif data == "agent":
        text = "👤 מידע על סוכנים זמין בערוץ:"
    else:
        text = "לחץ למטה להצטרפות לערוץ:"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 מעבר לערוץ", url=CHANNEL_URL)]
    ])

    await query.edit_message_text(text, reply_markup=keyboard)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()