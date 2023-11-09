import telebot
import random
from helpers import *
from telebot import types
# -*- coding: utf-8 -*-

bot = telebot.TeleBot(config.token) 
welcome = start_helpers

random_pet_names = ['Пирожок', 'Пряник', 'Киска', 'Крыска', 'Булочка', 'Ириска']

class pet_info:
	def pet_name_to_file(message):
		with open('base.txt', 'a') as f:
			f.write(str(message.from_user.id)+':'+gameplay.pet_name+'\n')
		return
	def pet_name_check(message):
		with open('base.txt') as f:
			for line in f:
				if str(message.from_user.id) in line.strip('\n').split(':'):
					gameplay.pet_name = line.strip().split(':')[1]
					return gameplay.pet_name
				else:
					return False
	
	

def send_help(message): #помощь
	if message.text=='/help' or message.text=='Помощь':
		bot.send_message(message.chat.id, welcome.help_text)
		return

def no_understand(message):
	bot.send_message(message.chat.id, 'Я не понимаю 👉👈')
	bot.send_message(message.chat.id, welcome.help_text)

def exit(message):
	bot.send_message(message.chat.id, 'До новой встречи!')
	return

def keyboard(markup, *buttons):
    markup.add(*buttons)
    return markup

def send_reg(message):
	if message.text=='Начнем!':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		keyboard(markup,'Рандомное имя', 'Выход')
		bot.send_photo(message.chat.id, photo=open(gameplay.nachalo_pic, 'rb'), caption=gameplay.nachalo_text, reply_markup=markup)
		bot.register_next_step_handler(message, register_check)
	elif message.text=='Помощь':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		keyboard(markup, 'Старт')
		bot.send_message(message.chat.id, welcome.help_text, reply_markup=markup)
		bot.register_next_step_handler(message, send_welcome)
	elif message.text=='Выход':
		exit(message)
	else:
		no_understand(message)


def  register_check(message):
	if message.text=='Выход':
		welcome.bn = 0
		exit(message)
	elif message.text=='Рандомное имя':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		keyboard(markup, 'Другое имя', 'Сохранить')
		gameplay.pet_name = random.choice(random_pet_names)
		bot.send_message(message.chat.id, 'Имя твоего котенка - ' + gameplay.pet_name + '! 👉👈 Сохранить это имя?',  reply_markup=markup)
		bot.register_next_step_handler(message, pet_name_check)
	else:
		gameplay.pet_name = message.text
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		keyboard(markup, 'Другое имя', 'Сохранить')
		bot.send_message(message.chat.id, 'Имя твоего котенка - ' + gameplay.pet_name + '! 👉👈 Сохранить это имя?',  reply_markup=markup)
		bot.register_next_step_handler(message, pet_name_check)


def pet_name_check(message):
	if message.text=='Другое имя':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		keyboard(markup,'Рандомное имя', 'Выход')
		bot.send_message(message.chat.id, 'Введи новое имя или нажми кнопку Рандомное имя',  reply_markup=markup)
		bot.register_next_step_handler(message, register_check)
	elif message.text=='Сохранить':
		pet_info.pet_name_to_file(message)
		pet_name_register(message)
	else:
		no_understand(message)

def pet_name_register(message):
	remove_keayboard = types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, 'Имя котенка сохранено!', reply_markup=remove_keayboard)
	welcome.bn = 1
	return


def play_check(message):
	if message.text=='Продолжим!':
		play_go_on(message)
	elif message.text=='Начнем заново!':
		welcome.bn = 0
		send_welcome(message)
	elif message.text=='Помощь':
		send_help(message)
	elif message.text=='Выход':
		exit(message)
	else:
		no_understand(message)

def play_go_on(message):
	remove_keayboard = types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, f'Отлично! Твой котенок {gameplay.pet_name} уже соскучился (=^･ω･^=)', reply_markup=remove_keayboard)
	return


# Переменные для создания условий или для сокращения

@bot.message_handler(commands=['start'])
def send_welcome(message): #стартовые сообщения
	if welcome.bn == 0:#если только начали
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		keyboard(markup, 'Начнем!', 'Помощь', 'Выход')
		bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=welcome.welcome_text, reply_markup=markup)
		bot.register_next_step_handler(message, send_reg)
	elif welcome.bn!=0: #Если уже создавали
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		keyboard(markup, 'Продолжим!', 'Начнем заново!', 'Помощь', 'Выход')
		bot.send_photo(message.chat.id, photo=open(welcome.start_pic, 'rb'), caption=f'{welcome.welcome_text}\n{gameplay.prodolj_text}', reply_markup=markup)
		bot.register_next_step_handler(message, play_check)

bot.infinity_polling()