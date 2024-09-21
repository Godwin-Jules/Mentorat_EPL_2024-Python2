# Mentorat_EPL_2024-Python2

## Activité 1
### Exercice 1
Ecrire un programme qui fait le calcule entre deux nombres en fonction de l'opération de l'utilisateur

### Exercice 2
Ecrire un programme qui calcule la distance entre deux points $A(x_a, y_a)$ et $B(x_b, y_b)$. La formule de calcul de la distance entre deux points est donnée sous la forme suivante :

$d(A, B) = \sqrt{(x_a - x_b)^2 + (y_a - y_b)^2}$

### Exercice 3 : Première partie du jeu de devinette
Dans cette partie, l'utilisateur est amené à fixer la valeur maximale du nombre aléatoire à générer.  
Les éléments essentiels dans cet exercice sont :
- La génération d'un nombre aléatoire
- Contrôle de la saisie de l'utilisateur
- Le but dans cet exercice est d'aider l'utilisateur à gagner

### Exercice 4 : Deuxième partie du jeu de devinette
Dans cette partie, on permet à l'utilisateur de jouer selon le niveau de difficulté qui dépend de la valeur maximale du nombre aléatoire à générer.
- **Facile** : 100
- **Moyen** : 500
- **Difficile** :1000
Egalement pour cette partie le but est de permettre au joueur de gagner quelqu'en soit le nombre d'essais.

### Exercice 5 : Troisième partie du jeu de devinette
Dans cette partie on fixe ne nombre de tentatives à 15. On se permet de qualifier chaque joueur en fonction du nombre de tentatives réalisé :
- **[1 - 3]** tentatives => Voyant
- **[4 - 6]** tentatives => Sage Voyant
- **[7 - 9]** tentatives => Apprenti Voyant
- **[10 et plus]** tentatives => Pusillanime
Quelques notions ont aussi été introduites :
- **Score** : $Score = 1 - \frac{attempts}{15}$ (sous forme de pourcentage)
- **Historisation** des tentatives
- **Ecart-Type** des tentatives
- **Moyenne olympique** des tentatives

## Activité 2
### Exercice 1 à 4
Dans quatre (4) premiers exercices de cette activité, il est question de manipuler les données d'une base de données json à travers un projet du nom de **BMI** (**B**ody **M**ass **I**ndex). Voici quelques notions abordées selon l'ordre des différents exercices :
- Calcul du poids idéal (masse idéale) d'une personne connaissant son poids réel (masse réelle) et sa taille
- Calcul de l'IMC (Indice de Masse Corporelle) d'une personne
- Classification de l'IMC d'une personne selon les données suivantes
  - **Moins de 18.5** : Maigreur, Sous-poids;
  - **Entre 18.5 et 25** : Corpulence normale;
  - **Entre 25 et 30** : Surpoids;
  - **Entre 30 et 35** : Obésité (modérée);
  - **Entre 35 et 40** : Obésité sévère;
  - **Plus de 40** : Obésité morbide ou massive.
- Lecture des données d'un fichier json afin de faire correspondre, en fonction de l'IMC de la personne,
  - **Diagnostic** : un diagnostic de l'état de santé de la personne
  - **Raison** : la raison du diagnostic (pourquoi la personne est dans cet état)
  - **Conseil** : un conseil à la personne pour améliorer son état de santé
  - Ces données se trouvent dans le fichier [sante.json](./Activite02/database/sante.json)
- Un système de gestion des utilisateurs qui permet de :
  - **Ajouter** un utilisateur
  - **Supprimer** un utilisateur
  - **Modifier** les informations d'un utilisateur
  - **Sauvegarder les données** des utilisateurs dans un fichier json

Un projet de même calibre a été réalisé dans le cadre de l'activité 2. Il s'agit de "Projet_IMC" que vous trouverez via lien [Projet_IMC](https://github.com/Godwin-Jules/Projet_IMC)

### Exercice 5
Cette partie consiste à chercher au minimum trois (3) projets (petit, moyen ou grand)

## Activité 3
Cette partie ne concerne rien que le POO en python

### Exercice 1
Une classe qui permet de manipuler les nombres complexes (Les éléments de l'ensemble des nombres complexes sont de la forme $a + bi$ où $a$ et $b$ sont des réels et $i$ est l'unité imaginaire telle que $i^2 = -1$). Les opérations suivantes sont implémentées :
- Somme de deux nombre complexes
- Produit de deux nombre complexes
- Conjugué d'un nombre complexe
- Module d'un nombre complexe
- Le carré d'un nombre complexe

### Exercice 2
Un petit système de gestion d'une entreprise. C'est un système qui permet de gérer les employés d'une entreprise avec leur hiérarchie, leur salaire, et leur prime. Les différentes classes qui ont été créées sont :
- **Employe** : La classe mère de tous les employés qui contient les informations de base de chaque employé
- **Responsable** : La classe fille qui hérite de la classe Employe et qui contient les informations spécifiques aux responsables comme les employés sous sa responsabilité
- **Commercial** : La classe fille qui hérite de la classe Employe et qui contient les informations spécifiques aux commerciaux comme le chiffre d'affaire réalisé et une autre logique de calcul de son salaire
- **Personnel** : La classe qui permet de gérer tous les employés de l'entreprise et qui fournie une méthode permettant de calculer la masse salariale de l'entreprise (la somme des salaires de tous les employés à la fin du mois)

### Exercice 3
Un système de gestion d'une bibliothèque. Les classes implémentées sont :
- **Livre** : La classe qui permet de représenter les livres avec leurs informaions de base
- **Membre** : La classe qui permet de représenter les membres de la bibliothèque
- **Bibliotheque** : La classe qui permet de gérer les livres et les membres de la bibliothèque. Elle permet d'ajouter un livre, d'emprunter un livre, de rendre un livre, de lister les livres empruntés par un membre, de lister les livres disponibles, de lister les membres de la bibliothèque

### Exercice 4
Cette exercice met plus en avant la notion de l'héritage et du Polymorphisme avec la surchage de méthodes. C'est le fameux jeu de pokémons. Les classes implémentées sont :
- **Pokemon** : La classe mère de tous les pokémons qui contient les informations de base de chaque pokémon
- **PokemonEau** : La classe fille qui hérite de la classe Pokemon et qui contient les informations spécifiques aux pokémons de type eau
- **PokemonFeu** : La classe fille qui hérite de la classe Pokemon et qui contient les informations spécifiques aux pokémons de type feu
- **PokemonPlante** : La classe fille qui hérite de la classe Pokemon et qui contient les informations spécifiques aux pokémons de type plante

**NB** :
Toutes les informations sur les différentes activités sont disponible dans le repertoire [Enonces](./Enonces) du projet