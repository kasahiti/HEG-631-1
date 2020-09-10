# Fonctions
def demander_annee() -> int:
    """
    Demande à l'utilisateur une année tant qu'il n'a pas saisi une année entre 1583 et 4000
    :return: annee
    """
    annee: int = None
    while (annee is None) or (annee > 4000 or annee < 1583):
        annee = int(input("Entrez une année (1583-4000) : "))
    return annee


def affiche_date(_annee: int, _chiffre: int):
    """
    Affiche la date de Paques pour l'année saisie par l'utilisateur
    :param _annee: int -> année saisie par l'utilisateur
    :param _chiffre: int -> jours calculés par la fonction date_paques
    :return: pas de return
    """
    mois: str = "mars"

    # Si il y a plus de 31 jours, passer au mois d'avril
    if _chiffre > 31:
        _chiffre = _chiffre - 31
        mois = "avril"

    # Affiche la date avec l'année, le jour et le mois
    print("Date de Paques en", _annee, ":", _chiffre, mois)


def date_paques(_annee: int) -> int:
    """
    Calcul le jour de Paque en fonction de l'année saisie par l'utilisateur. Utilise l'algorithme de Gauss pour ce faire.
    :param _annee: int -> année saisie par l'utilisateur
    :return: jour
    """
    siecle: int = _annee // 100
    p: int = (13 + 8 * siecle) // 25
    q: int = siecle // 4
    m: int = (15 - p + siecle - q) % 30
    n: int = 4 + siecle - q % 7
    d: int = (m + 19 * (_annee % 19)) % 30
    e: int = (2 * (_annee % 4) + 4 * (_annee % 7) + 6 * d + n) % 7
    jour: int = e + d + 22

    return check_jour(jour, e, d, m)


def check_jour(_jour: int, _e: int, _d: int, _m: int) -> int:
    """
    Fait une vérification sur le jour et ajuste le jour en fonction des instructions détaillées dans le TP.
    :param _jour: -> paramètre jour calculé dans la fonction date_paques()
    :param _e: int -> paramètre _e
    :param _d: int -> paramètre _d
    :param _m: int -> paramètre _m
    :return: _jour
    """
    if _e == 6 and (_d == 28 or _d == 29) and ((11 * (_m + 1)) % 30) < 19:
        return _jour - 7
    else:
        return _jour

# Programme Principal
# Déclaration et Initialisation des variables
annee: int = None
jour: int = None

# Séquence d'opérations
# Demande l'année à l'utilisateur avec la fonction demander_annee()
annee = demander_annee()

# Calcul le nombre de jour à partir du 1er jour du mois de mars pour l'année saisie
jour = date_paques(annee)

# Affiche la date de Paques pour l'année saisie par l'utilisateur
affiche_date(annee, jour)
