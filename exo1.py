import random 

print("Bienvenue dans le jeu!")

#compteur de clés
keys = 0

#répéter les manches jusqu'a ce qu'il y ait 3 clés !!! identation, tt doit ê ds while sinon ça va pas
while keys != 3:
    print("Vous avez 5 jarres devant vous, veuillez en choisir une")

    #Choix du nombre aleatoire perdant
    snake = random.randint(1, 5)#nbre de 1 a 5 pr le hasard

    #input pour demander nbre au joueur
    nbre = int(input('numero choisi')) 

    print("vous avez choisi la jarre n°", nbre)

    #verification 
    if nbre != snake: #Gagné 
        print("Félicitations, vous obtenez une clé magique ! Le serpent était dans la jarre n°", snake)
        keys += 1 
    else: 
        print("perdu ! Un serpent apparaît")
        keys -= 1
