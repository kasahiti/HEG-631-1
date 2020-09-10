from outils import est_egal_a, coordonnee_x, coordonnee_y, creer_caisse, creer_case_vide, creer_cible, creer_image, \
    creer_mur, creer_personnage
import time
import os


# Fonctions à développer
def jeu_en_cours(caisses: list, cibles: list) -> bool:
    """
    Fonction testant si le jeu est encore en cours et retournant un booléen comme réponse sur l'état de la partie.
    :param caisses: La liste des caisses du niveau en cours
    :param cibles: La liste des cibles du niveau en cours
    :return: True si la partie est finie, False sinon
    """
    # Ne rien faire si un des paramètres est None
    if None in (caisses, cibles):
        return None

    # Déclaration des variables locales - utilisées pour savoir si les caisses sont sur les cibles
    caisses_coord: list = []
    cibles_coord: list = []
    partie_finie: bool = True

    for caisse in caisses:
        caisses_coord.append((coordonnee_x(caisse), coordonnee_y(caisse)))

    for cible in cibles:
        cibles_coord.append((coordonnee_x(cible), coordonnee_y(cible)))

    # Si toutes les caisses ne sont pas sur des cibles, alors la partie n'est pas finie
    for cible_coord in cibles_coord:
        if cible_coord not in caisses_coord:
            partie_finie = False
            break

    return partie_finie


def charger_niveau(joueur: list, caisses: list, cibles: list, murs: list, path: str):
    """
    Fonction permettant de charger depuis un fichier.txt et de remplir les différentes listes permettant le
    fonctionnement du jeu (joueur, caisses, murs, cibles)
    :param joueur: liste des personnages
    :param caisses: liste des caisses
    :param cibles: liste des cibles
    :param murs: liste des murs
    :param path: Chemin du fichier.txt
    :return:
    """
    # Si le chemin "path" n'est pas un fichier, ne rien faire
    if not os.path.isfile(path):
        return None

    # Ne rien faire si un des paramètres est None
    if None in (joueur, caisses, cibles, murs, path):
        return None

    # Déclaration des variables locales
    ligne: str = None
    lignes: list = []

    # Lecture du fichier : chaque ligne est une liste insérée dans la liste "lignes"
    with open(path, 'r') as filin:
        while ligne != '':
            ligne = filin.readline().replace('\n', '')
            if ligne != '':
                lignes.append(list(ligne))

    # En fonction du caractère sur chaque ligne, créer un personnage, une caisse, une cible, ou un mur (cf. énoncé)
    for i in range(len(lignes)):
        for j in range(len(lignes[i])):
            if lignes[i][j] == '@':
                joueur.append(creer_personnage(j * DISTANCE_ENTRE_CASE + X_PREMIERE_CASE,
                                               i * DISTANCE_ENTRE_CASE + Y_PREMIERE_CASE))
            elif lignes[i][j] == '$':
                caisses.append(creer_caisse(j * DISTANCE_ENTRE_CASE + X_PREMIERE_CASE,
                                            i * DISTANCE_ENTRE_CASE + Y_PREMIERE_CASE))
            elif lignes[i][j] == '.':
                cibles.append(creer_cible(j * DISTANCE_ENTRE_CASE + X_PREMIERE_CASE,
                                          i * DISTANCE_ENTRE_CASE + Y_PREMIERE_CASE))
            elif lignes[i][j] == '#':
                murs.append(creer_mur(j * DISTANCE_ENTRE_CASE + X_PREMIERE_CASE,
                                      i * DISTANCE_ENTRE_CASE + Y_PREMIERE_CASE))


