""" TP04 - Kastriot Sahiti
"""
import sys
import os


# Fonctions
def arguments() -> list:
    """
    Fonction permettant de récupérer le chemin saisi par l'utilisateur (argument de la console/terminal),
    :return: _liste_fichiers
    """
    # Déclaration de variables locales (liste des fichier, le chemin saisi par l'utilisateur dans la console, et la liste des fichiers contenu dans ce chemin)
    _liste_fichiers: list = []
    _chemin: str = sys.argv[1]
    _fichiers = os.listdir(_chemin)

    # Pour chaque fichier dans le dossier spécifié par l'utilisateur, et s'il s'agit d'un fichier texte, ajouter son chemin complet dans la liste des _fichiers
    for i in _fichiers:
        if '.txt' in i:
            _liste_fichiers.append(_chemin + "\\" + i)

    # Retourne la liste des fichiers (chemins complets)
    return _liste_fichiers


def demander_saisie() -> list:
    """
    Demande à l'utilisateur de saisir une phrase
    :return: la saisie "nettoyée"
    """
    return nettoyage(input("Veuillez saisir une phrase: ")).split()


def nettoyage(_input: str) -> str:
    """
    Fonction supprimant les caractères inutiles (" ' ", " , ", " . ") et transformant la chaines en minuscule
    :param _input: str -> chaine de caractères dont il faut supprimer les caractères inutiles
    :return: _input
    """
    return _input.replace("'", " ").replace(",", "").replace(".", "").lower().strip()


def dictionnaire_ligne(_ligne: str, _dictionnaire: dict):
    """
    Fonction permettant transformer la ligne en cours en dictionnaire (comptage des occurrences des mots)
    :param _ligne: str -> ligne en cours de traitement (dans le fichier en cours de lecture)
    :param _dictionnaire: dict -> dictionnaire des textes
    :return: _ligne, _dictionnaire
    """
    # Variables locales
    _dictionnaire = {}
    _ligne = nettoyage(_ligne).split()

    # Pour chaque element dans la ligne en cours de traitement, si l'élément n'est pas dans le dictionnaire, l'ajouter et rajouter 1 comme valeur
    for elt in _ligne:
        if elt not in _dictionnaire:
            _dictionnaire[elt] = 1
        else:
            _dictionnaire[elt] += 1

    return _ligne, _dictionnaire


def frequence(_saisie: list, _dictionnaire: dict, _dictionnaire_saisie: dict) -> dict:
    """
    Permet de mettre dans un dictionnaire la saisie de l'utilisateur afin de pouvoir déterminer la fréquence par la suite
    :param _saisie: str -> saisie de l'utilisateur
    :param _dictionnaire: dict -> dictionnaire des fichiers
    :param _dictionnaire_saisie: dict -> dictionnaire de la saisie de l'utilisateur
    :return: _dictionnaire_saisie
    """
    # Remise à zéro de la variable _dictionnaire_saisie
    _dictionnaire_saisie = {}

    # Pour chaque élément de la saisie, si l'élément est dans le dictionnaire des fichier, l'ajouter dans le dictionnaire de la saisie
    for elt in _saisie:
        if elt in _dictionnaire:
            _dictionnaire_saisie[elt] = _dictionnaire[elt]

    return _dictionnaire_saisie


def calcul_frequenece(_dictionnaire: dict) -> int:
    """
    Permet de calculer de la somme des fréquences
    :param _dictionnaire: dict -> dictionnaire des fichiers
    :return: somme des fréquences
    """
    return sum(_dictionnaire.values())


def affichage_resultats(_compteur: int, _ligne: list):
    """
    Fonction affichant les résultats (la proximité de la saisie utilisateur aux fichiers textes)
    :param _compteur: int -> compteur utilisé pour le calcul
    :param _ligne: -> ligne du texte en cours de lecture
    :return:
    """
    longueur: int = len(_ligne)
    proximite: float = _compteur / longueur
    print("ce qui fait une proximité de", round(proximite, 2), "au texte", fichiers[i].split("\\")[len(fichiers[i].split("\\")) - 1])


# Déclaration et Initialisation des variables
dictionnaire_saisie: dict = {}
dictionnaire_fichier: dict = {}
fichiers: list = []
saisie: list = []
compteur: int = 0

# Programme Principal
# Si la portée est main, exécuter le programme principal
if __name__ == '__main__':
    # Demander une première fois une saisie utilisateur
    while True:
        fichiers = arguments()
        saisie = demander_saisie()

        # Si la saisie utilisateur est "Enter", i.e. si la liste "saisie" est vide, alors quitter la boucle while
        if len(saisie) <= 0:
            break

        # Pour chaque fichier dans la liste des fichiers, lire chaque ligne est calculer les fréquences d'apparitions de chaque mot
        for i in range(len(fichiers)):
            # Encodage UTF-8-SIG pour avoir les mêmes résultats que sur le .docx
            with open(fichiers[i], "r", encoding="utf-8-sig") as filin:
                for ligne in filin.readlines():
                    ligne, dictionnaire_fichier = dictionnaire_ligne(ligne, dictionnaire_fichier)
                    dictionnaire_saisie = frequence(saisie, dictionnaire_fichier, dictionnaire_saisie)
                    compteur = calcul_frequenece(dictionnaire_saisie)

                    # Affichage des résultats
                    affichage_resultats(compteur, ligne)
