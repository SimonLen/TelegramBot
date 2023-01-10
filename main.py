import telebot
from telebot import types
from config import TOKEN, currencies
from extensions import CurrencyConverter, APIException, create_markup, amount_markup

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def bot_info(message):
    text = 'Чтобы конвертировать валюту, отправьте сообщение в формате:\n\n' \
           '<название валюты><в какую валюту переводим><количество переводимой валюты>\n' \
           'Например: лира рубль 100\n\n' \
           'Или воспользуйтесь командой /convert\n' \
           'Список доступных валют /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def value(message):
    text = 'Доступные валюты:'
    for currency in currencies.keys():
        text = '\n'.join([text, currency])
    bot.reply_to(message, text)


@bot.message_handler(commands=['convert'])
def dialog_convert(message):
    text = 'Выберете валюту для конвертации.'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, base_handler)


def base_handler(message: telebot.types.Message):
    base = message.text.strip().lower()
    text = 'В какую валюту конвертируем?'
    bot.send_message(message.chat.id, text, reply_markup=create_markup(base))
    bot.register_next_step_handler(message, quote_handler, base)


def quote_handler(message: telebot.types.Message, base):
    quote = message.text.strip()
    text = 'Количество конвертируемой валюты:'
    bot.send_message(message.chat.id, text, reply_markup=amount_markup)
    bot.register_next_step_handler(message, amount_handler, base, quote)


def amount_handler(message: telebot.types.Message, base, quote):
    amount = message.text.strip()
    try:
        total_amount = CurrencyConverter.get_price(base.lower(), quote.lower(), amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Системная ошибка. \n{e}')
    else:
        text = f'{amount} {base} = {total_amount} {quote}'
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def message_convert(message: telebot.types.Message):
    try:
        values = message.text.split()

        if len(values) != 3:
            raise APIException('Неверное количество параметров. /help')

        base, quote, amount = values
        total_amount = CurrencyConverter.get_price(base.lower(), quote.lower(), amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Системная ошибка. \n{e}')
    else:
        text = f'{amount} {base} = {total_amount} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling()
