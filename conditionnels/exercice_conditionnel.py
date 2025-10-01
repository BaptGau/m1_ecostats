# v = input("Saisissez une valeur : ")
# print(v)
from time import sleep
from unittest import case

# Exercice
# Vous codez le software du micro onde
# 1.
# Demandez une valeur à l'utilisateur qui correspond au temps de cuisson en secondes
# Si le temps de cuisson est supérieur à 5 minutes > afficher un message d'erreur (print/raise)

# 2.
# Demandez à l'utilisateur la commande qu'il veut saisir :
# 3 cas autorisés:
# - Ouvrir le micro onde (Open)
# - Fermer le micro onde (Close)
# - Lancer une cuisson (Launch)
# Gérer les cas et générer un message d'erreur sinon

# Exercice 1
temps_cuisson_secondes = int(input("Saisissez le temps de cuisson en secondes: "))
temps_cuisson_minutes = temps_cuisson_secondes / 60

if temps_cuisson_minutes > 5:
    raise ValueError(
        "Le micro-ondes ne supportes pas des temps de cuisson supérieurs à 5 minutes."
    )
else:
    print("Cuisson en cours")


# Exercice 2
## solution 1
command_to_run = input("Quelle commande voulez-vous exécuter: ")
if command_to_run == "Open":
    print("Micro-ondes ouvert")
elif command_to_run == "Close":
    print("Couleur ouvert")
elif command_to_run == "Launch":
    print("Lancement de la cuisson")
else:
    raise ValueError("Commande non connue")

## solution 2
command_to_run = input("Quelle commande voulez-vous exécuter: ")
match command_to_run:
    case "Open":
        print("Micro-ondes ouvert")
    case "Close":
        print("Couleur ouvert")
    case "Launch":
        print("Lancement de la cuisson")
    case _:
        raise ValueError("Commande non connue")
