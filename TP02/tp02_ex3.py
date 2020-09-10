"""
    Programme permettant de savoir si un trajet ou une série de trajet sont réalisable par rapport
    au réservoir d'essence d'une voiture. Pour ce faire il faut spécifier une distance en kilometres
    et un nombre de passagers à bord(sans compte le conducteur).
    Indications:
        - Le véhicule a les caractéristiques suivantes :
            - Une consommation fixe de 5.0 litre pour 100km
            - Pour chaque personne ajoutée (le conducteur ne compte pas), l'essence utilisée augmente de 30%
              en rapport à la consommation normale
                - Exemple : pour 1 personne en plus du conducteur, la consommation vaut 1.3 fois la consommation normale
                            pour 2 personnes en plus du conducteur, la consommation vaut 1.6 fois la consommation normale
        - Lors de la saisie de la distance, si l'utilisateur met 0, le programme rempli le réservoir d'essence
          du véhicule
        - Lorsque qu'un voyage est réalisable, un message affiche le nombre de litres restants
        - Le programme se termine uniquement si une panne d'essence se produit. Si cela arrive,
          Un message affiche que la panne arrivera lors de ce trajet. Un second message affichera
          la distance parcourue avec tous les trajets.

"""
# Déclaration et  Initialisation des variables
MAX_CAP_RESERVOIR: float = 32.5
reservoir: float = MAX_CAP_RESERVOIR
distance_saisie: int = None
distance_max: float = None
distance_totale: float = 0.0
nb_personnes: int = None
consommation: float = None

# Séquence d'opération
# Tant que le reservoir n'est pas vide, le programme continue de poser des questions.
while reservoir > 0.0:
    distance = int(input("Entrez la distance de votre destination ou entrez 0 pour faire le plein :"))

    # Si la distance saisie = 0, remplir le réservoir d'essence et reposer la question de la distance à l'utilisateur.
    while distance == 0:
        reservoir = MAX_CAP_RESERVOIR
        distance_max = 100 * reservoir / 5
        print("Le réservoir est rempli totalement")
        distance = int(input("Entrez la distance de votre destination ou entrez 0 pour faire le plein :"))

    nb_personnes = int(input("Combien de personnes font parties du trajet en plus du conducteur ? "))

    # Pose la consommation à 1 pour 1 personne; pour chaque personne supplémentaire, augmente la consommation de 0.3.
    consommation = 1
    for i in range(1, nb_personnes+1):
        consommation += 0.3

    # Calcul ce qu'il reste dans le réservoir et la distance maximum que l'on peut parcourir avec.
    reservoir = round(reservoir - (distance * 5 / 100) * consommation, 2)
    distance_max = 100 * reservoir / 5

    # Si la distance voulue est + grande que la distance maximum posible, afficher le message d'avertissement.
    if distance > distance_max:
        print("Vous allez tomber en panne d'essence lors de ce trajet! Pensez à le raccourcir ou faire le plein.")
        break
    else:
        print("Il vous reste {}litres d'essence".format(reservoir))

    # Calcul de la distance totale depuis le début du programme.
    distance_totale = distance_totale + distance

# A la fin du programme, affichage d'un récapitulatif.
if distance_totale <= 0:
    print("Vous aurez parcouru 0.0 km")
elif distance_totale > 0:
    print("Vous avez parcouru", distance_totale, "km")