def mouvement(direction: str, can, joueur: list, murs: list, caisses: list, liste_image: list):
    """
    Fonction permettant de définir les cases de destinations (il yj en a 2 si le joueur pousse une caisse) selon la
    direction choisie.
    :param direction: Direction dans laquelle le joueur se déplace (droite, gauche, haut, bas)
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param joueur: liste des joueurs
    :param murs: liste des murs
    :param caisses: liste des caisses
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    """
    # Ne rien faire si un des paramètres est None
    if None in (direction, can, joueur, murs, caisses, liste_image):
        return None

    # Coordonnées du joueur
    xj: int = coordonnee_x(joueur[0])
    yj: int = coordonnee_y(joueur[0])

    # En fonction de la direction prise par le joueur, appel de la fonction "effectuer_mouvement()" en y insérant les paramètres nécessaires
    if direction == 'droite':
        effectuer_mouvement(creer_case_vide(xj + DISTANCE_ENTRE_CASE, yj),
                            creer_case_vide(xj + 2 * DISTANCE_ENTRE_CASE, yj),
                            creer_caisse(xj + DISTANCE_ENTRE_CASE, yj), caisses, murs, joueur, can,
                            xj + 2 * DISTANCE_ENTRE_CASE, yj, xj + DISTANCE_ENTRE_CASE, yj, liste_image)
    elif direction == 'gauche':
        effectuer_mouvement(creer_case_vide(xj - DISTANCE_ENTRE_CASE, yj),
                            creer_case_vide(xj - 2 * DISTANCE_ENTRE_CASE, yj),
                            creer_caisse(xj - DISTANCE_ENTRE_CASE, yj), caisses, murs, joueur, can,
                            xj - 2 * DISTANCE_ENTRE_CASE, yj, xj - DISTANCE_ENTRE_CASE, yj, liste_image)
    elif direction == 'haut':
        effectuer_mouvement(creer_case_vide(xj, yj - DISTANCE_ENTRE_CASE),
                            creer_case_vide(xj, yj - 2 * DISTANCE_ENTRE_CASE),
                            creer_caisse(xj, yj - DISTANCE_ENTRE_CASE), caisses, murs, joueur, can,
                            xj, yj - 2 * DISTANCE_ENTRE_CASE, xj, yj - DISTANCE_ENTRE_CASE, liste_image)
    elif direction == 'bas':
        effectuer_mouvement(creer_case_vide(xj, yj + DISTANCE_ENTRE_CASE),
                            creer_case_vide(xj, yj + 2 * DISTANCE_ENTRE_CASE),
                            creer_caisse(xj, yj + DISTANCE_ENTRE_CASE), caisses, murs, joueur, can,
                            xj, yj + 2 * DISTANCE_ENTRE_CASE, xj, yj + DISTANCE_ENTRE_CASE, liste_image)


