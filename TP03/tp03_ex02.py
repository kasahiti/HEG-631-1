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
    Méthode permettant de simuler l'évolution de la population de lapin et de renard et d'afficher à l'écran les résultats
    :param _duree: int -> durée totale, en mois, de la simulation
    :param _nb_lapins: int -> nombre de lapins saisi par l'utilisateur
    :param _nb_renards: int -> nombre de renards saisi par l'utilisateur
    :return: pas de return
    """
    # Déclaration et initialisation de variables locales
    nb_lapin_1: float = _nb_lapins
    nb_renards_1: float = _nb_renards

    for i in range(1, _duree + 1):
        # Calcul de la nouvelle population de renards et de lapins
        nb_lapin_1 = calcul_croissance_lapins(_nb_lapins, _nb_renards)
        nb_renards_1 = calcul_croissance_renards(_nb_lapins, _nb_renards)
        _nb_lapins = nb_lapin_1
        _nb_renards = nb_renards_1

        # En fonction du nombre de lapin ou de renards, afficher l'un des messages suivants pour chaque itération/mois
        if nb_lapin_1 < 0:
            print("Après {} mois, il y a 0.0 lapins et {:.2f} renards".format(i, _nb_renards))
        elif nb_renards_1 < 0:
            print("Après {} mois, il y a {:.2f} lapins et 0.0 renards".format(i, _nb_lapins))
        else:
            print("Après {} mois, il y a {:.2f} lapins et {:.2f} renards".format(i, _nb_lapins, _nb_renards))


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
