"""
Programme testant si une année, saisie par l'utilisateur,est bissextile ou non
  Données : Une année saisie par l'utilisateur
  Indications:
        - Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        - Si elle est multiple de 4, on regarde si elle est multiple de 100.
          - Si c'est le cas, on regarde si elle est multiple de 400.
            - Si c'est le cas, l'année est bissextile.
            - Sinon, elle n'est pas bissextile.
          - Sinon, elle est bissextile.
  Résultats : Un message spécifiant si l'année entrée est bissextile ou non
"""

# Déclaration des variables
annee: int

# Initialisation des variables
annee = int(input("Saisissez une année : "))

# Séquence d'opération
# Si l'année n'est pas un multiple de 4, elle n'est pas bissextile
if annee % 4 != 0:
    print("L'année saisie n'est pas bissextile.")

# Sinon si l'année est multiple de 4 et de 100, on regarde si elle est multiple de 400
elif annee % 4 == 0 and annee % 100 == 0:
    if annee % 400 == 0:
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
else:
    print("L'année saisie est bissextile.")
