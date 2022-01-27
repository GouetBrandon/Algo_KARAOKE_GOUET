import random
from Player import Player



nbPlayer = int(input("Veuillez choisir le nombre de joueurs ( max 5, faut pas abuser ) : "))
while nbPlayer < 1 or nbPlayer > 5:
    nbPlayer = int(input("ENTRE 1 ET 5 ! : "))

concurrents = []

for i in range(nbPlayer):
    player = str(input("Veuillez choisir un pseudo : "))
    player = Player (player) 
    concurrents.append(player)
    print ("Nouveau joueur inscrit ! ",player.getPseudo()," !")

for j in range(10):
    for i in range(nbPlayer):
        actualPlayer = concurrents[i].getPseudo()
        print("C'est au tour de ",actualPlayer," !")
        choix = int(input("Veuillez choisir une action. 1: Jouer 2: Voir Score 3: Meilleur Score 4:Moyenne des Score 5: Pire Score : "))
        while choix < 1 or choix > 5:
            choix = int(input("Une action de 1 à 5 ! : "))
        if choix == 1:
            chanson = int(input("Veuillez sélectionnez la chanson entre 0 et 4 : "))
            while chanson < 0 or chanson > 4:
                chanson = int(input("Une action de 0 à 4 ! : "))
            concurrents[i].play(chanson)

        if choix == 2:
            score = int(input("Veuillez choisir le numéro de la chanson dont vous voulez voir le score : "))
            while score < 0 or score > 4:
                score = int(input("Entre 0 et 4 ! :"))
            print("Votre score sur la chanson",score,"est de",concurrents[i].getScore(score))
        
        if choix == 3:
            concurrents[i].bestScore()

        if choix == 4:
            concurrents[i].moyenne()

        if choix == 5:
            concurrents[i].pireScore()
