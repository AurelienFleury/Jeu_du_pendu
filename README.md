## Auteur

Ce jeu du pendu a été développé par Aurelien Fleury.

## Date

Ce code a été créé le 17/05/2023.

# Jeu du Pendu

Ce projet est une implémentation du jeu du pendu en Python. Le jeu sélectionne aléatoirement un mot à partir d'un fichier contenant une liste de mots. Le joueur doit deviner le mot en proposant des lettres. Le joueur a un certain nombre de chances (ici 6) pour deviner correctement le mot. Si le joueur parvient à deviner toutes les lettres du mot avant d'épuiser ses chances, il gagne ; sinon, il perd.

## Contenu du Code

Le code source est composé des éléments suivants :

- 'choisir_mot()' : Cette fonction permet de sélectionner un mot aléatoire à partir du fichier de liste de mots : 'mots_pendu.txt'.

- 'afficher_etat(mot, lettres_devinees)' : Cette fonction affiche l'état actuel du mot recherché, en utilisant des "_" pour les lettres non devinées.

- 'jouer_pendu()' : Cette fonction permet de jouer au jeu du pendu. Elle gère les interactions avec le joueur, en lui demandant de deviner des lettres et en vérifiant si elles font partie du mot recherché et si les lettres proposées par le joueur n'ont pas déjà été prposées.

## Utilisation

1. Assurez-vous d'avoir un fichier 'mots_pendu.txt' contenant une liste de mots, un mot par ligne. Mettez-le dans le même dossier que le fichier contenant le code python.

2. Exécutez le script Python 'main.py'.

3. Suivez les instructions pour deviner les lettres du mot. Entrez une lettre à chaque tour.

4. Vous disposez de 6 chances pour deviner le mot. Si vous devinez correctement toutes les lettres du mot, vous gagnez ; sinon, vous perdez.
