import random 

print("Bienvenue dans le jeu!")
print("Vous avez 5 jarres devant vous, veuillez en choisir une")

#Choix du nombre aleatoire perdant
snake = random.randint(1, 5)#nbre de 1 a 5 pr le hasard

#input pour demander nbre au joueur
nbre = int(input('numero choisi')) 

print("vous avez choisi la jarre n°", nbre)

#verification 
if nbre == snake: #perdu 
    print("perdu ! Un serpent apparaît")
else: 
    print("Félicitation, vous obtenez une clé magique !")
