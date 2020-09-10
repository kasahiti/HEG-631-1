"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""
# Déclaration des variables
age: int
sexe: str
fumeur: str
sport: str
risque: int

# Initialisation des variables
# Demande à l'utilisateur des informations personnelles
fumeur = input("Êtes-vous fumeur ? (oui ou non)")
sport = input("Faîtes-vous du sport ? (oui ou non)")
sexe = input("Quel est votre sexe ? (h ou f)")
age = int(input("Quel est votre age ?"))
risque = 0

# Séquence d'opération
# Si l'utilisateur est fumeur, on augmente le risque de 2
if fumeur == "oui":
    risque += 2

# Si l'utilisateur est un sportif, on diminue le risque de 1
if sport == "oui":
    risque -= 1

# Si l'utilisateur est un homme de plus de 50 ans, on augmente le risque de 1
if sexe == "h" and age > 50:
    risque += 1

# Si l'utilisateur est une femme de plus de 60 ans, on augmente le risque de 1
if sexe == "f" and age > 60:
    risque += 1

# Si le risque final est inférieur à 1, on affiche risque faible, sinon risque élevé
if risque <= 1:
    print("Le niveau de risque est faible({})".format(risque))
else:
    print("Le niveau de risque est élevé ({})".format(risque))
