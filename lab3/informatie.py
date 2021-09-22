naam = 'naam'
leeftijd = 'leeftijd'

def informatie():
    print("Hallo", naam, "je leeftijd is ", leeftijd)
while naam != 'stop' and leeftijd != 'stop':
    naam = input("Wat is uw naam?  : ")
    if naam.lower() == 'stop':
        break
    leeftijd = input("Wat is uw leeftijd?  : ")
    if leeftijd.lower() == 'stop':
        break
    informatie()