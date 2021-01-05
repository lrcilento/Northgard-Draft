import random

def draft(dlcEnabled, atLeastOneBasic, clansPerPerson, numberOfPlayers):
    clans = ["Goat", "Boar", "Stag", "Bear", "Raven", "Wolf"]
    dlcClans = ["Ox", "Kraken", "Horse", "Snake", "Dragon", "Lynx"]
    totalClans = len(clans)
    auxArray = []
    results = []
    final = []
    clansAssigned = 0
    player = 1

    if dlcEnabled:
        totalClans += len(dlcClans)

    if numberOfPlayers * clansPerPerson > totalClans:
        final.append("Invalid amount of clans to be assigned.\n"+str(clansPerPerson*numberOfPlayers)+" clans needed, only "+str(totalClans)+" available.")
        return final

    elif atLeastOneBasic and numberOfPlayers > len(clans):
        final.append("Invalid amount of basic clans to be assigned.\n"+str(numberOfPlayers)+" clans needed, only "+str(len(clans))+" available.")
        return final

    else:
        while numberOfPlayers != 0:
            aux = random.randint(0, 1)
            if dlcEnabled == False or (clansAssigned == 0 and atLeastOneBasic) or (aux == 0 and len(clans) != 0 and (len(clans) >= numberOfPlayers or atLeastOneBasic == False)):
                aux = random.randint(1, len(clans))
                auxArray.append(clans[aux-1])
                clansAssigned += 1
                clans.pop(aux - 1)
            elif aux == 1 and len(dlcClans) != 0:
                aux = random.randint(1, len(dlcClans))
                auxArray.append(dlcClans[aux-1])
                clansAssigned += 1
                dlcClans.pop(aux - 1)
            if clansAssigned == clansPerPerson:
                results.append(auxArray)
                auxArray = []
                numberOfPlayers -= 1
                clansAssigned = 0

    while len(results) != 0:
        aux = random.randint(1, len(results))
        result = results[aux - 1]
        results.pop(aux - 1)
        final.append({'player': player, 'clans': result})
        player += 1
    
    return final