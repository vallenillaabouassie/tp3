import random
hp = 20
print("Vous êtes attrapés dans le dongeon! pour fuire, il vous faut tuer 3 monstres pour retrouver la sortie")

def hud():
    print("Vous tombez face a face avec un monstre!")
    choice = int(input("Que voulez - vous faire ? 1 - Combattre cet adversaire 2 - Contourner cet adversaire et aller ouvrir une autre porte 3 - Afficher les regles du jeu 4 - Quitter la partie : "))
    if choice == 1:
        dice = random.randint(1,6)
        print(f"Votre de a donne {dice}")
        force_adversaire = random.randint(1,5)
        print(f"Le de de l'ennemi est de {force_adversaire}")
        print("...")
        if dice > force_adversaire:
            print("Reussite!")

        else:
            print("Defaite..")

    elif choice == 2:
        print("2")

    elif choice == 3:
        print("3")

    elif choice == 4:
        exit()

hud()






