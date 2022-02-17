# файл bot.py
# Нужно импортировать все необходимые библиотеки, 
# файл с настройками 
# предварительно созданный api.py. 

import telebot
import config
import pytz
import api
import datetime
import json
import traceback


P_TIMEZONE = pytz.timezone(config.TIMEZONE)

TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

# Создадим бот с помощью библиотеки pyTelegramBotAPI. 
# Для этого конструктору нужно передать токен:

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(
		message.chat.id,  
        'Greetings! I can show you exchange rates.\n' + 
        '1) To get the exchange rates press /exchange.\n' + 
        '2) To get help press /help.'
        )

# обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    """Метод полуает встроенную клавиатуру (InlineKeyboardMarkup) 
    с одной кнопкой (InlineKeyboardButton) 
    текстом: “Developer messages” 
    и url='telegram.me/pyjan'"""

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Developer messages', url='telegram.me/pyjan'))
    bot.send_message(
        message.chat.id,
        '1) To receive a list of available currencies press /exchange.\n' + 
        '2) Click on the currency you are interested in.\n' + 
        '3) You will receive a message containing information regarding the source and the target currencies, ' + 
        'buying rates and selling rates.\n' + 
        '4) Click “Update” to receive the current information regarding the request. ' + 
        'The bot will also show the difference between the previous and the current exchange rates.\n' + 
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
        reply_markup=keyboard # дополнительный параметр
    )

# Обработчик команды /exchange отображает меню выбора валюты 
# и встроенную клавиатуру с 4 кнопками: USD, BTC, EUR и RUR (валюты, поддерживаемые API банка).

@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'))
    
    keyboard.row(telebot.types.InlineKeyboardButton('BTC', callback_data='get-BTC'))
    
    keyboard.row(telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'), telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR'))
    
    bot.send_message(message.chat.id, 'Click on the currency of choice:', reply_markup=keyboard)

# метод get_ex_callback:

def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])

# Метод answer_callback_query нужен, чтобы убрать состояние загрузки, 
# к которому переходит бот после нажатия кнопки. 

# Отправим сообщение send_exchange_query. 
# Ему нужно передать Message и код валюты 
# (получить ее можно из query.data. Если это, например, get-USD, передавайте USD).

# send_exchange_result:

def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    ex = api.get_exchange(ex_code)
    bot.send_message(message.chat.id, serialize_ex(ex), reply_markup=get_update_keyboard(ex), parse_mode='HTML')

# Сперва отправим состояние ввода в чат, 
# так чтобы бот показывал индикатор «набора текста», пока API банка получает запрос. 

# Теперь вызовем метод get_exchange из файла privatbank.py, 

# который получит код валюты (например, USD). 
# Также нужно вызвать два новых метода в send_message: serialize_ex, 

# get_update_keyboard возвращает клавиатуре кнопки “Update” и “Share”.

def get_update_keyboard(ex):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton(
        'Update', callback_data=json.dumps(
         {
          't': 'u',
          'e': {
              'b': ex['buy'],
              's': ex['sale'],
              'c': ex['ccy']
              }
         }
        ).replace(' ', '')
    ), 
    telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy']))
    return keyboard


# Запишем в get_update_keyboard текущий курс валют в callback_data в форме JSON. 

# JSON сжимается, потому что максимальный разрешенный размер файла равен 64 байтам.

# Кнопка t значит тип, а e — обмен. 
# Остальное выполнено по тому же принципу.

# У кнопки Share есть параметр switch_inline_query. 
# После нажатия кнопки пользователю будет предложено выбрать один из чатов, 
# открыть этот чат и ввести имя бота и определенный запрос в поле ввода.

# сериализатор валюты
# Методы serialize_ex и дополнительный serialize_exchange_diff нужны, 
# чтобы показывать разницу между текущим и старыми курсами валют после нажатия кнопки Update.

def serialize_ex(ex_json, diff=None):
    result = '<b>' + ex_json['base_ccy'] + ' -> ' + ex_json['ccy'] + ':</b>\n\n' + 'Buy: ' + ex_json['buy']
    if diff:
        result += ' ' + serialize_exchange_diff(diff['buy_diff']) + '\n' + 'Sell: ' + ex_json['sale'] + ' ' + serialize_exchange_diff(diff['sale_diff']) + '\n'
    else:
        result += '\nSell: ' + ex_json['sale'] + '\n'
    return result
    
def serialize_exchange_diff(diff):
    result = ''
    if diff > 0:
        result = '(' + str(diff) + ')'
    elif diff < 0:
        result = '(' + str(diff)[1:] + ')'
    return result

# метод serialize_ex получает необязательный параметр diff. 
# Ему будет передаваться разница между курсами обмена 
# в формате {'buy_diff': <float>, 'sale_diff': <float>}. 
# Это будет происходить во время сериализации после нажатия кнопки Update. 
# Когда курсы валют отображаются первый раз, он нам не нужен.

# обработчик для кнопок встроенной клавиатуры
# декоратор @bot.callback_query_handler, 
# передает объект CallbackQuery во вложенную функцию.

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)

if __name__ == '__main__':
    bot.infinity_polling()