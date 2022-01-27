import random
class Player :
    def __init__ (self,pseudo):
        self.__pseudo = pseudo
        self.__score0 = 0
        self.__score1 = 0
        self.__score2 = 0
        self.__score3 = 0
        self.__score4 = 0
    
    def getPseudo (self):
        return self.__pseudo

    def getScore (self,numero):
        
        if numero == 0:
            return self.__score0
        if numero == 1:
            return self.__score1
        if numero == 2:
            return self.__score2
        if numero == 3:
            return self.__score3
        if numero == 4:
            return self.__score4

    def bestScore (self):
        stock = self.__score0

        if stock < self.__score1:
            stock = self.__score1
        if stock < self.__score2:
            stock = self.__score2
        if stock < self.__score3:
            stock = self.__score3
        if stock < self.__score4:
            stock = self.__score4
        print("Votre meilleur score est de",stock,"points !")
   
    def moyenne (self):

        moyenne = (self.__score0 + self.__score1 + self.__score2 + self.__score3 + self.__score4) // 5

        print("La moyenne de vos scores est de",moyenne,"points !")

    def pireScore (self): 

        stock = self.__score0

        if stock > self.__score1:
            stock = self.__score1
        if stock > self.__score2:
            stock = self.__score2
        if stock > self.__score3:
            stock = self.__score3
        if stock > self.__score4:
            stock = self.__score4
        print("Votre pire score est de",stock,"points !")

    def play (self,numero):
        if numero == 0:
            print("Vous avez sélectionner la chanson",numero," !")
            self.__score0 = 50
            score = random.randint(0,50)
            self.__score0 = self.__score0 + score
            print("Chanson terminée ! Votre score est de",self.__score0,"points !")

        if numero == 1:
            print("Vous avez sélectionner la chanson",numero," !")
            self.__score1 = 50
            score = random.randint(0,50)
            self.__score1 = self.__score1 + score
            print("Chanson terminée ! Votre score est de",self.__score1,"points !")

        if numero == 2:
            print("Vous avez sélectionner la chanson",numero," !")
            self.__score2 = 50
            score = random.randint(0,50)
            self.__score2 = self.__score2 + score
            print("Chanson terminée ! Votre score est de",self.__score2,"points !")

        if numero == 3:
            print("Vous avez sélectionner la chanson",numero," !")
            self.__score3 = 50
            score = random.randint(0,50)
            self.__score3 = self.__score3 + score
            print("Chanson terminée ! Votre score est de",self.__score3,"points !")

        if numero == 4:
            print("Vous avez sélectionner la chanson",numero," !")
            self.__score4 = 50
            score = random.randint(0,50)
            self.__score4 = self.__score4 + score
            print("Chanson terminée ! Votre score est de",self.__score4,"points !")


