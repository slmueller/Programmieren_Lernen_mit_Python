#=========================================
#Quelle: usingpython.com/programs
#=========================================

import time #importiere die Bilbiothek time

print("Ist es draussen dunkel?\n==================")

#Monat_Nummer : Sonnenuntergang_Stunde
dunkel = {
    1: 16,
    2: 17,
    3: 18,
    4: 19,
    5: 19,
    6: 20,
    7: 20,
    8: 19,
    9: 18,
    10: 17,
    11: 16,
    12: 16
}

#Monat_Nummer : Sonnenaufgang_Stunde
hell = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 4,
    7: 4,
    8: 5,
    9: 6,
    10: 6,
    11: 7,
    12: 8
}

#Variable enthält die jetztige Zeit
zeit_jetzt = time.localtime()

#Brauche die "dunkel" und "hell" Dictionnaires.
#Es ist dunkel wenn die Stunde später oder gleich ist wie die Sonnenunterganszeit
#oder früher als Sonnenaufgangszeit.
if zeit_jetzt.tm_hour >=dunkel[zeit_jetzt.tm_mon] or zeit_jetzt.tm_hour < hell[zeit_jetzt.tm_mon]:
    print("Ja, es ist dunkel.")
else:
    print("Nein, es ist hell.")
