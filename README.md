# <img src="https://telegram.org/img/t_logo.png" width="28"> TelegramBot

A simple [Telegram](https://telegram.org) bot written in [Python](https://www.python.org) to convert currencies in real-time. 


<img src="https://pytba.readthedocs.io/en/latest/_static/logo2.png" width="28"> [*pyTelegramBotAPI*](https://github.com/eternnoir/pyTelegramBotAPI)

The Bot is written using the library pyTelegramBotAPI. [*Official documentation.*](https://pytba.readthedocs.io/en/latest/index.html)

<img src="https://assets.apilayer.com/apis/currency_data.png" width=28 height=28> [*Currency Data API*](https://apilayer.com/marketplace/currency_data-api) 

The Bot is running using Currency Data API which provides a simple REST API with real-time exchange rates for 168 world currencies, delivering currency pairs in universally usable JSON format. Depending on the need, Currency Data API can be replaced with any other REST API with a slight modification of the code.

**Important note:** Free plan gives you just 100 requests monthly. 

## Used libraries:
1. pytelegrambotapi
2. requests
3. json

## Bot's functions:
1. Commands **"/start"** and **"/help"** will display instructions for using the Bot.
2. Command **"/values"** will display the list of avaliable currencies.
3. You can input manually exchange request in format **"base" "quote" "amount"** and get exchange amount like below:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/57331385/211609394-71904d40-1243-4323-b51f-42ece64a930a.png">

4. You can also use command **"/convert"** . Then you just choose and tap currencies and amount via keyboard:

<img height="500" src="https://user-images.githubusercontent.com/57331385/211614467-f8eda481-25c3-4d65-9094-33d6b39a02dd.PNG"> <img height="500" src="https://user-images.githubusercontent.com/57331385/211614529-e46ea3f0-e93a-4f62-9a43-12abd6615a2d.PNG">

Finally you'll get the same result as in manual mode but with better user experience:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/57331385/211613543-5032d8c8-f16c-4dbe-a030-8412df314889.png">

