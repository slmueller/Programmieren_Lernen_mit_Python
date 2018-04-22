#Quelle: http://www.dancingbison.com, https://code.activestate.com/recipes/579117-simple-command-line-alarm-clock-in-python/
from time import sleep

print("Das ist ein Wecker. Stopp das Programm mit Ctrl + C.")
userEingabe = input("Wieviele Minuten möchtest Du schlafen? E.g. 10 \n>")

minuten = int(userEingabe)

#Unit: Plural or singular?
if minuten == 1:
    einheit = " Minute"
else:
    einheit = " Minuten"

#Convert to seconds
sekunden = minuten * 60

if minuten > 0:
    print("Schlaf noch " + str(minuten) + einheit)
    sleep(sekunden)  #Das System wartet x Sekunden.

#Läute den Wecker wenn die Zeit durch ist:
print("Wach auf!!!")
for i in range(5):  #Der Wecker läutet fünfmal da die Schlaufe fünfmal ausgeführt wird
    print(chr(7))   #ruft den Alarmsound auf
    sleep(1)
