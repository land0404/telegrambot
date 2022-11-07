import telebot
channel_id = "@namefrom"
# Создаем экземпляр бота
bot = telebot.TeleBot('5774968702:AAFZyG8B6zBN2PWP50JSORgkzzh6-rCS69w')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    name = message.from_user.first_name
    print(name)
    bot.reply_to(message, "Welcome, Напиши мне что-нибудь")
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    name2 = message.from_user.username
    s2 = '   '
    bot.send_message(channel_id, 'Автор  @' + str(name2) + str(s2) + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)



