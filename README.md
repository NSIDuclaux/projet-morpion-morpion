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

Le fichier principal `morpion_fini.py` contient trois classes principales :

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

1. Exécutez le fichier `morpion_fini.py`.
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
   git clone https://github.com/NSIDuclaux/projet-morpion-morpion.git
   ```
2. Naviguez vers le dossier du projet :
   ```bash
   cd projet-morpion-morpion
   ```
3. Exécutez le jeu :
   ```bash
   python morpion_fini.py
   ```

Amusez-vous bien en jouant au Morpion !

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vv7AS4H3)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17684549)
