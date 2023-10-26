import telebot
import helpers
from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

bot = telebot.TeleBot(helpers.config.token) 

welcome = helpers.start_helpers

na=helpers.nachalo

info = helpers.main_info

# Переменные для создания условий->

bn=False 

@bot.message_handler(commands=['start'])
def send_welcome(message):
	if bn !=True:
		info.keyboard(markup, 'Начнем!', 'Помощь', 'Какой-то текст')
		bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=welcome.welcome_text, reply_markup=markup)
	# bot.register_next_step_handler
	else:
		info.keyboard(markup, 'Продолжим!', 'Помощь', 'Какой-то текст')
		bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=f'{welcome.welcome_text}\n{welcome.prodolj_text}', reply_markup=markup)
@bot.message_handler(func=lambda m:True)
def send_help(message):
	if message.text=='/help' or message.text=='Помощь':
		bot.send_message(message.chat.id, welcome.help_text)
	if message.text=='Начнем!':
		bn=True
		info.keyboard(markup, 'Назад')
		bot.send_photo(message.chat.id, photo=open(na.nachalo_pic, 'rb'), caption=na.nachalo_text, reply_markup=markup)
bot.infinity_polling()