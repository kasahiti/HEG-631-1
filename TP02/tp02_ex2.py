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
CODE_PROMO: str = "#POU"

choix_utilisateur: str = None
no_produit: int = None
monnaie: float = None
reste_payer: float = None
saisie: str = None
no_produit: int = None
rabais: float = None
text_final: str = None

# Initialisation des variables
monnaie_rendu = 0
rabais = 1.0

# Séquence d'opération
print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

# Poser la question tant que la saisie n'est pas valide
while saisie is None:
    saisie = input("Veuillez sélectionner un produit et votre offre promotionnelle :")
    no_produit = int(saisie.split()[0])
    if no_produit < 1 or no_produit > 6:
        saisie = None
        print("Le produit sélectionné n'existe pas")

# Regarde si l'utilisateur a saisi un code promo et adapte le rabais en conséquence
if len(saisie) > 1:
    if saisie.split()[1] == CODE_PROMO:
        rabais = 0.8

# Calcule le prix à payer en fonction du choix de l'utilisateur, et prépare le text final ("*** servis !")
if no_produit == 1:
    reste_payer = round(PRIX_SANDWICH_POULET * rabais, 2)
    text_final = "Sandwich au poulet servi ! Bon appétit !"

elif no_produit == 2:
    reste_payer = round(PRIX_CHIPS_PAPRIKA * rabais, 2)
    text_final = "Chips Paprika servies ! Bon appétit !"

elif no_produit == 3:
    reste_payer = round(PRIX_BARRE_CHOCOLAT * rabais, 2)
    text_final = "Barre chocolatée serive ! Bon appétit !"

elif no_produit == 4:
    reste_payer = round(PRIX_BONBONS * rabais, 2)
    text_final = "Bonbons servis ! Bon appétit !"

elif no_produit == 5:
    reste_payer = round(PRIX_ICE_TEA * rabais, 2)
    text_final = "Ice Tea servi ! Santé !"
else:
    reste_payer = round(PRIX_LIMONADE * rabais, 2)
    text_final = "Limonade servie ! Santé !"

print("Le prix à payer est de :", reste_payer)

# Tant que l'utilisateur n'as pas entièrement payé son produit, lui demander la somme restante
while reste_payer is None or reste_payer > 0:
    monnaie = float(input("Veuillez introduire votre monnaie :"))
    reste_payer = round(reste_payer - monnaie, 2)

    if reste_payer > 0:
        print("Le montant est insuffisant. Veuillez ajouter encore :", reste_payer)
    if reste_payer <= 0:
        monnaie_rendu = round(-reste_payer, 2)

# En fonction du choix de l'utilisateur, affiche le text final et la monnaie à rendre
print(text_final)
print("Monnaie à rendre :", monnaie_rendu)
