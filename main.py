# main.py
from calculatrice import Calculatrice
from entete import Entete

if __name__ == "__main__":
    ma_calc = Calculatrice()

    operations = {
        '1': ma_calc.addition,
        '2': ma_calc.soustraction,
        '3': ma_calc.multiplication,
        '4': ma_calc.division
    }

    while True:
        Entete.afficher_menu()
        choix = input("Choisissez une opération (1-5): ")

        if choix == '5':
            print("Merci d'avoir utilisé la calculatrice. Au revoir!")
            break
        elif choix in operations:
            operations[choix]()
        else:
            print("Choix invalide. Veuillez choisir une option entre 1 et 5.")
