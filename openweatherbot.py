import telebot
import urllib.request
import json
import threading
import openweather

bot = telebot.TeleBot("420472180:AAFYSnMUEVjWXgA_1xC7KXFhAZGoHJC-WVg")

user = bot.get_me()

@bot.message_handler(func=lambda m: True)
def send_weather(message):
    try:
        zip_input = message.text.replace("/", "")
        owo = openweather.OpenWeather(zip_input, 'us', 'imperial', '60b91248e90de082739c85e97bd85da9')
        owo.get_data()
        my_message = ("The current temperature in {} is {}".format(owo.loc_name, owo.cur_temp))
        bot.reply_to(message, my_message)
    except Exception as e:
        bot.reply_to(message, e)

bot.polling()
