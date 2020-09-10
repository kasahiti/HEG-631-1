import random

"""
    Programme simulant un jeu de BlackJack avec des lancés de dés. L'objectif du jeu est d'arriver au plus proche de
    21 sans dépasser 21. Pour se faire l'utilisateur peut lancer un nombre de dés de son choix. Le programme simule un
    lancer de dés (en générant aléatoirement des valeurs entre 1 et 6) et obtiens une somme. L'utilisateur peut décider
    de continuer de lancer des dés supplémentaires ou de s'arrêter (entrer 0 lorsque l'on demande le nombre de dés).
    L'ordinateur joue également en parallèle avec sa propre somme et son score est affiché également. Le jeu se termine lorsque le
    joueur ET l'ordinateur ont terminé de jouer.

    Indications:
        - Si le joueur entre 0 comme nombre de dés à lancer, cela signifie qu'il arrête de lancer plus de dés et sa partie se termine
        - Voici le détail sur la stratégie de jeu de l'ordinateur:
            - Si la somme de l'ordinateur est inférieure à 6, il demande 3 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 6 et inférieure à 12, il demande 2 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 12 et inférieure à 18, il demande 1 dés
            - Si la somme de l'ordinateur est supérieure ou égale à 18, il s'arrête de jouer

"""

# Déclaration et Initialisation des variables
MIN_DES: int = 1
MAX_DES: int = 6

# Variables "joueur"
somme_des_joueur: int = 0
resultat_joueur: int = 0
des_joueur: int = None
nombre_lancer_des_joueur: int = None

# Variables "ordinateur"
somme_des_ordi: int = 0
resultat_ordi: int = 0
des_ordi: int = None
nombre_lancer_des_ordi: int = None

# Séquence d'opération
# Pose des questions tant que le joueur n'a pas dépassé 21 ou tant que l'ordinateur n'a pas dépassé 18.
while somme_des_joueur <= 21 and somme_des_ordi <= 18:
    nombre_lancer_des_joueur = int(input("Combien de dés souhaitez-vous lancer ? "))

    if nombre_lancer_des_joueur > 0:
        # Pour chaque dé lancé, le prog. choisi un chiffre aléatoire, stocke cette info, et recommance. Print final du score total.
        for nombre_lancer_des_joueur in range(1, nombre_lancer_des_joueur+1):
            resultat_joueur = random.randint(MIN_DES, MAX_DES)
            somme_des_joueur += resultat_joueur
        print("Vous avez un score de \t{}\n".format(somme_des_joueur))

    if nombre_lancer_des_joueur == 0:
        # Si l'utilisateur ne veut plus lancer de dé, affiche le score final et quitte la boucle while.
        print("Vous avez un score de \t{}\n".format(somme_des_joueur))
        break

    # Ce block d'if-elif traduit la stratégie de l'ordinateur et le nombre de dés à lancer en fonction de son score.
    if somme_des_ordi < 6:
        nombre_lancer_des_ordi = 3
        print("L'ordinateur choisi {} dés".format(nombre_lancer_des_ordi))
        for nombre_lancer_des_ordi in range(nombre_lancer_des_ordi):
            resultat_ordi = random.randint(MIN_DES, MAX_DES)
            somme_des_ordi += resultat_ordi
        print("L'ordinateur a un score de \t{}\n".format(somme_des_ordi))
    elif 6 <= somme_des_ordi < 12:
        nombre_lancer_des_ordi = 2
        print("L'ordinateur choisi {} dés".format(nombre_lancer_des_ordi))
        for nombre_lancer_des_ordi in range(nombre_lancer_des_ordi):
            resultat_ordi = random.randint(MIN_DES, MAX_DES)
            somme_des_ordi += resultat_ordi
        print("L'ordinateur a un score de \t{}\n".format(somme_des_ordi))
    elif 12 <= somme_des_ordi < 18:
        nombre_lancer_des_ordi = 1
        print("L'ordinateur choisi {} dés".format(nombre_lancer_des_ordi))
        for nombre_lancer_des_ordi in range(nombre_lancer_des_ordi):
            resultat_ordi = random.randint(MIN_DES, MAX_DES)
            somme_des_ordi += resultat_ordi
        print("L'ordinateur a un score de \t{}\n".format(somme_des_ordi))
    elif somme_des_ordi >= 18:
        nombre_lancer_des_ordi = 0
        print("L'ordinateur choisi {} dés".format(nombre_lancer_des_ordi))
        for nombre_lancer_des_ordi in range(nombre_lancer_des_ordi):
            resultat_ordi = random.randint(MIN_DES, MAX_DES)
            somme_des_ordi += resultat_ordi
        print("L'ordinateur a un score de \t{}\n".format(somme_des_ordi))

# A la fin du programme, compare le score final et affiche le résultat.
if 21 >= somme_des_joueur > somme_des_ordi or somme_des_ordi > 21:
    print("Vous avez gagné ({}) contre l'ordinateur ({})".format(somme_des_joueur, somme_des_ordi))
elif somme_des_joueur == somme_des_ordi:
    print("Vous êtes à égalité ({}) contr l'ordinateur ({})".format(somme_des_joueur, somme_des_ordi))
elif somme_des_joueur < somme_des_ordi <= 21 or somme_des_joueur > 21:
    print("Vous avez perdu ({}) contre l'ordinateur ({})".format(somme_des_joueur, somme_des_ordi))
