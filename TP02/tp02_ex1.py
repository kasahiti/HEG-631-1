"""
Considérons les opérations suivantes applicables à un nombre entier (positif) :
    — si ce nombre est divisible par 3, on lui ajoute 4 ;
    — s’il n’est pas divisible par 3 mais divisible par 4, on le divise par 2;
    — s’il n’est divisible ni par 3, ni par 4, on lui soustrait 1.
On répète ces opérations successivement jusqu’à arriver à 0.

Ecrivez un programme affichant le nombre d'opérations pour arriver à 0 pour
chaque chiffre entier compris entre deux valeurs demandées à l'utilisateur.

"""
# Déclaration et Initialisation des variables
nb_operation: int = 0
nb_utilisateur: int = None
saisie_initiale: int = None

# Tant que la saisie n'est pas valable, continuer de poser la question
while saisie_initiale is None or saisie_initiale <= 0:
    saisie_initiale = int(input("Saisissez un nombre entier positif : "))

nb_utilisateur = saisie_initiale

# Séquence d'opération
while nb_utilisateur > 0:
    # Cas où le nombre est divisible par 3
    if nb_utilisateur % 3 == 0:
        nb_utilisateur += 4
        nb_operation += 1

    # Cas où le nombre n'est pas divisible par 3 mais est divisible par 4
    elif nb_utilisateur % 3 != 0 and nb_utilisateur % 4 == 0:
        nb_utilisateur = int(nb_utilisateur / 2)
        nb_operation += 1

    # Dans tous les autres cas, on soustrait 1
    else:
        nb_utilisateur -= 1
        nb_operation += 1

# Affichage final du nombre d'opérations
print(saisie_initiale, "->", nb_operation)
