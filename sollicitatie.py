# begin
print('*****************************************************')
print('*Vacature: Circusdirecteur voor Circus HotelDeBotel *')
print('*****************************************************')
print('* Er worden u een paar relevante vragen gesteld.    *')
print('* Gelievde deze vragen eerlijk de beantworden.      *')
print('* Als u aan alle eisen voldoet,                     *')  
print('* Komt u in aanmerking voor de baan!                *')
print('* de vragenlijst gaat nu van start                  *')
print('*****************************************************')

# De vragen
print('Hoeveel jaar heeft u ervaring met praktijkervaring dieren-dressuur?')
antwoord1 = input(': ')

print('Hoeveel jaar heeft u ervaring met jongleren?')
antwoord2 = input(': ')
    
print('Hoeveel jaar heeft u met praktijkervaring acrobatiek?')
antwoord3 = input(': ')

print('Bent u in bezit van een Diploma MBO-4 ondernemen?')
antwoord4 = input('ja/nee: ')

print('Bent u in het bezit van een geldig Vrachtwagen rijbewijs?')
antwoord5 = input('ja/nee: ')

print('Bent u in bezit van een hoge hoed?')
antwoord6 = input('ja/nee: ')

print('bent u een man of een vrouw?')
antwoord7 = input('man/vrouw: ')
if (antwoord7 == 'man'):
    print('hoeveel cm is uw snor?')
    antwoord8 = input(': ')
else:
    print('Welke stijl is u haar?')
    antwoord9 = input(': ')
    print('Welke kleur haar heeft u?')
    antwoord10 = input(': ')
    print('Hoeveel cm is u haar?')
    antwoord11 = input(': ')

print('Wat is uw lengte?')
antwoord12 = input(': ')

print('Wat is u gewicht?')
antwoord13 = input(': ')

print('Heeft u het Certificaat “Overleven met gevaarlijk personeel”')
antwoord14 = input('ja/nee: ')

# 4 Nutteloze vragen
print('Ren je sneller dan 20km/h?')
input('ja/nee: ')
print('Bent u een pro gamer?')
input('ja/nee: ')
print('Kunt u zingen?')
input('ja/nee: ')
print('Ben u wel eens van de trap gevallen?')
input('ja/nee: ')

# Mag degene soliciteren?
print('**************************************************')
if (antwoord1 >= '4' or antwoord2 >= '5' or antwoord3 >= '3' + antwoord4 == 'ja' + antwoord5 == 'ja' + antwoord6 == 'ja' + antwoord8 >= '10' or antwoord9 == 'krullen' and antwoord10 >= '20' + antwoord11 >= '150' + antwoord12 >= '90' + antwoord13 == 'ja'):
    print('Proficiat! u komt in aanmerking voor het solicitatiegesprek. Stuur u cv op en wij nemen contact met u op.')

else: 
    print('Helaas pindakaas. U voldoet niet onze eisen.')






