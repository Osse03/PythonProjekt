import random

antal_gissningar_i_rad = []

def meny(): # här är altenativer för meny. 
    print('1. The Power Of Two')
    print('2. TäningsSpel')
    print('3. Gissa Slump Tal')
    print('4. Avsluta Programmet')


def Power_Of_Two():
    x = 21
    inp = int(input('välj ett tal som vi ska upphöja med 2:'))
    if inp > x:
        print('Du valde ett tal större än 2^21. Vänligen välj ett mindre tal.')
    else:
        for n in range(inp + 1):
            result = 2 ** n
            print(f'2 upphöjt till {n} är: {result}')
            

def TärningSpel():
    omgångar = int(input('Hur många omgångar vill du spela:' ))
    
    #olika variablar som jag kommer använda.
    Dina_vinster = 0
    Dators_vinster = 0
    Dina_totala_poäng = 0
    Dators_totala_poäng = 0
    min_kast = 6
    max_kast = 1

    for omgångar in range(omgångar):
        input('Tryck enter för att kasta tärningen igen.')
        
        # random för att kasta slumpmässigt mellan 1-6
        Dina_kast = random.randint(1, 6)
        Dators_kast = random.randint(1, 6)
        
        Dina_totala_poäng += Dina_kast
        Dators_totala_poäng += Dators_kast
        
        print(f'\nDu fick {Dina_kast}, Datorn fick {Dators_kast}')

        if Dina_kast > Dators_kast:
            Dina_vinster += 1
            print('Du vann omgången :).')
        elif Dina_kast < Dators_kast:
            Dators_vinster += 1
            print('Datorn vann omgången :(.')
        else:
            print('Matchen är oavgjort')
              
    #Statistik
    Din_medelvärde = Dina_totala_poäng / omgångar
    Dators_medelvärde = Dators_totala_poäng / omgångar
    
    min_kast = min(min_kast, Dina_kast, Dators_kast)
    max_kast = max(max_kast, Dina_kast, Dators_kast)

    print('\nResultat efter alla omgångar:')
    print(f'Antal vinster för dig: {Dina_vinster}')
    print(f'Antal vinster för datorn: {Dators_vinster}')
    
    print ('\nStatstik:')
    print (f'Medelvärdet för dina kast: {Din_medelvärde}')
    print(f'Medelvärdet för dators kast: {Dators_medelvärde}')
    print(f'Högsta kast: {max_kast}')
    print(f'Minsta kast: {min_kast}')

def GissaSlumpTal():
    global antal_gissningar_i_rad
    slump_tal = random.randint(1, 100)
    antal_gissningar = 0
    

    while True:
        gissning = int(input('Gissa ett tal mellan 1 och 100: '))
        antal_gissningar += 1

        if gissning > slump_tal:
            print('För högt!')
        elif gissning < slump_tal:
            print('För lågt!')
        else:
            print(f'Rätt gissat!! du gissade rätt tal {slump_tal} på {antal_gissningar} försök ')
            break

    if antal_gissningar <= 7:
        print('Bra jobbat :)')
    else:
        print('Så många försök borde det inte ta')

    # här använder jag global variablel för gissningar i rad.
    antal_gissningar_i_rad.append(antal_gissningar)
    antal_gissningar_i_rad = antal_gissningar_i_rad [-3:]

    if len(antal_gissningar_i_rad) == 3 and all(gissning <=7 for gissning in antal_gissningar_i_rad):
        print('Fantastiskt jobbat! Du har besviligen en bra strategi.')


def main(): 
    meny()
    val = int(input('Vilket spel vill du spela (ange mellan 1/2/3):'))

    while val != 4: # om användare inte väljer 4 så kör loopen annars stannar den. 
        if val == 1:
            print('Val 1 blev kallad.')
            Power_Of_Two()
            while True:
                val = input ('Vill du köra spelet igen? (yes/no):')
                if val.lower() == 'yes': 
                    print ('Spelet startas om.')
                    Power_Of_Two()

                elif val.lower() == 'no':
                    print ('Tack för att du spelade, Hejdå!')
                    main() # här skriver main() för att om använder väljer de så går man tillbaka till meny.
                    break
                else:
                    print('O giltig val, vänligen ange yes eller no.')
        elif val == 2:
            print('Val 2 blev kallad.')
            TärningSpel()
            while True:
                val = input ('\nVill du köra spelet igen? (yes/no):')
                if val.lower() == 'yes':
                    print ('Spelet startas om.')
                    TärningSpel()
                    
                elif val.lower() == 'no':
                    print ('Tack för att du spelade, Hejdå!')
                    main()
                    break
                else:
                    print('O giltig val, vänligen ange yes eller no.')
        elif val == 3:
            print('Val 3 blev kallad.')
            GissaSlumpTal()
            while True:
                val = input ('Vill du köra spelet igen? (yes/no):')
                if val.lower() == 'yes':
                    print ('Spelet startas om.')
                    GissaSlumpTal()
                elif val.lower() == 'no':
                    print ('Tack för att du spelade, Hejdå!')
                    main()
                    break
                else:
                    print('O giltig val, vänligen ange yes eller no.')
main()