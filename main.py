import telebot
from config import TOKEN, currencies
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def bot_info(message):
    text = 'Чтобы конвертировать валюту, отправьте сообщение в формате:\n\n' \
           '<название валюты><в какую валюту переводим><количество переводимой валюты>\n\n' \
           'Например: лира рубль 100\n' \
           'Список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def value(message):
    text = 'Доступные валюты:'
    for currency in currencies.keys():
        text = '\n'.join([text, currency])
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Неправильный ввод. /help')

        base, quote, amount = values
        total_amount = CurrencyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду. \n{e}')
    else:
        text = f'{amount} {base} = {total_amount} {quote}'
        bot.send_message(message.chat.id, text)


bot.polling()
