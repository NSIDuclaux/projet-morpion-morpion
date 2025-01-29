# Morpion (Tic-Tac-Toe) avec Interface Tkinter et IA

Ce projet implémente le jeu classique du Morpion (Tic-Tac-Toe) avec une interface graphique utilisant Tkinter et différents niveaux d'IA.

## Caractéristiques principales

- Interface graphique conviviale avec Tkinter
- Plusieurs modes de jeu :
  - Joueur contre IA aléatoire
  - Joueur contre IA défensive
  - Joueur contre IA défensive et offensive
- Possibilité de rejouer et de changer de mode de jeu

## Structure du code

Le fichier principal `morpion_tkinter_vs_IA.py` contient trois classes principales :

1. `Morpion_1vPCalea` : Implémente le jeu contre une IA aléatoire.
2. `Morpion_1vPCdef` : Implémente le jeu contre une IA défensive.
3. `Morpion_1vPCdef_et_off` : Implémente le jeu contre une IA défensive et offensive.

### Fonctionnalités clés

- `sur_bouton_clique` : Gère les clics des joueurs sur la grille.
- `ordinateur_alea`, `ordinateur_defensif`, `ordinateur_defensif_et_offensif` : Implémentent différentes stratégies pour l'IA.
- `a_gagne` : Vérifie si un joueur a gagné.
- `jeu_nul` : Vérifie si la partie est nulle.
- `reinitialiser_jeu` : Permet de recommencer une nouvelle partie.

## Comment jouer

1. Exécutez le fichier `morpion_tkinter_vs_IA.py`.
2. Choisissez votre mode de jeu.
3. Cliquez sur les cases pour placer vos symboles.
4. L'IA jouera automatiquement après votre tour.
5. Le jeu annoncera le gagnant ou un match nul.
6. Vous pouvez rejouer ou changer de mode de jeu à la fin de chaque partie.

## Dépendances

- Python 3.x
- Tkinter (généralement inclus avec Python)

## Installation et exécution

1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre-username/votre-repo-morpion.git
   ```
2. Naviguez vers le dossier du projet :
   ```bash
   cd votre-repo-morpion
   ```
3. Exécutez le jeu :
   ```bash
   python morpion_tkinter_vs_IA.py
   ```

# Projet Morpion

Bienvenue sur le dépôt GitHub pour le projet de morpion ! Ce projet a pour but de créer une implémentation de jeu de morpion en Python. Il comprend deux versions : une interface graphique avec `morpion_fini.py` et une version en ligne de commande avec `morpion_terminal.py`.

## Description du projet

Le fichier `morpion_fini.py` contient l'implémentation complète du jeu de morpion avec une interface graphique. Le jeu prend en charge deux modes de jeu : un joueur contre un autre joueur sur le même ordinateur et un joueur contre une intelligence artificielle.

Le fichier `morpion_terminal.py` fournit une version en ligne de commande du jeu de morpion pour deux joueurs humains.

Les fonctionnalités incluses dans le projet sont les suivantes :

- Choix du mode de jeu (1 joueur contre 1 joueur ou 1 joueur contre l'IA)
- Affichage du plateau de jeu avec des cases cliquables (pour `morpion_fini.py`) ou en texte (pour `morpion_terminal.py`)
- Détermination du gagnant après chaque coup
- Détection de la fin de la partie (match nul ou joueur gagnant)
- Possibilité de recommencer une partie

## Comment exécuter le programme

1. Téléchargez les fichiers `morpion_fini.py` et `morpion_terminal.py` sur votre ordinateur.
2. Ouvrez un terminal ou une invite de commande et accédez au répertoire où vous avez téléchargé les fichiers.
3. Exécutez la commande suivante pour lancer le programme :
   - Pour `morpion_fini.py` : `python morpion_fini.py`
   - Pour `morpion_terminal.py` : `python morpion_terminal.py`

Amusez-vous bien en jouant au Morpion !

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vv7AS4H3)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17684549)
