# Knarr

Ceci est un projet informatique pour l'Esigelec.

## Comment faire fonctionner le programme ?

Le programme nécessite un écran de 1920x1080 pixels pour fonctionner correctement. Il est possible de le lancer en utilisant la commande `python main.py` dans la console.

## Comment le programme fonctionne-t-il ?

### Le jeu se lance

Lorsque le programme est lancé, on arrive sur un menu principal. Il est possible de naviguer dans le menu grâce à la souris.
On tombe sur :
- Un bouton pour se connecter
- Un bouton pour s'inscrire
- Un bouton pour les options

(le bouton pour quitter le jeu est en haut à droite de l'écran et est toujours visible)

### L'inscription

Lorsque l'on clique sur le bouton pour s'inscrire, on arrive sur un écran où il est possible de rentrer un nom d'utilisateur et un mot de passe. Il est possible de revenir en arrière en cliquant sur le bouton "Retour".

### La connexion

Lorsque l'on clique sur le bouton pour se connecter, on arrive sur un écran où il est possible de rentrer un nom d'utilisateur et un mot de passe. Il est possible de revenir en arrière en cliquant sur le bouton "Retour".

### Les options

Lorsque l'on clique sur le bouton pour les options, on arrive sur un écran où il est possible de régler le volume de la musique et des bruitages. Il est possible de revenir en arrière en cliquant sur le bouton "Retour".

### Les réglages de la partie

Une fois connecté, on arrive sur un écran où il est possible de commencer une partie. Il est possible de revenir en arrière en cliquant sur le bouton "Retour". Lorsque l'on clique sur le bouton pour commencer une partie, on arrive sur un écran où il est possible de choisir un nombre de joueurs grâce aux boutons "+" et "-". Une fois le nombre de joueurs choisi, il est possible de commencer la partie en cliquant sur le bouton "Valider".

*A noter que l'on ne peut affronter que des IA pour le moment.*

### Le jeu

Le jeu se déroule par tour.
Le joueur (vous) commence.
Les cartes échange et influence sont en haut à gauche de l'écran, juste en dessous vous trouverez le plateau de jeu où vous pourrez voir votre avancement et celui de vos adversaires.
En bas du plateau de jeu, vous trouverez les cartes de la pioche associées à leur couleur.
En bas à droite de l'écran, vous trouverez les cartes que vous avez en main et au dessus, vous trouverez votre équipage.
Au centre de l'écran, vous trouverez votre bateau avec vos bracelets et vos recrues.

### Comment déplacer une carte et comment faire du commerce ?

Pour déplacer une carte, il suffit de cliquer dessus et de la déplacer à l'endroit souhaité.
Pour faire du commerce, il suffit de cliquer sur les boutons à coté du bateau pour récupérer vos gains. Cliquer sur la flèche pour passer cette étape.

### Fin du tour

Lorsque vous n'avez plus rien à faire, cliquez sur le bouton en bas à gauche pour passer au tour suivant.
Lorque un tour complet est passé, le jeu vérifie si un joueur a gagné. Si c'est le cas, le jeu s'arrête et un écran de fin de partie s'affiche. Et les données sont enregistrées dans la base de données.