def effectuer_mouvement(coordonnee_destination, coordonnee_case_suivante, ancienne_caisse, caisses: list, murs: list, joueur: list, can,
                        deplace_caisse_x, deplace_caisse_y, deplace_joueur_x, deplace_joueur_y, liste_image: list):
    """
    Fonction permettant d'effectuer le déplacement ou de ne pas l'effectuer si celui-ci n'est pas possible. Voir énoncé
    "Quelques règles". Cette methode est appelée par mouvement.
    :param coordonnee_destination: variable CaseVide ayant possiblement des coordonnées identiques à une autre variable
    (murs, caisse, casevide)
    :param coordonnee_case_suivante: variable CaseVide ayant possiblement des coordonnées identiques à une autre variable
    (murs, caisse, casevide) mais représente la case après coordonnee_destination
    :param ancienne_caisse: variable utile pour supprimer l'ancienne caisse (après avoir déplacé celle-ci)
    :param caisses: liste des caisses
    :param murs: liste des murs
    :param joueur: liste des joueurs
    :param can: Canvas (ignorez son fonctionnement), utile uniquement pour créer_image()
    :param deplace_caisse_x: coordonnée à laquelle la caisse va être déplacée en x (si le joueur pousse une caisse)
    :param deplace_caisse_y: coordonnée à laquelle la caisse va être déplacée en y (si le joueur pousse une caisse)
    :param deplace_joueur_x: coordonnée en x à laquelle le joueur va être après le mouvement
    :param deplace_joueur_y: coordonnée en y à laquelle le joueur va être après le mouvement
    :param liste_image: liste des images (murs, caisses etc...) détaillée dans l'énoncé
    :return:
    """
    # Ne rien faire si un des paramètres est None
    if None in (caisses, murs, joueur, can, deplace_caisse_x, deplace_caisse_y, deplace_joueur_x, deplace_joueur_y, liste_image):
        return None

    # Déclaration de booléens permettant de savoir si un mur ou une caisse se trouve sur la case de destination ou sur la case suivante
    est_mur_des: bool = False
    est_mur_sui: bool = False
    est_caisse_des: bool = False
    est_caisse_sui: bool = False

    # S'il y a un mur sur la case de destination, mettre la variable est_mur_des à Vrai
    for mur in murs:
        if est_egal_a(mur, coordonnee_destination):
            est_mur_des = True
            break

    # S'il y a un mur sur la case suivante, mettre la variable est_mur_sui à Vrai
    for mur in murs:
        if est_egal_a(mur, coordonnee_case_suivante):
            est_mur_sui = True
            break

    # S'il y a une caisse sur la case de destination, mettre la variable est_caisse_des à Vrai
    for caisse in caisses:
        if est_egal_a(caisse, coordonnee_destination):
            est_caisse_des = True
            break

    # S'il y a une caisse sur la case suivante, mettre la variable est_caisse_sui à Vrai
    for caisse in caisses:
        if est_egal_a(caisse, coordonnee_case_suivante):
            est_caisse_sui = True
            break

    # S'il n'y a pas de mur sur la case de destination, et s'il n'y a pas deux caisses ou une caisse et un mur en face du joueur, alors effectuer le mouvement
    if not est_mur_des:
        if not (est_caisse_des and est_caisse_sui):
            if not (est_caisse_des and est_mur_sui):
                # S'il y a une caisse à la destination
                if est_caisse_des:
                    # Créer une image vide la où se trouvait le joueur avant le déplacement, et mise à jour de la liste "joueur"
                    creer_image(can, coordonnee_x(joueur[0]), coordonnee_y(joueur[0]), liste_image[6])
                    joueur[0] = creer_personnage(deplace_joueur_x, deplace_joueur_y)

                    # Créer une image vide la où se trouvait la caisse avant le déplacement, et mise à jour de la liste "caisse"
                    creer_image(can, coordonnee_x(ancienne_caisse), coordonnee_y(ancienne_caisse), liste_image[6])
                    caisses.remove(ancienne_caisse)
                    caisses.append(creer_caisse(deplace_caisse_x, deplace_caisse_y))

                # Cas où le joueur se déplace sans objet à la desination
                else:
                    # Créer une image vide la où se trouvait le joueur avant le déplacement, et mise à jour de la liste "joueur"
                    creer_image(can, coordonnee_x(joueur[0]), coordonnee_y(joueur[0]), liste_image[6])
                    joueur[0] = creer_personnage(deplace_joueur_x, deplace_joueur_y)


def chargement_score(scores_file_path: str, dict_scores: dict):
    """
    Fonction chargeant les scores depuis un fichier.txt et les stockent dans un dictionnaire
    :param scores_file_path: le chemin d'accès du fichier
    :param dict_scores:  le dictionnaire pour le stockage
    :return:
    """
    # Si le chemin "scores_file_path" n'est pas un fichier, ne rien faire
    if not os.path.isfile(scores_file_path) or dict_scores is None:
        return None

    # Déclaration de variables locales
    ligne: str = None
    score: str = ""
    liste_scores: list = []

    # Lecture du fichier des scores : insertion de chaque score dans une liste de score.
    with open(scores_file_path, 'r') as filin:
        while ligne != '':
            ligne = filin.readline().replace('\n', '')
            # Pour chaque ligne, si le caractère n'est pas ";", ajouter le caractère en cours dans la variable "score"
            if ligne != '':
                for i in ligne[2:]:
                    if i != ";":
                        score += i

                    # Si le caractère en cours de lecture est ";", ajouter le contenu de la variable score à la liste des scores
                    else:
                        liste_scores.append(int(score))
                        score = ""
                dict_scores[int(ligne[0])] = sorted(liste_scores, reverse=True)
                liste_scores = []


