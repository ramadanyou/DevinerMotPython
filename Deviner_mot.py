import random

# Liste de mots possibles
mots = ['python', 'ordinateur', 'programmation', 'algorithmique', 'developpement']

def choisir_mot():
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ''
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += '_'
    return mot_cache

def deviner_lettre():
    lettre = input("Devinez une lettre : ").lower()
    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre.")
        return deviner_lettre()
    return lettre

def jouer_au_canari():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    tentatives_restantes = 6

    print("Bienvenue au jeu du Canari !")
    print("Le mot à deviner comporte", len(mot_a_deviner), "lettres.")

    while tentatives_restantes > 0:
        mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print("\nMot à deviner :", mot_cache)
        print("Tentatives restantes :", tentatives_restantes)

        lettre = deviner_lettre()

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
        elif lettre in mot_a_deviner:
            print("Bravo ! La lettre", lettre, "est dans le mot.")
            lettres_trouvees.add(lettre)
            if afficher_mot_cache(mot_a_deviner, lettres_trouvees) == mot_a_deviner:
                print("Félicitations, vous avez deviné le mot", mot_a_deviner, "!")
                break
        else:
            print("Dommage, la lettre", lettre, "n'est pas dans le mot.")
            tentatives_restantes -= 1

    if tentatives_restantes == 0:
        print("Vous avez épuisé toutes vos tentatives. Le mot était", mot_a_deviner)

# Appel de la fonction principale pour jouer
jouer_au_canari()
