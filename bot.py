from telebot import TeleBot

TOKEN = "8477635053:AAF0vwt0wbR22NRXj3tnPyX8Z1odzQmJ5u8"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = """
👋 Assalomu alaykum!

🎉 Turo Tools rasmiy botiga xush kelibsiz!

Quyidagi buyruqlardan birini tanlang:

📦 /order - Buyurtma berish
👨‍💼 /agent - Agentni chaqirish
💳 /debt - Qarzdorlikni tekshirish
ℹ️ /help - Yordam

🚚 Turo Tools - ishonchli hamkoringiz!
"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['order'])
def order(message):
    bot.send_message(message.chat.id,
"""📦 Buyurtma berish

🏢 Korxona nomi:
📍 Manzil:
📞 Telefon:
🛠 Kerakli mahsulot:
📦 Miqdori:

Ma'lumotlarni to'ldirib yuboring.""")

@bot.message_handler(commands=['agent'])
def agent(message):
    bot.send_message(message.chat.id,
"""👨‍💼 Agent chaqirish

🏢 Korxona nomi:
📍 Manzil:
📞 Telefon:

Agentimiz siz bilan tez orada bog'lanadi.""")

@bot.message_handler(commands=['debt'])
def debt(message):
    bot.send_message(message.chat.id,
"""💳 Qarzdorlikni tekshirish

🏢 Korxona nomi:
📞 Telefon:

Ma'lumotlarni yuboring, qarzdorlikni tekshirib javob beramiz.""")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
"""📋 Buyruqlar:

/start - Botni ishga tushirish
/order - Buyurtma berish
/agent - Agentni chaqirish
/debt - Qarzdorlikni tekshirish""")

print("Bot ishga tushdi...")

bot.infinity_polling()