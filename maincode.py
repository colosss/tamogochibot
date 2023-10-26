import telebot
import helpers
from telebot import types

bot = telebot.TeleBot(helpers.config.token) 

welcome = helpers.start_helpers

info = helpers.main_info

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	info.keyboard(markup, 'Начнем!', 'Помощь', 'Какой-то текст')
	bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=welcome.welcome_text, reply_markup=markup)
	# bot.register_next_step_handler
@bot.message_handler(func=lambda m:True)
def send_help(message):
	if message=='/help':
		bot.send_message(message.chat.id, welcome.help_text)

bot.infinity_polling()