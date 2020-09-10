from mots_pendus import tirer_mot


# Fonctions
def affichage_mot_cache(_mot: str, _lettres: str, _erreurs: int):
    """
    Cette fonction affichera le mot caché et les lettres déjà trouvées sous la forme "_ _ o _ _ i" par exemple.
    Elle affiche également le nombre de tentatives restantes
    :param _mot: str -> le mot qu'il faut deviner
    :param _lettres: str -> les lettres déjà saisies par l'utilisateur
    :param _erreurs: int -> le nombre de tentatives restantes
    :return: pas de return
    """
    lettres_trouvees: str = ""
    for i in _mot:
        if i in _lettres:
            lettres_trouvees += i + " "
        else:
            lettres_trouvees += "_ "
    print(lettres_trouvees, "\t\t ({} erreurs restantes)".format(_erreurs))


def tirage_lettre(_lettres: str) -> str:
    """
    Cette fonction demandera à l’utilisateur de saisir une lettre et reposera la question tant que la lettre entrée a déjà été choisie.
    :param _lettres: str -> lettres déjà tirées
    :return: _lettres
    """
    saisie: str = None
    while True:
        saisie = input("Veuillez entrer une lettre que vous n'avez pas choisie avant : ")
        if saisie in _lettres:
            saisie = input("Veuillez entrer une lettre que vous n'avez pas choisie avant : ")
        else:
            _lettres += saisie
            break
    return _lettres


def verification_mot(_mot: str, _lettres: str) -> bool:
    """
    Cette fonction vérifiera si le mot a effectivement été trouvé.
    :param _mot: str -> le mot qu'il faut deviner
    :param _lettres: str -> les lettres saisies par l'utiliseur; sera comparé avec _mot
    :return: True si le mot a été trouvé, False sinon
    """
    compteur: int = 0
    for i in range(len(_mot)):
        if _lettres.find(_mot[i]) != -1:
            compteur += 1
    if compteur == len(_mot):
        return True
    else:
        return False


def diminuer_erreurs(_erreurs: int) -> int:
    """
    La fonction retourne le nombre de tentatives restantes diminué de 1
    :param _erreurs: int -> le nombre de tentatives restantes
    :return: _erreurs
    """
    _erreurs -= 1
    return _erreurs


# Programme principal
# Déclaration et Initialisation des variables
MOT: str = tirer_mot()
mot_trouve: bool = None
saisie_util: str = None
tentatives: int = 10
lettres: str = ""

# Séquence d'opérations
while True:
    # Commence par afficher le mot caché avec le nombre de tentatives autorisées
    affichage_mot_cache(MOT, lettres, tentatives)

    # L'utilisateur tire une lettre
    lettres = tirage_lettre(lettres)

    # Si la lettre saisie par l'utilisateur n'est pas dans le mot, diminuer le nombre de tentatives
    if lettres[len(lettres)-1] not in MOT:
        tentatives = diminuer_erreurs(tentatives)

    # Si le nombre de tentatives restantes est de 0, afficher "Vous avez perdu" et terminer le programme
    if tentatives == 0:
        print("Vous avez perdu ! Le mot était :", MOT)
        break

    # Si le mot est trouvé, afficher "Bravo" et terminer le programme
    mot_trouve = verification_mot(MOT, lettres)
    if mot_trouve:
        print("Bravo vous avez trouvé le mot !", MOT)
        break
