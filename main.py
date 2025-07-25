from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ai_logic import du_doan_tai_xiu

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Thay bằng token bot thật

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎲 Gửi /du đoán để AI dự đoán Tài/Xỉu!")

async def du(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ket_qua = du_doan_tai_xiu()
    await update.message.reply_text(ket_qua)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("du", du))
    print("Bot is running...")
    app.run_polling()

