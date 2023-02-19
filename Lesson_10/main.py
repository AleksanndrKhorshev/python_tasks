
import logging
import telebot

TOKEN = '5612327958:AAFv4pygI1hs1D43OGmiAbHslIhk43m8niA'

logging.basicConfig(level=logging.INFO,
                    filename="logs.log",
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(message):
    if message.find('+') != -1:
        a, b = map(int, message.split('+'))
        result = add(a, b)
    elif message.find('-') != -1:
        a, b = map(int, message.split('-'))
        result = subtract(a, b)
    elif message.find('*') != -1:
        a, b = map(int, message.split('*'))
        result = multiply(a, b)
    elif message.find('/') != -1:
        a, b = map(int, message.split('/'))
        result = divide(a, b)
    else:
        result = 'Incorrect input'

    return result

@bot.message_handler(commands=['start'])
def start_message(message):
    logger.info("Started")
    bot.send_message(message.chat.id, 'Hello! I am a calculator bot. Use /help to get a list of commands.')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я могу выполнить следующие операции в формате:\n1.Сложение: a+b\n2.Вычитание: a-b\n3.Умножение: a*b\n4.Деление: a/b')

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        result = calculate(message.text)
        bot.send_message(message.chat.id, result)
        logger.info("Result: %s" % result)
    except Exception as e:
        bot.send_message(message.chat.id, 'Некорректный ввод')
        logger.error("Ошибка: %s" % e)

bot.polling()
