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
    """
    Une classe simple pour effectuer des opérations arithmétiques de base.
    """
    def __init__(self):
        """
        Initialise une nouvelle instance de Calculatrice.
        Les nombres sur lesquels opérer ne sont pas stockés en permanence
        dans l'objet, mais demandés au besoin pour chaque opération.
        Le résultat de la dernière opération est stocké dans 'resultat'.
        """
        self.resultat = 0

    def _obtenir_nombres(self):
        """
        Méthode interne (privée) pour obtenir deux nombres entiers de l'utilisateur.
        Utilise un underscore préfixe pour indiquer qu'elle est destinée à un usage interne.
        """
        while True:
            try:
                num1 = float(input("Entrez le premier nombre: "))
                num2 = float(input("Entrez le deuxième nombre: "))
                return num1, num2
            except ValueError:
                print("Erreur: Veuillez entrer des nombres valides (entiers ou décimaux).")

    def addition(self):
        """Effectue une addition et affiche le résultat."""
        num1, num2 = self._obtenir_nombres()
        self.resultat = num1 + num2
        self._afficher_resultat("Addition")

    def soustraction(self):
        """Effectue une soustraction et affiche le résultat."""
        num1, num2 = self._obtenir_nombres()
        self.resultat = num1 - num2
        self._afficher_resultat("Soustraction")

    def multiplication(self):
        """Effectue une multiplication et affiche le résultat."""
        num1, num2 = self._obtenir_nombres()
        self.resultat = num1 * num2
        self._afficher_resultat("Multiplication")

    def division(self):
        """Effectue une division et affiche le résultat, gérant la division par zéro."""
        num1, num2 = self._obtenir_nombres()
        if num2 != 0:
            self.resultat = num1 / num2
            self._afficher_resultat("Division")
        else:
            print("Erreur: Division par zéro impossible !")

    def _afficher_resultat(self, operation):
        """
        Méthode interne pour afficher le résultat de l'opération.
        """
        print(f"Résultat de l'{operation}: {self.resultat}")

# --- Démarrage du programme principal ---

if __name__ == "__main__": # Cette ligne assure que le code s'exécute seulement si le script est lancé directement
    ma_calc = Calculatrice() # Création d'une seule instance de la calculatrice.

    # Dictionnaire pour mapper les choix aux méthodes de la calculatrice
    operations = {
        '1': ma_calc.addition,
        '2': ma_calc.soustraction,
        '3': ma_calc.multiplication,
        '4': ma_calc.division
    }

    while True:
        afficher_menu()
        choix = input("Choisissez une opération (1-5): ")

        if choix == '5':
            print("Merci d'avoir utilisé la calculatrice. Au revoir!")
            break
        elif choix in operations:
            operations[choix]() # Appelle la méthode correspondante
        else:
            print("Choix invalide. Veuillez choisir une option entre 1 et 5.")