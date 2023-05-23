#Auteur : Aurelien Fleury
#Date : 17/05/2023
#Titre : Jeu du pendu
import random

#Focntion permettant de sélectionner un mot aléatoire à partir du fichier mots_pendu
def choisir_mot():
    #Ouverture en tant que lecture du fichier mots_pendu
    with open("mots_pendu.txt", "r") as fichier:
        #Création d'une liste contenant tous les mots du fichier mots_pendu
        liste_mots = fichier.readlines()
    #Choix aléatoire d'un mot
    mot = random.choice(liste_mots)
    #Supprime le dernier caractère du mot qui est surement un espace ou un retour à la ligne
    mot = mot[:-1]
    return mot

#Focntion permettant d'afficher l'état actuel du mot recherché en utilisant des _ pour les lettres non devinées
def afficher_etat(mot, lettres_devinees):
    #Création d'une chaîne de caractère vide qui va nous servir à afficher l'état du mot recherché
    affichage = ""
    #Permet de mettre la lettre si elle fait partie du mot recherché
    for lettre in mot:
        if lettre in lettres_devinees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    print(affichage)

#Fonction permettant de jouer au jeu du pendu
def jouer_pendu():
    #Chois du mot aléatoire à l'aide de la fonction créée
    mot = choisir_mot()
    #Chaîne de caractère contenant les lettres devinées par le joueur
    lettres_devinees =''
    #Initialisation du nombre de chances à 6
    chances_restantes = 6
    #Chaîne de caractère contenant les lettres du mot à deviner. Utilisation du 'set' afin de ne pas avoir de lettre en doublon
    lettres_a_deviner = set(mot)
    #Utilisation de la fonction afin de montrer l'état du mot au début de la partie
    afficher_etat(mot, lettres_devinees)

    #Boucle tant que, permettant au joueur de jouer tant qu'il lui reste encore au moins une chance
    while chances_restantes > 0:
        print("Chances restantes : ", chances_restantes)
        #Demander au joueur d'entrer la lettre qu'il souhaite jouer
        lettre = input("Entrez une lettre que vous pensez être dans le mot : ")
        #Permet de recommencer la boucle si la lettre jouée à déjà été joué par l'utilisateur
        if lettre in lettres_devinees:
            print('Vous avez déjà essayé cette lettre.')
            continue
        #Ajout de la lettre joué à la liste
        lettres_devinees += lettre

        if lettre in mot:
            #Affiche que la lettre est dans le mot recherché
            print("Bravo, la lettre fait partie du mot")
            #Enlève la lettre de la liste des lettres à deviner
            lettres_a_deviner.remove(lettre)
        else:
            #Si la lettre ne fait pas partie du mot on l'affiche à l'utilisateur et cela enlève une chance aux chances restantes
            print("Dommage, la lettre ne fait pas partie du mot.")
            chances_restantes -= 1
        #Permet d'afficher l'état du mot recherché
        afficher_etat(mot, lettres_devinees)
        #S'il ne reste aucune lettre dans la liste des lettre à deviner alors le joueur à gagné, il a trouvé le mot
        if not lettres_a_deviner:
            print("Félicitations, vous avez gagné ! Le mot était :", mot)
            return
    #Une fois toutes les chances écoulées, le joueur a perdu, on affiche alors le mot qu'il devait trouver
    print("Vous avez perdu! Le mot était : ", mot)

#Exécution du jeu du pendu
jouer_pendu()