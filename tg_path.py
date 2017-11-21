import telebot
import params

bot = telebot.TeleBot(params.tg_token)

def send_message(message):
    bot.send_message(-224344075, message)