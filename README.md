# pygameAnimation
interactive animation in python
Initialisation :
Le programme commence par importer les modules nécessaires (pygame, pygame_gui, sys, math, random) et initialiser la bibliothèque Pygame avec pygame.init().
Il initialise la fenêtre d'affichage (screen) avec une taille de 1000x900 pixels.
Une horloge (clock) est créée pour contrôler le taux de rafraîchissement de la fenêtre.
Un gestionnaire d'interface utilisateur (manager) est créé pour gérer les éléments d'interface utilisateur.
Initialisation des variables :
Diverses variables sont initialisées pour contrôler le comportement du programme, telles que j, timmm, tres, rotation, nombreDeCercles, etc.
Des variables sont également définies pour stocker les valeurs des curseurs et des boutons, qui sont utilisés pour ajuster les paramètres du dessin.
Initialisation des boutons et curseurs :
Plusieurs boutons et curseurs d'interface utilisateur sont créés à l'aide de la bibliothèque Pygame GUI (UIButton, UIHorizontalSlider, UILabel).
Les boutons ont des emplacements relatifs et des textes correspondant à leurs fonctions.
Les curseurs sont associés à des valeurs minimales, maximales et initiales, et sont également placés à des emplacements relatifs dans la fenêtre.
Boucle principale (Main Loop) :
Le programme entre dans une boucle infinie (while True) qui gère l'interaction avec l'utilisateur et met à jour l'affichage en continu.
À l'intérieur de cette boucle, le taux de rafraîchissement est régulé à 60 images par seconde à l'aide de l'horloge (time_delta = clock.tick(60)).
Gestion des événements d'interface utilisateur :
Le programme utilise une boucle for event in pygame.event.get(): pour capturer les événements d'interface utilisateur.
Les événements de bouton appuyé, curseur déplacé, etc., sont gérés en conséquence :
Lorsqu'un bouton est appuyé, les variables correspondantes sont mises à jour en fonction de l'action du bouton.
Lorsqu'un curseur est déplacé, les valeurs des paramètres sont mises à jour en fonction de la position du curseur.
Affichage des éléments d'interface utilisateur :
Le gestionnaire d'interface utilisateur est utilisé pour mettre à jour et afficher les éléments d'interface utilisateur (manager.update(time_delta/1) et manager.draw_ui(screen)).
Les boutons et curseurs affichent leurs états actuels en fonction des événements et des interactions de l'utilisateur.
Dessin des cercles :
Les cercles sont dessinés à l'aide de la fonction pygame.draw.circle() dans la boucle de dessin.
Les propriétés des cercles (position, rayon, couleur) sont calculées en fonction des paramètres actuels et sont dessinées sur l'écran.
Mise à jour des variables :
Les variables telles que rotation, nombreDeCercles, j, etc., sont mises à jour à chaque itération de la boucle.
La rotation des cercles est ajustée pour donner un effet de rotation.
D'autres paramètres tels que la couleur, le rayon, le nombre de cercles, etc., sont également mis à jour.
Affichage du fond (background) :
Si l'option backgroundBool est activée, un rectangle de couleur est dessiné en arrière-plan.
Conclusion :
En résumé, ce code est un programme interactif qui utilise Pygame et Pygame GUI pour créer une interface graphique permettant à l'utilisateur de dessiner des cercles avec divers paramètres ajustables. Les cercles sont dessinés en rotation avec des couleurs et des tailles variables, et l'interface utilisateur permet de modifier ces paramètres en temps réel.
