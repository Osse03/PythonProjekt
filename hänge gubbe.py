import random
import os

# Pseudokod:
# Starta
#   En lista med ord och deras betydelser som spelaren ska gissa på.
#   
#   Funktion slumpa_ord(ordlista)
#   Returnera ett slumpmässigt ord från ordlistan med deras betydelse.
#   
#   Funktion visa_ord_med_understrykning(ordet, gissade_bokstaver)
#   Skapa en sträng med ordet, där ej gissade bokstäver ersätts med understreck
#   Returnera den modifierade strängen och vissa på skärmen
#   
#   Funktion för hänga_gubbe()
#   Välj ett slumpmässigt ord och dess betydelse från ordlistan
#   Omvandla ordet till små bokstäver
#   
#   Skriv ut välkomstmeddelande 
#   
#   Skapa en tom lista för gissade bokstäver
#   Sätt antal gissningar till 5
#   
#    Medan antal gissningar är större än 0
#    Visa ordet med understreck och gissade bokstäver
#   
#    Deklarererar en variabel som får ett värde beroende på användarens input
#   
#    Om gissningen inte är en enskild bokstav eller inte är en bokstav alls
#    Skriv ut felmeddelande och fortsätt till nästa iteration av loopen
#   
#    Om gissningen redan har gjorts
#    Skriv ut meddelande om att bokstaven redan har gissats
#   
#    Om gissningen finns i ordet
#    Lägg till gissningen i listan med gissade bokstäver
#    Om alla bokstäver i ordet har gissats
#    Skriv ut vinstmeddelande och avsluta loopen
#    Annars
#    Lägg till gissningen i listan med gissade bokstäver
#    Minska antal gissningar med 1
#   
#    Skriv ut förlustmeddelande och visa det korrekta ordet
#   
#   Fråga spelaren om de vill spela igen
#   Om svaret är ja, gå tillbaka till början av programmet
#   Annars avsluta programmet
# Slut

# Lista med ord och deras betydelser som spelaren ska gissa
ordlista = [
    ("Vispgrädde", "Uppvispad grädde"),
    ("Ukulele", "Ett fyrsträngat instrument med ursprung i Portugal"),
    ("Innebandyspelare", "En person som spelar sporten innebandy"),
    ("Flaggstång", "En mast man hissar upp en flagga på"),
    ("Yxa", "Verktyg för att hugga ved"),
    ("Havsfiske", "Fiske till havs"),
    ("Prisma", "Ett transparent optiskt element som bryter ljuset vid plana ytor"),
    ("Landsbygd", "Geografiskt område med lantlig bebyggelse"),
    ("Generositet", "En personlig egenskap där man vill dela med sig av det man har"),
    ("Lyckosam", "Att man ofta, eller för stunden har tur"),
    ("Perrong", "Den upphöjda yta som passagerare väntar på eller stiger på/av ett spårfordon"),
    ("Samarbeta", "Att arbeta tillsamans mot ett gemensamt mål"),
    ("Välartad", "Att någon är väluppfostrad, skötsam, eller lovande")
]

# Funktion för att slumpa ett ord från listan
def slumpa_ord(ordlista):
    return random.choice(ordlista)

# Funktion för att visa ordet med understreck eller den gissade bokstaven
def visa_ord_med_understrykning(ordet, gissade_bokstaver):
    return "".join([bokstav if bokstav in gissade_bokstaver else "-" for bokstav in ordet])

# Huvudfunktionen för spelet "Hänga Gubbe"
def hänga_gubbe():
    ord, betydelsen = slumpa_ord(ordlista)
    ordet = ord.lower()
    gissade_bokstaver = []
    antal_gissningar = 5

    print("Välkommen till Hänga Gubbe!")

    while antal_gissningar > 0: # Loop som körs så länge spelaren har fler gissningar
        ord_med_understrykning = visa_ord_med_understrykning(ordet, gissade_bokstaver)
        print(f"Gissa ordet: {ord_med_understrykning}")
        print(f"Använda bokstäver: {' '.join(gissade_bokstaver)}")
        print(f"{antal_gissningar} gissningar kvar")

        gissning = input("Gissa en bokstav: ").lower()

        if len(gissning) != 1 or not gissning.isalpha(): # Kontrollerar att man gissar på en alfabetisk bokstav
            print("Ogiltig gissning. Försök igen med en bokstav.")
            continue

      #If- funktioner som utförs om man redan gissat på en bokstav,vunnit eller förlorat spelet
        if gissning in gissade_bokstaver:
            print("Du har redan gissat den bokstaven.")
        elif gissning in ordet:
            gissade_bokstaver.append(gissning)
            if all(bokstav in gissade_bokstaver for bokstav in ordet):
              print(f"Du vann!\nOrdet var {ordet.capitalize()} ({betydelsen})")
              break

        else:
            gissade_bokstaver.append(gissning)
            antal_gissningar -= 1

    else:
        print(f"Du förlorade. Rätt ord var: {ord} ({betydelsen})")

# Fråga om du vill köra igen, och rensar även tidigare spel.
while True:
    hänga_gubbe()
    fortsätt_spela = input("Vill du spela igen? (Ja/Nej): ").lower()
    os.system("clear")
    if fortsätt_spela != "ja":
        break
