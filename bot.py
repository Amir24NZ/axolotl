from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

# توکن API ربات خود را اینجا وارد کنید
BOT_TOKEN = "7738350348:AAEaeDTmobYLRfPwxu-myA8qOFxvVsF633c"

# دستورات /start
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    # ایجاد دکمه برای پیوستن به کانال
    keyboard = [
        [InlineKeyboardButton("Join Axolotl Airdrop Channel", url="https://t.me/axolotl_airdrop")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ارسال پیام خوش آمدگویی
    await update.message.reply_text(
        f"Hello {user.first_name}! Welcome to the Axolotl Airdrop Bot.\n\n"
        "You're now part of the Axolotl Airdrop campaign! Please join our channel to stay updated "
        "and participate in exciting giveaways.\n\n"
        "click start to join Airdrop!.\n\n"
        "Good luck!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    # ساخت برنامه
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # افزودن فرمان /start
    app.add_handler(CommandHandler("start", start))

    # اجرای ربات
    print("Bot is running...")
    app.run_polling()
