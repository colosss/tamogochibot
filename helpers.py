class start_helpers:
    prodolj_text="""Вы уже создали котёнка👉👈\n
    Хотите начать создание заново?"""

    welcome_text = """Здравствуйте! ฅ•ω•ฅ\n
    Это тамагочи-бот  (=^･ω･^=)\n
    В этой игре вам придется ухаживать за маленьким Кошко-работником!\n
    Он еще маленький, но уже трудится, чтобы заработать себе на вкусняшки 👉👈\nДа, на заводе котенку тяжело...\n
    Ухаживайте за ним - помогите котенку не забыть сходить в лоток, вовремя покушать и умыться перед работой, чтобы он не стал вонючкой! (=‐ω‐=)"""

    start_pic = '1_start_pic.png'

    help_text = """Привет! Это тамагочи-бот\n
    Вот список доступных команд:\n
    /help - вывести справку
    /start - начать игру или продолжить"""

    bn = 0

class config:
    token = '6620453925:AAGdFBKWCfxD3PeVMAmWLomP7zS6yVjhCY8'

class main_info:
    def keyboard(markup, *buttons):
        markup.add(*buttons)
        return markup
        # for button in buttons:
	    # 	markup.add(button)


class nachalo:
    nachalo_text="""И так, давай начнем!\n
    Для начала выберете имя своему милому работничку"""
    nachalo_pic='cot_vibor.png'
    

class sogl:
    sogl_text="Вы уверены в своём выборе?"
    
class id:
    m_id=0
    