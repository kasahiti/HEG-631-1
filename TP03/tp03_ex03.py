# Fonctions
def initialisation_renards() -> int:
    """
    Retourne un int représentant le nombre de renards saisi par l'utilisateur
    :return: nb_renards
    """
    nb_renards: int = None

    # Repose la question tant que l'utilisateur n'a pas saisie une donnée valide
    while nb_renards is None or nb_renards < 2:
        nb_renards = int(input("Combien de renards au départ (>= 2) ?"))
    return nb_renards


def initialisation_lapins() -> int:
    """
    Retourne un int représentant le nombre de lapins saisi par l'utilisateur
    :return: nb_lapins
    """
    nb_lapins: int = None

    # Repose la question tant que l'utilisateur n'a pas saisie une donnée valide
    while nb_lapins is None or nb_lapins < 5:
        nb_lapins = int(input("Combien de lapins au départ (>= 5) ?"))
    return nb_lapins


def simulation(_duree: int, _nb_lapins: int, _nb_renards: int):
    """
    Méthode permettant de simuler l'évolution de la population de lapin et de renard et d'afficher à l'écran le résultat final
    :param _duree: int -> durée totale, en mois, de la simulation
    :param _nb_lapins: int -> nombre de lapins saisi par l'utilisateur
    :param _nb_renards: int -> nombre de renards saisi par l'utilisateur
    :return: pas de return
    """
    # Déclaration et initialisation de variables locales
    nb_lapin_1: float = _nb_lapins
    nb_renards_1: float = _nb_renards
    flag_renard: bool = False
    flag_lapin: bool = False
    flag_population_renard: bool = None
    flag_population_lapin: bool = None
    iterations: int = 0

    for i in range(1, _duree + 1):
        # Calcul de la nouvelle population de renards et de lapins
        nb_lapin_1 = calcul_croissance_lapins(_nb_lapins, _nb_renards)
        nb_renards_1 = calcul_croissance_renards(_nb_lapins, _nb_renards)
        _nb_lapins = nb_lapin_1
        _nb_renards = nb_renards_1

        # "Active" un ou plusieurs flags en fonction de l'évolution de la population de lapins et/ou de renards
        if _nb_lapins < 5:
            flag_lapin = True
        if _nb_renards < 5:
            flag_renard = True
        if flag_lapin and _nb_lapins > 5:
            flag_population_lapin = True
        if flag_renard and _nb_renards > 5:
            flag_population_renard = True
        if _nb_renards < 2:
            flag_population_renard = False
            _nb_renards = 0
        if _nb_lapins < 2:
            flag_population_lapin = False
            _nb_lapins = 0

        iterations += 1
        # Si le nombre de lapin et de renards tombe à 0, arrêter la boucle
        if _nb_lapins == 0 and _nb_renards == 0:
            _nb_lapins = 0
            _nb_renards = 0
            break

    # Affiche un récapitulatif final
    if nb_lapin_1 <= 0:
        print("\nAprès {} mois, il y a 0 lapins et {:.0f} renards".format(iterations, _nb_renards))
    elif nb_renards_1 <= 0:
        print("\nAprès {} mois, il y a {:.0f} lapins et 0 renards".format(iterations, _nb_lapins))
    else:
        print("\nAprès {} mois, il y a {:.0f} lapins et {:.0f} renards".format(iterations, _nb_lapins, _nb_renards))

    # En fonction des flags activés, affiche un message personnalisé
    check_renards(flag_renard, flag_population_renard)
    check_lapins(flag_lapin, flag_population_lapin)
    if not(flag_lapin or flag_renard):
        print("Les lapins et les renards ont des populations stables.")


def calcul_croissance_lapins(_nb_lapins: float, _nb_renards: float) -> float:
    """
    Permet de calculer mathématiquement l'évolution de la population de lapin pour le mois prochain.
    :param _nb_lapins: float -> nombre de lapin du mois précédent
    :param _nb_renards: float -> nombre de renard du mois précédent
    :return: nombre de lapins pour le prochain mois
    """
    return _nb_lapins * (1.0 + TX_LAPINS - TX_ATTAQUE * _nb_renards)


def calcul_croissance_renards(_nb_lapins: float, _nb_renards: float) -> float:
    """
    Permet de calculer mathématiquement l'évolution de la population de renard pour le mois prochain.
    :param _nb_lapins: float -> nombre de lapin du mois précédent
    :param _nb_renards: float -> nombre de renard du mois précédent
    :return: nombre de renards pour le prochain mois
    """
    return _nb_renards * (1.0 + TX_ATTAQUE * _nb_lapins * TX_RENARDS - TX_MORT_RENARD)


def check_renards(_flag_renard: bool, _population_renard: bool):
    """
    En fonction des flags renards, affiche un message différent (en voie d'extinction, remoté, disparus)
    :param _flag_renard: bool -> True si la population de renard est descendue en dessous de 5
    :param _population_renard: bool -> True si la population de renard est remonté au dessus de 5
    :return: pas de return
    """
    if _flag_renard and _population_renard:
        print("\nLes renards ont été en voie d'extinction\nmais la population est remontée ! Ouf !")
    elif _flag_renard and _population_renard is False:
        print("\nLes renards ont été en voie d'extinction\net les renards ont disparus :-(")
    elif _flag_renard:
        print("\nLes renards ont été en voie d'extinction")


def check_lapins(_flag_lapin: bool, _population_lapin: bool):
    """
    En fonction des flags lapins, affiche un message différent (en voie d'extinction, remoté, disparus)
    :param _flag_lapin: bool -> True si la population de lapin est descendue en dessous de 5
    :param _population_lapin: bool -> True si la population de lapin est remonté au dessus de 5
    :return:
    """
    if _flag_lapin and _population_lapin:
        print("Les lapins ont été en voie d'extinction\nmais la population est remontée ! Ouf !")
    elif _flag_lapin and _population_lapin is False:
        print("Les lapins ont été en voie d'extinction\net les lapins ont disparus :-(")
    elif _flag_lapin:
        print("Les lapins ont été en voie d'extinction")

# Programme Principal
# Déclaration et Initialisation des variables
DUREE: int = 50
TX_LAPINS: float = 0.4
TX_RENARDS: float = 0.008
TX_ATTAQUE: float = 0.01
TX_MORT_RENARD: float = 0.1
nb_lapins: int = None
nb_renards: int = None

# Séquence d'opérations
# Nous initialisons nos deux variable grâce aux méthodes initialisation_renards/lapins()
nb_renards = initialisation_renards()
nb_lapins = initialisation_lapins()

# Simulation de l'évolution
simulation(DUREE, nb_lapins, nb_renards)
