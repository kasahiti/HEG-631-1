"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

# Déclaration des variables
PRIX_SANDWICH_POULET: float = 4.90
PRIX_CHIPS_PAPRIKA: float = 2.50
PRIX_BARRE_CHOCOLAT: float = 2.00
PRIX_BONBONS: float = 3.30
PRIX_ICE_TEA: float = 2.20
PRIX_LIMONADE: float = 1.90

monnaie: float
no_produit: int
monnaie_rendu: float

# Initialisation des variables
monnaie_rendu = 0

# Séquence d'opération
print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

# Demande à l'utilisateur d'introduire sa monnaie et de sélectionner un produit
monnaie = float(input("Veuillez introduire votre monnaie :"))
no_produit = int(input("Veuillez sélectionner un produit :"))

# En fonction du choix de l'utilisateur, on calcule la monnaie rendue et affiche à l'écran la monnaie à rendre.
if no_produit == 1:
    monnaie_rendu = monnaie - PRIX_SANDWICH_POULET
    print("Monnaie à rendre :", round(monnaie_rendu, 2), "\nSandwich au poulet servi ! Bon appétit !)")
elif no_produit == 2:
    monnaie_rendu = monnaie - PRIX_CHIPS_PAPRIKA
    print("Monnaie à rendre :", round(monnaie_rendu, 2), "\nChips Paprika servies ! Bon appétit !")
elif no_produit == 3:
    monnaie_rendu = monnaie - PRIX_BARRE_CHOCOLAT
    print("Monnaie à rendre :", round(monnaie_rendu, 2), "\nBarre chocolatée serive ! Bon appétit !")
elif no_produit == 4:
    monnaie_rendu = monnaie - PRIX_BONBONS
    print("Monnaie à rendre :", round(monnaie_rendu, 2), "\nBonbons servis ! Bon appétit !")
elif no_produit == 5:
    monnaie_rendu = monnaie - PRIX_ICE_TEA
    print("Monnaie à rendre :", round(monnaie_rendu, 2), "\nIce Tea servi ! Santé !")
else:
    monnaie_rendu = monnaie - PRIX_LIMONADE
    print("Monnaie à rendre :", round(monnaie_rendu, 2), "\nLimonade servie ! Santé !")
