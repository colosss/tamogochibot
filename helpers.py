from telebot import types
import telebot

class start_helpers:
    
    welcome_text = """
    Здравствуйте! ฅ•ω•ฅ\n
    Это тамагочи-бот (=^･ω･^=)\n
    В этой игре вам придется ухаживать за маленьким Кошко-работником!\n
    Он еще маленький, но уже трудится, чтобы заработать себе на вкусняшки 👉👈\nДа, на заводе котенку тяжело...\n
    Ухаживайте за ним - помогите котенку не забыть сходить в лоток, вовремя покушать и умыться перед работой, чтобы он не стал вонючкой! (=‐ω‐=)
    """

    help_text = """
    Привет! Это тамагочи-бот\n
    Вот список доступных команд:\n
    /help - вывести справку
    /start - начать игру или продолжить
    """

    start_pic = r'images/1_start_pic.png'

    bn = 0

class config:
    token = '6620453925:AAGdFBKWCfxD3PeVMAmWLomP7zS6yVjhCY8'
    m_id=0
    # def keyboard(markup, *buttons):
    #     markup.add(*buttons)
    #     return markup

class gameplay:
    nachalo_text="""И так, давай начнем!\n
    Для начала выбери имя своему милому работничку\n
    Введи новое имя или нажми кнопку Рандомное имя """
    nachalo_pic=r'images/cot_vibor.png'
    sogl_text="Вы уверены в своём выборе?"
    prodolj_text="""Вы уже создали котёнка👉👈\n
    Хотите начать создание заново?"""
    pet_name = ''


