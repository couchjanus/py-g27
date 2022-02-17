
# Use this token to access the HTTP API:
# 5236531719:AAF9OqLiXxijj1qbtk5uhIBhXknrPQC81CY
# Keep your token secure and store it safely, it can be used by anyone to control your bot.

# For a description of the Bot API, see this page: 
import telebot
import requests

# bot = telebot.TeleBot('2118247526:AAH-crDn7TaL8HbKYM-lr4oaIsCpcIckbiI')
# # res = requests.get("https://api.telegram.org/bot5236531719:AAF9OqLiXxijj1qbtk5uhIBhXknrPQC81CY/getMe")

# # print(res.json())

# @bot.message_handler(context_types=['text'])
# def get_text_messahes(message):
#     if message.text == 'Hello':
#         bot.send_message(message.from_user.id, "Hi, Can I help You?")
#     elif message.text == '/help':
#         bot.send_message(message.from_user.id, 'Text Hello please')
#     else:
#         bot.send_message(message.from_user.id, "I don't understand You. Text please /help")


        
bot.polling(non_stop=True, interval=0)
        
