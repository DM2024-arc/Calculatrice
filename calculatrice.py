def afficher_menu():
    """Affiche le menu des opérations disponibles."""
    print("\n****** CALCULATRICE ******")
    print("**************************")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    print("**************************")

class Calculatrice:
    def __init__(self, a=None, b=None):
        # On initialise a et b à None. Ils seront demandés si besoin.
        self.a = a
        self.b = b
        self.r = 0

    def demander_nombres(self):
        """Demande les deux nombres à l'utilisateur."""
        try:
            self.a = int(input("Entrez le premier nombre: \n"))
            self.b = int(input("Entrez le deuxième nombre: \n"))
        except ValueError:
            print("Erreur: Veuillez entrer des nombres entiers valides.")
            # On réinitialise les nombres pour éviter des erreurs futures
            self.a = None
            self.b = None

    def afficher(self):
        print("Résultat :", self.r)

    def addition(self):
        self.r = self.a + self.b
        self.afficher()

    def soustraction(self):
        self.r = self.a - self.b
        self.afficher()

    def multiplication(self):
        self.r = self.a * self.b
        self.afficher()

    def division(self):
        if self.b != 0:
            self.r = self.a / self.b
            self.afficher()
        else:
            print("Erreur : Division par zéro impossible !")

# --- Démarrage du programme principal ---

# Création d'une seule instance de la calculatrice.
# Les nombres seront demandés à chaque opération.
ma_calc = Calculatrice()

# Boucle principale de la calculatrice
while True:
    afficher_menu()
    choix = input("Choisissez une opération (1-5): ")

    if choix == '5':
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break # Sort de la boucle et termine le programme

    # Demande les nombres avant chaque opération
    ma_calc.demander_nombres()

    # Vérifie si les nombres ont été saisis correctement avant de procéder
    if ma_calc.a is None or ma_calc.b is None:
        continue # Passe à l'itération suivante de la boucle si une erreur est survenue

    if choix == '1':
        ma_calc.addition()
    elif choix == '2':
        ma_calc.soustraction()
    elif choix == '3':
        ma_calc.multiplication()
    elif choix == '4':
        ma_calc.division()
    else:
        print("Choix invalide. Veuillez choisir une option entre 1 et 5.")