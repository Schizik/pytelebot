import telebot
import imdb
from flask import Flask


token = '375244280:AAGkTnPEmuVOapKzXguixWZmnVmOP41X_AY'
bot = telebot.TeleBot(token)
app = Flask(__name__)
ia = imdb.IMDb() # by default access the web

def searchartist(msg):
    S = "Nothing found"
    S1 = ""
    s_result = ia.search_person(msg.text)
    if " " in msg.text:
        the_unt = s_result[0]
        ia.update(the_unt)
        try:
            if len(the_unt.data['actor'])<5:
                bot.send_message(msg.chat.id, the_unt['bio'])
            else:
                S = "Filmlist to long. View last 10 films:\n"
                for i in range(0,10):
                    S = S + str(the_unt.data['actor'][i]) + "\n"
            S1 = str(the_unt['name']) + " http://www.imdb.com/name/nm"+str(the_unt.personID) + "\n"
        except LookupError:
#        except:
            if len(the_unt.data['actress'])<5:
                bot.send_message(msg.chat.id, the_unt['bio'])
            else:
                S = "Filmlist to long. View last 10 films:\n"
                for i in range(0,10):
                    S = S +str(the_unt.data['actress'][i]) + "\n"
            S1 = str(the_unt['name']) + " http://www.imdb.com/name/nm"+str(the_unt.personID) + "\n"
    else:
        S = "Try to input full name"
        for item in s_result:
            S = S + item['name'].encode('utf-8') + " http://www.imdb.com/name/nm"+str(item.personID) + "\n"
    if len(S1) != 0:
        bot.send_message(msg.chat.id, S1)
        bot.send_message(msg.chat.id, S)

def searchfilm(msg):
    s_result = ia.search_movie(msg.text)
    S = "Nothing found"
    for item in s_result:
        S = S + item['long imdb canonical title'].encode('utf-8') + " http://www.imdb.com/title/tt" + str(item.movieID) + "\n"
    bot.send_message(msg.chat.id, S)

def charactersearch(msg):
    s_result = ia.search_character(msg.text)
    S = "Nothing found"
    for item in s_result:
        S = S + item['long imdb canonical title'].encode('utf-8') + " http://www.imdb.com/title/tt" + str(item.movieID) + "\n"
    bot.send_message(msg.chat.id, S)