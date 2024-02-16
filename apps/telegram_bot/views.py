from django.conf import settings
from telebot import TeleBot, types
from .models import TelegramUser

# Create your views here.
TELEGRAM_TOKEN = "6551317352:AAHy64GeYJJgz-UzG9E0-4q67j_TcX8dewg"
ADMIN_ID = 1651703852

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admin_id = ADMIN_ID

@bot.message_handler(commands=['start','go'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    # bot.delete_message(message.chat.id, message.message_id) 
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

class Mail:
    def __init__(self): 
        self.description = None

mail = Mail()


def get_message(message:types.Message):
    mail.description = message.text 
    users = TelegramUser.objects.all()
    for user in users:
        bot.send_message(user.id_user, mail.description)
    bot.send_message(message.chat.id, "Рассылка окончена")

@bot.message_handler(commands=['mailing'])
def send_mailing(message:types.Message):
    if message.chat.id != int(admin_id):
        bot.send_message(message.chat.id, "Эта команда доступна только админу")
        return
    msg = bot.send_message(message.chat.id, "Введите текст для рассылки: ")
    bot.register_next_step_handler(msg, get_message)

def get_text(message):
    bot.send_message(admin_id, message, parse_mode='HTML')

def get_text_doctor(message, id):
    bot.send_message(id, message)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")