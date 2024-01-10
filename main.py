import telebot
import requests
import json
import urllib

headers_auth = {'X-API-KEY':'6276e25c-d5ec-4a8a-8606-ba4681a243bd'}
bot = telebot.TeleBot('5613342873:AAEUhMZHWL6mB7bgWYG6PB_j1issBBV78yU')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет вацок, можешь узнать за любой фильм')
@bot.message_handler(content_types='text')
def message(message):
    film = message.text
    r = requests.get('https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword='+film,headers=headers_auth).json()

    send_user = r['films'][0]
    nameRu = send_user['nameRu']
    try:
        nameEn = send_user['nameEn']
    except:
        nameEn = '-'
    type_film = send_user['type']
    year = send_user['year']
    description = send_user['description']
    film_time = send_user['filmLength']
    countries = send_user['countries']
    #country = countries[0]['country']
    x = len(countries)
    print(nameRu+'\n',nameEn+'\n',type_film+'\n',year+'\n',description+'\n')
    n = 0
    for n in range(x):
        country = countries[n]['country']
        print(country)
    rating = send_user['rating']
    post = send_user['posterUrlPreview']
    name = '2.png'
    p = requests.get(post)
    out = open(name, "wb")
    out.write(p.content)
    out.close()
    photo = open('2.png','rb')
    bot.send_photo(message.chat.id,photo,caption='Название: '+nameRu+' ('+nameEn+') '+year+' год'+'\n'+
                   'Продолжительность: ' + film_time + '\n'+
                   'Страна: '+country+'\n'+
                   'Описание: '+description)


bot.polling(none_stop=True)

