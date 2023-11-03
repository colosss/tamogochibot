import telebot
import helpers
from telebot import types


bot = telebot.TeleBot(helpers.config.token) 

welcome = helpers.start_helpers

na=helpers.nachalo

info = helpers.main_info

# Переменные для создания условий или для сокращения


@bot.message_handler(commands=['start'])
def send_welcome(message): #стартовые сообщения
	if helpers.start_helpers.bn ==0:#если только начали
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,selective=True)
		info.keyboard(markup, 'Начнем!', 'Помощь', 'Какой-то текст')
		bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=welcome.welcome_text, reply_markup=markup)
	# bot.register_next_step_handler
	elif helpers.start_helpers.bn!=0:#Если уже создавали
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,selective=True)
		info.keyboard(markup, 'Продолжим!', 'Помощь', 'Какой-то текст')
		bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=f'{welcome.welcome_text}\n{welcome.prodolj_text}', reply_markup=markup)
@bot.message_handler(func=lambda m:True)
def send_help(message):#помощь
	if message.text=='/help' or message.text=='Помощь':
		bot.send_message(message.chat.id, welcome.help_text)
def send_reg(message):
	if message.text=='Начнем!':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,selective=True)
		helpers.start_helpers.bn=True
		info.keyboard(markup,'Назад','Помощь')
		#adasd
		bot.send_photo(message.chat.id, photo=open(na.nachalo_pic, 'rb'), caption=na.nachalo_text, reply_markup=markup)
@bot.message_handler(func=lambda m:True)
def send_message(message):
	if message.text==message:
		bot.send_message(message.chat.id,'sadasd')
bot.infinity_polling()