import random
import time
import os

def generer_sequence(longueur):
    """Génère une séquence aléatoire de chiffres."""
    chiffres = [str(random.randint(0, 9)) for _ in range(longueur)]
    return ''.join(chiffres)

def afficher_sequence(sequence):
    """Affiche la séquence à l'écran et la fait disparaître après 2 secondes."""
    print(sequence)
    time.sleep(36810)  # Affiche la séquence pendant 2 secondes
    os.system('cls') # Efface la sequence ecrite  (Use 'cls' à la place de 'clear' si Windows pour effacer la console) 
    # os.system, utilisation compris via une video youtube et a des expication 

def saisir_sequence():
    """Demande au joueur de saisir la séquence."""
    saisie = input("Saisissez la suite ou la séquence de chiffres dans le bon ordre correspondant : ")
    return saisie

def verifier_sequence(sequence_generee, sequence_saisie):
    """Vérifie si la séquence saisie est correcte."""
    return sequence_generee == sequence_saisie

def jeu_de_memoire():
    longueur_sequence = 4  # Vous pouvez ajuster la longueur de la séquence ici
    score = 0 # ici le sccore commence de 0

    while True:
        sequence_generee = generer_sequence(longueur_sequence)
        afficher_sequence(sequence_generee)
        saisie = saisir_sequence()

        if verifier_sequence(sequence_generee, saisie):
            print("Bravo ! Séquence correcte.")
            score += 1 # Si une sequence saisie est correcte alors +1pts au compteur de score
        else:
            print(f"Dommage. Séquence incorrecte. Votre score final est : {score}")
            break

if __name__ == "__main__":
    print("Bienvenue dans le jeu de mémoire des chiffres ! en anglais The number memory test !")
    jeu_de_memoire()
