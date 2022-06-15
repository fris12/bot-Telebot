import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
from telebot import types

today = date.today()

rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)
#Создаем клавиатуру
menu = types.ReplyKeyboardMarkup( resize_keyboard=True)
#Создаем кнопку
btnUSD = types.KeyboardButton(text="🇺🇸 Доллар США")
btnEUR = types.KeyboardButton(text="🇪🇺 Евро")
btnCNY = types.KeyboardButton(text="cny Юань")
#добавляем кнопку на клавиатуру
menu.add(btnUSD,btnEUR)
menu.add(btnCNY)

@bot.message_handler(commands=["start"])
def start(message):
	#reply_markup=menu - прикрепляем клавиатуру к сообщению
	bot.send_message(message.chat.id, "Выбери валюту:", reply_markup=menu)
#делаем реакцию на кнопку
@bot.message_handler(func = lambda message: message.text=='🇺🇸 Доллар США')
def usd(message):
	text = "1 Доллар США ="+str(rates['USD'].rate)+"руб."
	bot.send_message(message.chat.id, text)
@bot.message_handler(func = lambda message: message.text=='eu  Евро')
def eur(message):
	text = "1 Евро ="+str(rates['EUR'].rate)+"руб."
	bot.send_message(message.chat.id, text)	
@bot.message_handler(func = lambda message: message.text=='eu  Евро')
def cny(message):
	text = "1 Юань ="+str(rates['CNY'].rate)+"руб."
	bot.send_message(message.chat.id, text)	
if __name__ == '__main__':
	bot.infinity_polling()