def maj_score(niveau_en_cours: str, dict_scores: dict) -> str:
    """
    Fonction mettant à jour l'affichage des scores en stockant dans un str l'affichage visible
    sur la droite du jeu.
    ("Niveau x
      1) 7699
      2) ... ").
    :param niveau_en_cours: le numéro du niveau en cours
    :param dict_scores: le dictionnaire pour stockant les scores
    :return str: Le str contenant l'affichage pour les scores ("\n" pour passer à la ligne)
    """
    # Ne rien faire si un des paramètres est None
    if niveau_en_cours is None or dict_scores is None:
        return None

    # Déclaration de variables locales permettant d'afficher le score sur l'écran de droite
    affichage_score: str = ""
    i: int = 1

    # Affiche le niveau en cours
    affichage_score += "Niveau " + niveau_en_cours + "\n"

    # Affiche tous les scores présents dans le dictionnaire dict_scores au niveau en cours.
    for val in dict_scores[int(niveau_en_cours)]:
        affichage_score += str(i) + ") " + str(val) + "\n"
        i += 1

    # Retourne la str à afficher sur l'écran de droite
    return affichage_score


def enregistre_score(temps_initial: float, nb_coups: int, score_base: int, dict_scores: dict, niveau_en_cours: str) -> int:
    """
    Fonction enregistrant un nouveau score réalisé par le joueur. Le calcul de score est le suivant :
    score_base - (temps actuel - temps initial) - (nombre de coups * valeur d'un coup)
    Ce score est arrondi sans virgule et stocké en tant que int.
    :param temps_initial: le temps initial
    :param nb_coups: le nombre de coups que l'utilisateurs à fait (les mouvements)
    :param score_base: Le score de base identique pour chaque partie
    :param dict_scores: Le dictionnaire stockant les scores
    :param niveau_en_cours: Le numéro du niveau en cours
    :return: le score sous forme d'un int
    """
    # Ne rien faire si un des paramètres est None
    if None in (temps_initial, nb_coups, score_base, dict_scores, niveau_en_cours):
        return None

    # Calcul du nouveau score
    nv_score: int = int(round(score_base - (time.time() - temps_initial) - (nb_coups * VALEUR_COUP), 0))
    liste_score: list = dict_scores[int(niveau_en_cours)]

    # Insère le nouveau score dans le dictionnaire des scores, au bon niveau, et au bon endroit, sans écraser les scores existants. Conserve un maximum de 10 scores dans la liste.
    for i in range(len(liste_score)):
        if liste_score[i] <= nv_score:
            liste_score.insert(i, nv_score)
            liste_score.pop(len(liste_score) - 1)
            break

    return nv_score


def update_score_file(scores_file_path: str, dict_scores: dict):
    """
    Fonction sauvegardant tous les scores dans le fichier.txt.
    :param scores_file_path: le chemin d'accès du fichier de stockage des scores
    :param dict_scores: Le dictionnaire stockant les scores
    :return:
    """
    # Si le chemin "scores_file_path" n'est pas un fichier ou si le dictionnaire des scores est à None, ne rien faire
    if not os.path.isfile(scores_file_path) or dict_scores is None:
        return None

    # Inscrit tous les scores du dictionnaires "dict_scores" dans le fichier donné, au format "1;XXXX;XXXY;..." (cf. énoncé)
    with open(scores_file_path, "w") as filout:
        for cle, val in dict_scores.items():
            filout.write(str(cle) + ";")
            for i in val:
                filout.write(str(i) + ";")
            filout.write("\n")


# Constantes à utiliser
DISTANCE_ENTRE_CASE = 32  # distance par rapport à l'autre case
VALEUR_COUP = 50
X_PREMIERE_CASE = 20
Y_PREMIERE_CASE = 20

# Ne pas modifier !
if __name__ == '__main__':
    os.system("fourni\simulateur.py")
