import tweepy, time
from keys import *

mensajes = open("contenido.txt")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print "Usuario autentificado correctamente..."

t = int(input("En que intervalo de tiempo (min)? "))
i = 1
seg = t * 60

for tweet in mensajes:
	api.update_status(tweet)
	print "Mensaje enviado "+str(i)
	i = i + 1
	time.sleep(seg)
print "Todos los mensajes han sido enviados correctamente"
