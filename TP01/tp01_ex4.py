"""
Une compagnie d'assurance automobile propose à ses clients quatre familles
de tarifs identifiables par une couleur, du moins au plus onéreux :
    tarifs bleu, vert, orange et rouge.
Le tarif dépend de la situation du conducteur :
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins
      de deux ans, se voit attribuer le tarif rouge, si toutefois
      il n'a jamais été responsable d'accident.
      Sinon, la compagnie refuse de l'assurer.
    - un conducteur de moins de 25 ans et titulaire du permis depuis
      plus de deux ans, ou de plus de 25 ans mais titulaire du permis
      depuis moins de deux ans a le droit au tarif orange s'il
      n'a jamais provoqué d'accident, au tarif rouge pour un accident,
      sinon il est refusé.
    - un conducteur de plus de 25 ans titulaire du permis depuis plus de
      deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun
      accident et du tarif orange pour un accident, du tarif rouge pour
      deux accidents, et refusé au-delà
    - De plus, pour encourager la fidélité des clients acceptés,
      la compagnie propose un contrat de la couleur immédiatement la plus
      avantageuse s'il est entré dans la maison depuis plus de cinq ans.
      Ainsi, s'il satisfait à cette exigence, un client normalement "vert"
      devient "bleu", un client normalement "orange" devient "vert",
      et le "rouge" devient "orange".

Ecrire l'algorithme permettant de saisir les données nécessaires
(sans contrôle de saisie) et de traiter ce problème.

  Données : - L'Age du conducteur
            - Le nombre d'année de permis
            - Le nombre d'accidents
            - Le nombre d'années d'assurance
  Résultats : Un message spécifiant la situation du client
"""

# Déclaration des variables
TARIF_BLEU: str = "Bleu"
TARIF_VERT: str = "Vert"
TARIF_ORANGE: str = "Orange"
TARIF_ROUGE: str = "Rouge"

situation: str
age: int
nb_annee_permis: int
nb_accidents: int
nb_annee_assurance: int

# Initialisation des variables
situation = ""

# Demande à l'utilisateur des informations personnelles
age = int(input("Entrez l'âge: "))
nb_annee_permis = int(input("Entrez le nombre d'année de permis: "))
nb_accidents = int(input("Entrez le nombre d'accidents: "))
nb_annee_assurance = int(input("Entrez le nombre d'années d'assurance: "))

# Séquence d'opération
# Si l'âge est inférieur à 25 et qu'il a moins de 2 ans de permis, on regarde le nombre d'accident et stocke la situation
if age < 25 and nb_annee_permis < 2:
    if nb_accidents > 0:
        situation = "refusé"
    else:
        situation = TARIF_ROUGE

# Si l'age est inférieur à 25 avec >2 ans de permis OU si l'âge est supérieur à 25 avec moins de 2 ans de permis, on regarde le nombre d'accident et stocke la situation
elif (age < 25 and nb_annee_permis >= 2) or (age >= 25 and nb_annee_permis < 2):
    if nb_accidents == 0:
        situation = TARIF_ORANGE
    elif nb_accidents == 1:
        situation = TARIF_ROUGE
    else:
        situation = "refusé"

# Sinon si l'âge est supérieur à 25 avec plus de 2 ans de permis, on regarde le nombre d'accident et on stocke la situation
elif age >= 25 and nb_annee_permis >= 2:
    if nb_accidents == 0:
        situation = TARIF_VERT
    elif nb_accidents == 1:
        situation = TARIF_ORANGE
    elif nb_accidents == 2:
        situation = TARIF_ROUGE
    else:
        situation = "refusé"

# En fonction du nombre d'année d'assurance, on diminue le tarif
if nb_annee_assurance > 5:
    if situation == TARIF_ROUGE:
        situation = TARIF_ORANGE
    elif situation == TARIF_ORANGE:
        situation = TARIF_VERT
    elif situation == TARIF_VERT:
        situation = TARIF_BLEU

# On affiche la situation finale
print("Votre situation :", situation)
