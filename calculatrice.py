from dataclasses import dataclass

@dataclass
class Operation:
    num1: float
    num2: float
    resultat: float = 0.0

class Calculatrice:
    """
    Une calculatrice simple utilisant une dataclass pour stocker les données de l'opération.
    """

    def _obtenir_operation(self) -> Operation:
        while True:
            try:
                num1 = float(input("Entrez le premier nombre: "))
                num2 = float(input("Entrez le deuxième nombre: "))
                return Operation(num1=num1, num2=num2)
            except ValueError:
                print("Erreur : Veuillez entrer des nombres valides.")

    def addition(self):
        operation = self._obtenir_operation()
        operation.resultat = operation.num1 + operation.num2
        self._afficher_resultat("Addition", operation)

    def soustraction(self):
        operation = self._obtenir_operation()
        operation.resultat = operation.num1 - operation.num2
        self._afficher_resultat("Soustraction", operation)

    def multiplication(self):
        operation = self._obtenir_operation()
        operation.resultat = operation.num1 * operation.num2
        self._afficher_resultat("Multiplication", operation)

    def division(self):
        operation = self._obtenir_operation()
        if operation.num2 != 0:
            operation.resultat = operation.num1 / operation.num2
            self._afficher_resultat("Division", operation)
        else:
            print("Erreur : Division par zéro impossible !")

    def _afficher_resultat(self, operation_nom: str, operation: Operation):
        print(f"Résultat de l'{operation_nom} : {operation.resultat}")
