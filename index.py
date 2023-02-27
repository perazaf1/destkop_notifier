
import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC

#Pas de data à l'origine 
covidData = None

try :
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except :
    #au cas où pas de connexion internet
    print("Vérifiez la connexion Internet")

#si les données sont trouvées 
if (covidData != None):
    #convertir au format JSON
    data = covidData.json()["Success"]

    #répéter la boucle plusieurs fois
    while (True):
        notification.notfiy(
            #Titre de la notification,
            title = "Statistiques Covid-19 sur {}".format(datetime.date.today()),
            #Corps de la notification
            message = "Nombre de cas : {totalcases} \nCas d'aujourd'hui : {todaycases} \nMorts aujourd'hui :{todaydeaths}\n Cas actifs :{active}".format(
                totalcases = data['cases'],
                todaycases = data['todayCases'],
                todaydeaths = data['todayDeaths'],
                active = data ['active']),
            #Icone de la notification
            app_icon = "Shield Check.ico",
            #temps que la notif reste
            timeout = 50
                    
        )
        #4 heures = 60*4
        #répétition de la notif toutes les 4 heures
        time.sleep(60*4)