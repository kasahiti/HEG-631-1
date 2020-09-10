"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
# Déclaration des variables
PRIX_BILLET: int = 10
RABAIS_ETUDIANT: int = 2
RABAIS_MEMBRE: int = 3
RABAIS_FAMILLE: int = 1

carte_mensuelle: str
carte_membre: str
carte_etudiante: str
forfait_famille: str

prix: int

# Initialisation des variables
carte_membre = "non"
carte_mensuelle = "non"
carte_etudiante = "non"
forfait_famille = "non"

# Demande à l'utilisateur ses informations
carte_mensuelle = input("Possédez-vous la carte mensuelle ? (oui ou non)")
if carte_mensuelle == "oui":
    print("Le prix a payer est : 0CHF")
else:
    carte_membre = input("Possédez-vous la carte membre ? (oui ou non)")
    carte_etudiante = input("Possédez-vous la carte étudiante ? (oui ou non)")
    forfait_famille = input("Bénéficiez-vous du forfait famille ? (oui ou non)")

# Séquence d'opération
# Les indications spéciales / combinaisons sont traduites sur ce premier if et les deux elif suivants
if (carte_membre == "oui" and carte_etudiante == "oui" and forfait_famille == "oui") or (carte_membre == "oui" and carte_etudiante == "oui"):
    # Si l'utilisateur possède tous les rabais, ne prendre en compte que le rabais membre et étudiant
    prix = PRIX_BILLET - RABAIS_MEMBRE - RABAIS_ETUDIANT
    print("Le prix à payer est : {}CHF".format(prix))

elif carte_membre == "oui" and forfait_famille == "oui":
    prix = PRIX_BILLET - RABAIS_MEMBRE - RABAIS_FAMILLE
    print("Le prix à payer est : {}CHF".format(prix))

elif carte_etudiante == "oui" and forfait_famille == "oui":
    print("Il n'est pas possible de bénéficier des ces rabais en même temps.")

# Pour tous les autres cas, où l'utilisateur ne possède qu'une carte :
elif carte_membre == "oui":
    prix = PRIX_BILLET - RABAIS_MEMBRE
    print("Le prix à payer est : {}CHF".format(prix))

elif carte_etudiante == "oui":
    prix = PRIX_BILLET - RABAIS_ETUDIANT
    print("Le prix à payer est : {}CHF".format(prix))

elif forfait_famille == "oui":
    prix = PRIX_BILLET - RABAIS_FAMILLE
    print("Le prix à payer est : {}CHF".format(prix))
