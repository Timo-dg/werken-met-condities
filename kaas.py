#Timo de Gruiter 
#kaas opdracht


print(' ')
print('Welke kaas is het? dat is de kaasvraag ')
print(' ')
print('----------------------------------------')
print('is jou kaas geel?')
print('ja/nee')

response1 = input('Antwoord: ')
if (response1 == 'ja' ):
    
    print('Zitten er gaten in?')  
    print('ja/nee')
    response2 = input('Antwoord: ')
    if (response2 == 'ja'):
    
        print('Is de kaas belachelijk duur?')
        print('ja/nee')
        response3 = input('Antwoord: ')
        if (response3 == 'ja'):
            print('Emmenthaler')
            print('----------------------------------------')
            
        else:
            print('Leerdammer')
            print('----------------------------------------')
    else:
        print('Is de kaas hard als steen')
        print('ja/nee')
        response4 = input('Antwoord: ')
        if (response4 == 'ja'):
            print('Pamigiano Reggiano')
            print('----------------------------------------')
        else:
            print('Goudse Kaas')
            print('----------------------------------------')


    
else:
    print('Heeft de kaas blauwe schimmel?')
    print('ja/nee')
    response5 = input('Antwoord: ')
    if (response5 == 'ja'):
        print('Heeft de kaas een korst?')
        print('ja/nee')
        response6 = input('Antwoord: ')
        if (response6 == 'ja'):
            print('Blue de Rochbaron')
            print('----------------------------------------')


        else: 
            print('Foume d`Ambert')
            print('----------------------------------------')

    
    else:
        print('Heeft de kaas een korst?')
        print('ja/nee')
        response7 = input('Antwoord: ')
        if (response7 == 'ja'):
            print('Camembert')
            print('----------------------------------------')
            
        else:
            print('Mozzarella')
            print('----------------------------------------')

